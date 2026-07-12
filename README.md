````markdown
# 🤖 PolicyGPT: Enterprise Document Assistant

A lightweight and production-ready **Retrieval-Augmented Generation (RAG)** application that enables users to upload enterprise policy PDFs and ask natural language questions with grounded, context-aware responses powered by the **Groq API (Llama 3.1)**.

Built with a custom native Python retrieval pipeline that eliminates heavy vector databases and SQLite dependencies, ensuring fast startup, lightweight deployment, and efficient document search.

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-F55036?style=for-the-badge)
![Llama](https://img.shields.io/badge/Llama_3.1-6E40C9?style=for-the-badge)
![PyPDF](https://img.shields.io/badge/PyPDF-0A66C2?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Native_Python-success?style=for-the-badge)

---

## 📁 Project Structure

```bash
PolicyGPT/
│
├── .streamlit/
│   └── secrets.toml      # Secure API key storage
│
├── app.py                # Streamlit dashboard
├── rag.py                # Native RAG retrieval engine
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

# Screenshots

![Home Page](screenshots/home.png)

![Document Upload](screenshots/upload.png)

![Chat Interface](screenshots/chat.png)

---

## 🚀 Features

### 📄 Intelligent PDF Analysis

- Upload enterprise policy documents
- Native PDF text extraction
- Supports multi-page documents
- Fast document processing

### 🧠 Retrieval-Augmented Generation (RAG)

- Custom context retrieval pipeline
- Dynamic text chunking
- Context-aware question answering
- Grounded responses with reduced hallucinations

### ⚡ High-Performance Architecture

- Native Python retrieval engine
- No SQLite dependency
- No FAISS or ChromaDB required
- Lightweight cloud deployment
- Optimized for low-latency inference

### 📚 Source Citation

- Displays the document page used for every answer
- Transparent response generation
- Easy compliance verification

### 🎨 Modern Enterprise Dashboard

- Professional dark-themed interface
- Interactive chat experience
- Session management
- Clear conversation history
- Responsive layout

---

## 🌐 Live Demo

**Application**

https://policygpt123.streamlit.app/

**Video Walkthrough**

https://youtu.be/mV8a-aEJzIA?si=bUYkg7GJqEx3fIEG

**GitHub Repository**

https://github.com/saikarthik2906/PolicyGPT

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/saikarthik2906/PolicyGPT.git

cd PolicyGPT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create the Streamlit secrets folder

```bash
mkdir .streamlit
```

Create `secrets.toml`

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Purpose of the Project

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Large Language Model integration
- Enterprise document intelligence
- Native Python information retrieval
- Prompt engineering
- Context grounding
- PDF document processing
- Streamlit application development
- Cloud deployment optimization
- Secure API management

Perfect for:

- GenAI portfolio projects
- Enterprise AI assistants
- RAG demonstrations
- LLM application showcases
- Compliance document analysis
- Streamlit deployments

---

## 🚀 Future Enhancements

- Semantic vector search using Pinecone
- OCR support for scanned PDFs
- Multi-document querying
- Cross-document comparison
- Conversation export
- Authentication and user management

---

## 👨‍💻 Author

**Sai Karthik**

Building lightweight, scalable, and production-ready Generative AI applications for enterprise use.
````
