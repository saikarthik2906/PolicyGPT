````markdown
# 🤖 PolicyGPT: Enterprise Document Assistant

A high-performance, ultra-lightweight enterprise **Retrieval-Augmented Generation (RAG)** system built in native Python. This production-ready dashboard extracts documentation intelligence from enterprise policy PDFs, processes textual boundaries natively to guarantee zero-latency execution, and surfaces structured compliance answers powered by the **Groq API**.

Designed to bypass the heavy system-level SQLite dependencies and native compilation bottlenecks common in cloud deployments, this platform achieves sub-second context matching and deterministic grounding.

---

## 🌐 Live Demo

- **Live Application:** https://policygpt123.streamlit.app/
- **Video Walkthrough:** https://youtu.be/mV8a-aEJzIA?si=bUYkg7GJqEx3fIEG
- **Source Code:** https://github.com/saikarthik2906/PolicyGPT

---

# 🏗️ System Architecture

PolicyGPT leverages a highly optimized, custom text-processing pipeline and localized contextual retrieval engine to isolate relevant document sections before passing bounded context to the Large Language Model.

```text
          [ Upload PDF ]
                 │
                 ▼
      Native Text Extraction (PyPDF)
                 │
                 ▼
    Custom Dynamic Boundary Chunking
                 │
                 ▼
 Deterministic Contextual Matching Matrix
                 │
      ┌──────────┴──────────┐
      ▼                     ▼
 Exact Match          Granular Page
 Extraction             Mapping
      │                     │
      └──────────┬──────────┘
                 ▼
 Groq Cloud (Llama 3.1 Inference)
                 │
                 ▼
 Structured Response + Source Citations
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3 |
| Framework | Streamlit |
| LLM | Groq API (Llama 3.1) |
| PDF Processing | PyPDF |
| Retrieval | Native Python Context Matching |
| Deployment | Streamlit Community Cloud |

---

# 🧠 Skills Demonstrated

### 🤖 Generative AI & LLM Engineering
- Retrieval-Augmented Generation (RAG)
- Prompt engineering
- Context grounding
- Hallucination reduction
- Token context optimization
- Response guardrails

### 🏗️ Systems Architecture
- Lightweight cloud-native deployment
- Zero cold-start optimization
- Stateless retrieval pipeline
- Python 3.14 compatibility

### 📄 Data Engineering
- Native PDF parsing
- Dynamic boundary chunking
- Metadata extraction
- Context serialization
- Deterministic retrieval

### 🔒 Security & Compliance
- Secure API key management
- Streamlit Secrets integration
- Sandboxed runtime configuration

### 💻 Full-Stack Development
- Interactive Streamlit dashboard
- Session state management
- Custom HTML/CSS styling
- Responsive enterprise UI

---

# 🚀 Key Features

## 🏢 Enterprise User Interface

- Modern dark-themed enterprise dashboard
- Dynamic welcome screen
- Query suggestions
- Real-time notifications
- Responsive layout

---

## 📄 Lightweight Document Retrieval

- Native Python retrieval engine
- No SQLite dependency
- No FAISS dependency
- No Chroma dependency
- No C++ compilation requirements
- Fast startup and deployment
- Multi-page document support

---

## 🧠 Grounded AI Assistant

- Strict context confinement
- Hallucination reduction
- Conversational query routing
- Compliance-focused responses
- Low-latency Groq inference

---

## 📚 Source Traceability

- Exact page citation
- Transparent answer grounding
- Document source tracking
- Conversation reset
- Index clearing

---

# 📁 Project Structure

```text
PolicyGPT/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── rag.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/saikarthik2906/PolicyGPT.git

cd PolicyGPT
```

---

## 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 3. Configure API Key

Create the hidden Streamlit configuration folder.

```bash
mkdir .streamlit
```

Create `secrets.toml`

```toml
GROQ_API_KEY = "your_groq_api_key"
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Production Deployment

The project is optimized for **Streamlit Community Cloud**.

### Steps

1. Fork or clone the GitHub repository.

2. Deploy it using Streamlit Community Cloud.

3. Open **Advanced Settings → Secrets**

Paste:

```toml
GROQ_API_KEY = "gsk_your_production_key"
```

4. Deploy.

The application typically becomes live in under **90 seconds**.

---

# 🔮 Roadmap

- [ ] Hybrid semantic vector search (Pinecone)
- [ ] OCR support for scanned PDF documents
- [ ] Multi-document retrieval
- [ ] Cross-document compliance analysis
- [ ] Better citation ranking
- [ ] Conversation history export

---

# 👨‍💻 Author

## Sai Karthik

Building lightweight, production-ready Generative AI systems focused on performance, scalability, and enterprise deployment.

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
````
