# Offline RAG-based PDF Question Answering System (Chatbot)
Developed an Offline RAG-based PDF Question Answering System using Python, FastAPI, LangChain, Ollama, ChromaDB, and Streamlit. Implemented document ingestion, text chunking, embeddings, vector database retrieval, and local LLM integration to answer questions from PDF documents without internet access. 
Built a fully offline and secure AI chatbot solution suitable for internal enterprise and defence environments.

# Tech Stack:
- Python
- FastAPI
- LangChain
- Ollama
- ChromaDB / FAISS
- Sentence Transformers
- PyPDF
- Streamlit (Frontend)

# Architecture Flow:
```
PDF → Text Extraction → Chunking → Embedding → Vector DB
                                                ↓
User Question → Embedding → Similarity Search → LLM (Ollama)
                                                ↓
                                           Final Answer
```
# Project Folder
offline-rag-chatbot/
│
├── backend/
│   ├── app.py
│   ├── rag_pipeline.py
│   ├── upload_pdfs/
│   └── vector_db/
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md

# How System Works
## PDF Upload
User Upload PDF
        ↓
Text Extract
        ↓
Chunking
        ↓
Embedding
        ↓
Store in ChromaDB

## Question Asking
User Question
        ↓
Convert to Embedding
        ↓
Similarity Search
        ↓
Relevant Chunks
        ↓
Send to LLM
        ↓
Generate Answer

# Features
- ✅ Fully Offline
- ✅ No Internet Required
- ✅ Multiple PDF Support
- ✅ Local LLM using Ollama
- ✅ Vector Database Search
- ✅ FastAPI APIs
- ✅ Streamlit UI
- ✅ Secure for Defence/Internal Projects

# Advanced Features (Optional)
- Chat History Memory
- Multi-user Login
- Role-based Access
- Citation/Sources
- GPU Acceleration
- Docker Deployment
- FAISS instead of ChromaDB
- Hybrid Search
- OCR Support
- DOCX/TXT support
- Voice Chat
- Agentic AI
- Local Whisper STT...

# Run Backend
```
cd backend
uvicorn app:app --reload

Backend URL:
http://127.0.0.1:8000

Swagger API:
http://127.0.0.1:8000/docs
```
# Run Streamlit (frontend)
```
cd frontend
streamlit run streamlit_app.py

Frontend URL:
http://localhost:8501
```

## Note
Most production AI apps still use python 3.11 not 3.13(not stable)