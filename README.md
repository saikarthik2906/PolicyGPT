# 🤖 PolicyGPT: Enterprise Document Assistant

A high-performance, ultra-lightweight enterprise Retrieval-Augmented Generation (RAG) system built in native Python. This production-ready dashboard extracts documentation intelligence from enterprise policy PDFs, processes textual boundaries natively to guarantee zero-latency execution, and surfaces structured compliance answers powered by the Groq API.

Designed to bypass the heavy system-level SQLite dependencies and native compilation bottlenecks common in cloud deployments, this platform achieves sub-second context matching and deterministic grounding.

---

# 🌐 Live Demo

**Live Application:**  
https://policygpt123.streamlit.app

**Video Walkthrough:**  
YouTube Link

**Source Code:**  
https://github.com/saikarthik2906/PolicyGPT

---

# 🛠 Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3.1
- PyPDF
- Native Python Retrieval Engine

---

# 🏗 System Architecture

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

# 📁 Project Structure

```text
PolicyGPT/
│
├── .streamlit/
│   └── secrets.toml       # Production API Keys & Environment Secrets
│
├── app.py                 # Streamlit UI & Core Dashboard Layout
├── rag.py                 # Lightweight Retrieval-Augmented Generation Logic
├── requirements.txt       # Project Dependencies
└── README.md              # Project Documentation
```

---

# 📸 Screenshots

(Add application screenshots here)

---

# 🚀 Features

## 🏢 Enterprise User Interface

- Modern dark-themed enterprise dashboard
- Dynamic welcome screen with quick-start queries
- Session state management for seamless navigation
- Responsive layout tailored for desktop and mobile runtimes

---

## 📄 Lightweight Document Retrieval

- Native Python context matching engine
- Zero external heavy database dependencies
- No SQLite
- No FAISS
- No Chroma
- No C++ compilation requirements
- Rapid startup times optimized for serverless architectures
- High-speed dynamic multi-page document parsing

---

## 🧠 Grounded AI Assistant

- Strict context confinement to prevent hallucinations
- Low-latency processing using Groq Cloud (Llama 3.1 Inference)
- Smart token utilization to stay well within strict API context limits
- Automated compliance guardrails

---

## 📚 Source Traceability

- Exact page citations mapping to source files
- Fully transparent, deterministic answer grounding
- Instant index clearing and hot-reload session resetting

---

# ⚙️ Installation & Usage

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

## 3. Configure API Keys

Create a local secret configuration directory and file.

```bash
mkdir .streamlit
```

Create a `secrets.toml` file inside `.streamlit/` and append your API credentials.

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Production Deployment

This project is fully engineered and optimized for seamless deployment on Streamlit Community Cloud.

1. Fork or clone this repository to your GitHub profile.

2. Deploy the repository using your Streamlit Cloud Workspace.

3. Open **Advanced Settings → Secrets**.

4. Paste your secure production environment values.

```toml
GROQ_API_KEY = "gsk_your_production_key_here"
```

5. Click **Save**.

The application will compile and go live in under **90 seconds**.

---

# 🎯 Purpose of the Project

This project demonstrates:

- Production-ready Generative AI & LLM Engineering architectures
- Implementation of custom, lightweight RAG strategies without bloatware
- Clean Data Engineering pipelines (Deterministic parsing, dynamic chunking)
- Secure cloud pipeline integration and credentials sanitization
- Stateless retrieval optimizations compatible up to Python 3.14

Perfect for enterprise portfolio showcases, lightweight compliance auditing applications, and high-performance LLM deployment architectures.

---

# 🔮 Roadmap

- [ ] Hybrid semantic vector search capabilities (Pinecone integration)
- [ ] OCR parsing engines for scanned image-only PDFs
- [ ] Simultaneous multi-document batch retrieval matrices
- [ ] Cross-document comparative compliance analysis systems
- [ ] Dynamic conversation history serialization and JSON export

---

# 👨‍💻 Author

## Sai Karthik

Building lightweight, production-ready Generative AI systems focused on high performance, enterprise scalability, and optimized cloud deployments.

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub!
