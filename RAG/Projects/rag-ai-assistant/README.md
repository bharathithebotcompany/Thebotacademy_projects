
# RAG AI Assistant 🚀
(End-to-End Retrieval-Augmented Generation System)

---

## 📌 Project Overview

The **RAG AI Assistant** is a full-stack, AI-powered document question-answering system built using **Retrieval-Augmented Generation (RAG)**.  
Users can upload PDF documents and ask natural language questions. The system retrieves relevant document content using semantic search and generates accurate, context-aware answers using open-source Large Language Models (LLMs).

This project is designed to be:
- **100% free & open-source**
- **Production-ready**
- **Interview & resume worthy**
- **Deployable using Docker**

---

## 🎯 Objectives

- Build a document-based AI assistant without paid APIs
- Implement semantic search using embeddings
- Store and retrieve vectors efficiently
- Generate grounded answers using LLMs
- Provide a clean frontend chat interface
- Follow industry-level backend architecture
- Support Dockerized deployment

---

## 🧠 Key Features

- 📄 PDF document upload
- ✂️ Intelligent text chunking with overlap
- 🔢 Embeddings using SentenceTransformers
- 📦 FAISS vector database
- 🤖 Free HuggingFace LLM (FLAN-T5)
- 💬 Chat-based UI (React)
- 🗄️ Chat history stored in SQLite
- 🐳 Dockerized backend & frontend
- 🌐 Nginx reverse proxy
- 🆓 Fully free tech stack

---

## 🏗️ System Architecture

### High-Level Architecture

```
User (Browser)
   ↓
React Frontend
   ↓
Nginx Reverse Proxy
   ↓
FastAPI Backend
   ↓
RAG Pipeline
 ├─ Document Loader
 ├─ Text Chunker
 ├─ Embedding Model
 ├─ FAISS Vector Store
 └─ LLM Answer Generator
```

---

### RAG Pipeline Flow

```
PDF Upload
 → Text Extraction
 → Chunking
 → Embedding Generation
 → FAISS Storage

User Question
 → Query Embedding
 → Similarity Search (FAISS)
 → Context Retrieval
 → Prompt Construction
 → LLM Answer Generation
 → Chat History Storage
```

---

### Component Description

#### Frontend (React + Vite)
- Chat interface
- PDF upload
- Displays AI responses
- Communicates with backend via REST APIs

#### Backend (FastAPI)
- REST API layer
- Document ingestion
- RAG orchestration
- Chat history logging

#### Vector Database (FAISS)
- Stores semantic embeddings
- Enables fast similarity search
- Local & free

#### LLM (HuggingFace)
- FLAN-T5-base
- Open-source
- CPU compatible

#### Database (SQLite)
- Stores user questions & answers
- Timestamped chat history

---

## 🧰 Technology Stack

### Backend
- Python 3.10
- FastAPI
- LangChain
- HuggingFace Transformers
- SentenceTransformers
- FAISS (CPU)
- SQLite + SQLAlchemy

### Frontend
- React (Vite)
- Tailwind CSS
- Axios

### DevOps
- Docker
- Docker Compose
- Nginx
- Git & GitHub

---

## 📂 Project Structure

```
rag-ai-assistant/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── rag/
│   │   ├── db/
│   │   ├── core/
│   │   └── models/
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── api/
│   │   └── pages/
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup Guide

### Prerequisites
- Python 3.10+ (3.10 recommended)
- Node.js 18+
- Docker & Docker Compose
- Git

---

### Backend Setup (Local)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at:
```
http://127.0.0.1:8000
```

---

### Frontend Setup (Local)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
```
http://localhost:5173
```

---

### Docker Setup (Recommended)

```bash
docker compose --profile prod up --build
```

Application runs at:
```
http://localhost
```

---

## 📡 API Documentation

### Base URL
```
/api
```

---

### Health Check

**GET** `/health`

Response:
```json
{
  "status": "healthy"
}
```

---

### Upload Document

**POST** `/upload`

Form Data:
- `file` (PDF)

Response:
```json
{
  "filename": "sample.pdf",
  "status": "Uploaded, chunked & indexed (40 chunks)"
}
```

---

### Chat with AI

**POST** `/chat`

Request:
```json
{
  "question": "What is the objective of the document?"
}
```

Response:
```json
{
  "answer": "The document explains..."
}
```

---

### Chat History

**GET** `/history`

Response:
```json
[
  {
    "id": 1,
    "question": "...",
    "answer": "...",
    "created_at": "2025-01-01T10:30:00"
  }
]
```

---

## 🧪 Testing

```bash
pytest
```

Includes:
- API health test
- Input validation tests

---

## 🚀 Deployment

- Backend: Docker container
- Frontend: Nginx static hosting
- Reverse Proxy: Nginx
- Fully containerized using Docker Compose

---

## 🧠 Interview Explanation (Quick)

> “I built an end-to-end RAG-based AI assistant using FastAPI and React.  
Documents are embedded using SentenceTransformers, stored in FAISS, and retrieved semantically to generate grounded answers using a HuggingFace LLM.  
The entire system is Dockerized with an Nginx reverse proxy and uses only free, open-source tools.”

---

## 🔮 Future Enhancements

- Multi-document support
- Source citation in answers
- Streaming responses
- Authentication
- PostgreSQL instead of SQLite
- Kubernetes deployment

---

## 📚 References

- FastAPI Documentation
- LangChain Documentation
- HuggingFace Transformers
- FAISS by Meta AI
- Research papers on Retrieval-Augmented Generation

---

© RAG AI Assistant Project
