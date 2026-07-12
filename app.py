import streamlit as st
import os
import tempfile
from rag import process_pdf, get_answer  # your existing RAG helper module

# ------------------------------------------------------------------
# Page config
# ------------------------------------------------------------------
st.set_page_config(
    page_title="PolicyGPT | Enterprise Compliance Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------
# EY Inspired Theme: Deep Charcoal, Premium Light Gray, & Active Yellow
# Polished / production-grade pass — same palette, more refined execution
# ------------------------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
:root {
    --charcoal: #1E1E1E;
    --charcoal-2: #242424;
    --charcoal-3: #2C2C2C;
    --charcoal-4: #333333;
    --yellow: #FFE600;
    --yellow-dim: rgba(255, 230, 0, 0.14);
    --gray-bg: #141414;
    --gray-border: #333333;
    --gray-text: #D8D8D8;
    --gray-muted: #8A8A8A;
    --user-bubble: #2A2410;
    --bot-bubble: #202020;
}

/* Base Canvas — Full Dark Mode */
html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMain"] {
    background-color: var(--gray-bg) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
[data-testid="stAppViewContainer"] { color: #EDEDED !important; }
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stDecoration"] { display: none !important; }

/* Layout */
.block-container {
    padding-top: 1.75rem !important;
    padding-bottom: 3rem !important;
    max-width: 1180px !important;
    margin: 0 auto;
}

/* ---------------- Header ---------------- */
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.4rem 2rem;
    background: linear-gradient(135deg, #1E1E1E 0%, #151515 100%);
    border-radius: 10px;
    border: 1px solid #2E2E2E;
    margin-bottom: 2rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    width: 100%;
    position: relative;
    overflow: hidden;
}
.header-container::before {
    content: "";
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 5px;
    background: var(--yellow);
}

.header-title-area { display: flex; align-items: center; gap: 14px; }

.logo-mark {
    width: 42px; height: 42px;
    background: var(--yellow);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
}

.brand-text h1 {
    font-size: 1.5rem !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    margin: 0 !important;
    padding: 0 !important;
    letter-spacing: -0.02em;
}
.brand-text p {
    font-size: 0.82rem !important;
    color: #ADADAD !important;
    margin: 3px 0 0 0 !important;
    font-weight: 500;
}

.badge-secure {
    background-color: var(--yellow-dim);
    border: 1px solid rgba(255, 230, 0, 0.4);
    color: var(--yellow) !important;
    padding: 7px 16px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 7px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    white-space: nowrap;
}
.badge-secure .pulse-dot-live {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--yellow);
    box-shadow: 0 0 0 rgba(255,230,0,0.5);
    animation: pulseGlow 2s infinite;
}
@keyframes pulseGlow {
    0%   { box-shadow: 0 0 0 0 rgba(255,230,0,0.5); }
    70%  { box-shadow: 0 0 0 6px rgba(255,230,0,0); }
    100% { box-shadow: 0 0 0 0 rgba(255,230,0,0); }
}

/* ---------------- Sidebar ---------------- */
section[data-testid="stSidebar"] {
    background-color: var(--charcoal) !important;
    border-right: 1px solid #2E2E2E;
}
section[data-testid="stSidebar"] > div { padding-top: 1.5rem; }

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] label {
    color: #D8D8D8 !important;
}

.sidebar-title {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #7A7A7A !important;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.sidebar-title::after {
    content: "";
    flex: 1;
    height: 1px;
    background: #333333;
}

[data-testid="stFileUploaderDropzone"] {
    background-color: var(--charcoal-2) !important;
    border: 1.5px dashed #444444 !important;
    border-radius: 8px !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
    border-color: var(--yellow) !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzoneInstructions"] span,
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzoneInstructions"] small {
    color: #B8B8B8 !important;
}

.doc-card {
    background: var(--charcoal-3);
    border: 1px solid #3A3A3A;
    border-left: 3px solid var(--yellow);
    border-radius: 6px;
    padding: 14px 16px;
    margin-top: 1rem;
}
.doc-name {
    font-size: 0.85rem;
    font-weight: 600;
    color: #FFFFFF !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.doc-meta {
    font-size: 0.73rem;
    color: #999999 !important;
    margin-top: 4px;
}
.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.73rem;
    color: var(--yellow) !important;
    font-weight: 600;
    margin-top: 10px;
}
.pulse-dot {
    width: 6px; height: 6px;
    background-color: var(--yellow);
    border-radius: 50%;
    animation: pulseGlow 2s infinite;
}

