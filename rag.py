import re
from pypdf import PdfReader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


def native_text_splitter(text, chunk_size=1000, chunk_overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - chunk_overlap)
    return chunks


def process_pdf(file_path):
    reader = PdfReader(file_path)
    document_chunks = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            splits = native_text_splitter(text, chunk_size=1000, chunk_overlap=200)
            for split in splits:
                document_chunks.append({
                    "text": split,
                    "page": page_num + 1
                })
    return document_chunks


def calculate_relevance(query, document_text):
    words = re.findall(r'\w+', query.lower())
    doc_lower = document_text.lower()
    score = 0
    for word in words:
        score += doc_lower.count(word)
    return score


# Phrases that indicate the user is asking about the document as a whole
# (summary/overview) rather than looking up a specific fact. Keyword scoring
# fails for these because words like "document", "about", "contain" rarely
# appear verbatim in the policy text itself.
META_TRIGGERS = [
    "summary", "summarize", "summarise", "overview", "what is this document",
    "what does this document", "what it has", "what's in this", "what is in this",
    "tell me about the document", "tell me about this document", "tell me about doc",
    "describe the document", "describe this document", "what is this doc",
    "what does the document contain", "give me a brief",
]


def is_meta_question(question: str) -> bool:
    q = question.lower().strip()
    if any(trigger in q for trigger in META_TRIGGERS):
        return True
    # Short, vague questions that just mention "doc"/"document"
    # e.g. "tell me about document", "what it has?"
    word_count = len(q.split())
    if word_count <= 6 and ("document" in q or "doc" in q):
        return True
    return False


def get_relevant_chunks(document_chunks, question, max_chunks=3):
    """Keyword-matched chunks for specific factual questions."""
    scored_chunks = []
    for chunk in document_chunks:
        score = calculate_relevance(question, chunk["text"])
        scored_chunks.append((score, chunk))
    scored_chunks.sort(key=lambda x: x[0], reverse=True)
    return [item for score, item in scored_chunks[:max_chunks]]


def get_overview_chunks(document_chunks, max_pages=5):
    """A representative sample spanning the document, for meta/summary questions."""
    seen_pages = set()
    overview = []
    for chunk in document_chunks:
        if chunk["page"] not in seen_pages:
            overview.append(chunk)
            seen_pages.add(chunk["page"])
        if len(overview) >= max_pages:
            break
    return overview


def get_answer(document_chunks, groq_api_key, question):
    # Short-circuit handle for simple greetings
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "greetings"]
    if question.lower().strip() in greetings:
        return "Hello! 👋 I am PolicyGPT. I've indexed your document—feel free to ask any specific questions about its contents!", []

    if not document_chunks:
        return "I couldn't extract any readable text from this document.", []

    if is_meta_question(question):
        top_matches = get_overview_chunks(document_chunks, max_pages=5)
    else:
        top_matches = get_relevant_chunks(document_chunks, question, max_chunks=3)
        # If keyword matching found nothing useful (all zero scores),
        # fall back to an overview instead of an empty/near-random context.
        if all(calculate_relevance(question, m["text"]) == 0 for m in top_matches):
            top_matches = get_overview_chunks(document_chunks, max_pages=3)

    context = "\n\n".join(item["text"] for item in top_matches)
    pages = sorted(list(set(item["page"] for item in top_matches)))

    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0, groq_api_key=groq_api_key)

    prompt = ChatPromptTemplate.from_template("""
    You are PolicyGPT, an Enterprise Document Assistant.

    Answer the user's question using ONLY the provided context below.
    You may summarize, paraphrase, or describe the context to answer general
    questions about the document (e.g. "what is this about", "summarize this").
    Only reply with "I couldn't find that information in the uploaded document."
    if the context truly has nothing relevant to the question.

    Context:
    {context}

    Question:
    {question}
    """)

    messages = prompt.format_messages(context=context, question=question)
    response = llm.invoke(messages)

    return response.content, pages