section[data-testid="stSidebar"] button {
    background-color: transparent !important;
    border: 1px solid #444444 !important;
    color: #B0B0B0 !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    transition: all 0.15s ease;
}
section[data-testid="stSidebar"] button:hover {
    border-color: var(--yellow) !important;
    color: var(--yellow) !important;
    background-color: var(--yellow-dim) !important;
}

/* ---------------- Empty / Info Panels ---------------- */
.empty-state {
    background: var(--charcoal-2) !important;
    border: 1px solid var(--gray-border) !important;
    border-radius: 10px !important;
    padding: 3rem 2.75rem !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    margin-bottom: 1.5rem !important;
}
.empty-state h3 {
    color: #FFFFFF !important;
    font-weight: 800 !important;
    font-size: 1.3rem !important;
    margin-top: 0 !important;
    margin-bottom: 0.6rem !important;
}
.empty-state p, .empty-state div { color: #B8B8B8 !important; font-size: 0.95rem !important; line-height: 1.65 !important; }
.empty-state b { color: var(--yellow) !important; }

.icon-badge {
    width: 56px; height: 56px;
    background: var(--charcoal-3);
    border: 1px solid var(--gray-border);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem;
    margin-bottom: 1.25rem;
}

/* Real clickable suggestion pills (Streamlit buttons in main content area) */
[data-testid="stMain"] div[data-testid="stButton"] button {
    background: var(--charcoal-3) !important;
    border: 1px solid var(--gray-border) !important;
    color: #E8E8E8 !important;
    border-radius: 20px !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    padding: 8px 16px !important;
    transition: all 0.15s ease !important;
    white-space: normal !important;
}
[data-testid="stMain"] div[data-testid="stButton"] button:hover {
    border-color: var(--yellow) !important;
    color: var(--yellow) !important;
    background: var(--yellow-dim) !important;
}
[data-testid="stMain"] div[data-testid="stButton"] button:focus:not(:active) {
    border-color: var(--yellow) !important;
    color: var(--yellow) !important;
    box-shadow: none !important;
}

.section-label {
    font-size: 0.75rem;
    font-weight: 700;
    color: #A0A0A0;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
}

/* ---------------- Chat ---------------- */
[data-testid="stChatMessage"] {
    border-radius: 10px !important;
    padding: 1.1rem 1.25rem !important;
    margin-bottom: 1rem !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.22);
    background-color: var(--bot-bubble) !important;
    border: 1px solid var(--gray-border) !important;
}
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] li {
    color: #F2F2F2 !important;
    font-size: 0.95rem !important;
    line-height: 1.65 !important;
}

/* Bot (assistant) messages — white text, neutral dark bubble */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
    background-color: var(--bot-bubble) !important;
    border-left: 3px solid #4A4A4A !important;
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stMarkdownContainer"] li {
    color: #FFFFFF !important;
}

/* User messages — yellow accent, dark bubble with yellow text/border */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background-color: var(--user-bubble) !important;
    border: 1px solid rgba(255, 230, 0, 0.35) !important;
    border-left: 3px solid var(--yellow) !important;
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"] li {
    color: var(--yellow) !important;
    font-weight: 500;
}

.source-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: var(--yellow-dim);
    border: 1px solid rgba(255, 230, 0, 0.45);
    color: var(--yellow) !important;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 5px 10px;
    border-radius: 6px;
    margin-top: 10px;
    letter-spacing: 0.01em;
}

[data-testid="stChatInput"] {
    border-radius: 10px !important;
    border: 1.5px solid var(--gray-border) !important;
    background: var(--charcoal-2) !important;
}
[data-testid="stChatInput"] textarea {
    color: #FFFFFF !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #777777 !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: var(--yellow) !important;
    box-shadow: 0 0 0 3px var(--yellow-dim) !important;
}

/* Toast / spinner text tone */
[data-testid="stSpinner"] p { color: #C8C8C8 !important; font-weight: 500; }
[data-testid="stToast"] { background-color: var(--charcoal-2) !important; color: #FFFFFF !important; }

/* ---------------- Footer ---------------- */
footer, #MainMenu { visibility: hidden; }
.app-footer {
    border-top: 1px solid var(--gray-border);
    padding-top: 1.25rem;
    margin-top: 3rem;
    font-size: 0.75rem;
    color: var(--gray-muted);
    text-align: center;
    letter-spacing: 0.02em;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Secrets Validation
# ------------------------------------------------------------------
if "GROQ_API_KEY" in st.secrets:
    groq_key = st.secrets["GROQ_API_KEY"]
else:
    st.error("❌ Configuration Error: 'GROQ_API_KEY' not found in your application secrets.")
    st.stop()

# ------------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------------
def format_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ["B", "KB", "MB"]:
        if size < 1024:
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"

# ------------------------------------------------------------------
# Enterprise Top Header Bar
# ------------------------------------------------------------------
st.markdown("""
<div class="header-container">
    <div class="header-title-area">
        <div class="logo-mark">🛡️</div>
        <div class="brand-text">
            <h1>PolicyGPT</h1>
            <p>Enterprise Compliance &amp; Knowledge Discovery Engine</p>
        </div>
    </div>
    <div class="badge-secure">
        <span class="pulse-dot-live"></span>
        Secure Node Session
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Sidebar: Document Control Panel
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown('<p class="sidebar-title">Data Source</p>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload reference PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        st.markdown(f"""
        <div class="doc-card">
            <div class="doc-name">📄 {uploaded_file.name}</div>
            <div class="doc-meta">{format_size(uploaded_file.size)} • Verified Matrix</div>
            <div class="status-indicator"><span class="pulse-dot"></span>Active Query Sandbox</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p class="sidebar-title">Session</p>', unsafe_allow_html=True)

    if st.button("Clear Cache & History", use_container_width=True):
        st.session_state.messages = []
        if "current_file_id" in st.session_state:
            del st.session_state.current_file_id
        st.rerun()

# ------------------------------------------------------------------
# Document Processing Sandbox
# ------------------------------------------------------------------
if not uploaded_file:
    st.markdown("""
    <div class="empty-state">
        <div class="icon-badge">📁</div>
        <h3>No Document Pipeline Active</h3>
        <p>Upload an enterprise compliance document, framework statement, or policy PDF from the left panel to begin analysis.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="app-footer">PolicyGPT Enterprise Engine • Corporate Intelligence System</div>', unsafe_allow_html=True)
    st.stop()

# Parse Document
file_id = f"{uploaded_file.name}_{uploaded_file.size}"
if "current_file_id" not in st.session_state or st.session_state.current_file_id != file_id:
    with st.spinner("Processing document matrix and executing embedding strategy..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        st.session_state.document_chunks = process_pdf(tmp_path)
        st.session_state.current_file_id = file_id
        st.session_state.messages = []
        os.unlink(tmp_path)
    st.toast(f"Connected to Pipeline: {uploaded_file.name}", icon="⚡")

# Initialize Chat State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Empty State / Initial Suggestions Workspace
SUGGESTED_QUERIES = [
    "What is the primary scope of this policy?",
    "Summarize the key compliance deadlines.",
    "Are there any penalty or governance clauses?",
]

pending_suggestion = None

if len(st.session_state.messages) == 0:
    st.markdown(f"""
    <div class="empty-state">
        <div class="icon-badge">✨</div>
        <h3>Document Successfully Parsed</h3>
        <p style="margin-bottom: 1.4rem;">Pipeline successfully extracted data matrix vectors from: <b>{uploaded_file.name}</b></p>
        <div class="section-label">Suggested Exploration Queries</div>
    </div>
    """, unsafe_allow_html=True)

    pill_cols = st.columns(len(SUGGESTED_QUERIES))
    for col, q in zip(pill_cols, SUGGESTED_QUERIES):
        with col:
            if st.button(q, key=f"suggestion_{q}", use_container_width=True):
                pending_suggestion = q

# ------------------------------------------------------------------
# Chat Execution Stream
# ------------------------------------------------------------------
for msg in st.session_state.messages:
    is_user = msg["role"] == "user"

    if is_user:
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
            if msg.get("pages"):
                pages_str = ", ".join(map(str, msg["pages"]))
                st.markdown(f'<div class="source-badge">📖 Verification Reference: pp. {pages_str}</div>', unsafe_allow_html=True)

# User Entry Interaction Hook
if question := st.chat_input("Ask a question about this document..."):
    st.session_state.messages.append({"role": "user", "content": question})
    st.rerun()

# Suggested-query pill click behaves exactly like typing + submitting
if pending_suggestion:
    st.session_state.messages.append({"role": "user", "content": pending_suggestion})
    st.rerun()

# Check last item to generate response asynchronously
if len(st.session_state.messages) > 0 and st.session_state.messages[-1]["role"] == "user":
    user_query = st.session_state.messages[-1]["content"]

    with st.spinner("Analyzing document contexts against vector indices..."):
        answer, pages = get_answer(st.session_state.document_chunks, groq_key, user_query)

    st.session_state.messages.append({"role": "assistant", "content": answer, "pages": pages})
    st.rerun()

# ------------------------------------------------------------------
# Footer Component
# ------------------------------------------------------------------
st.markdown('<div class="app-footer">PolicyGPT Enterprise Engine • Auditing and verification systems active. Core data remains sandboxed.</div>', unsafe_allow_html=True)