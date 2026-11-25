# 🧠 RAG — All in One

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Latest-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B35?style=for-the-badge)
![Cohere](https://img.shields.io/badge/Cohere-Reranker-coral?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A complete, hands-on implementation of every major RAG technique.**  
From basic ingestion pipelines to multimodal RAG, hybrid search, reranking, and advanced retrieval strategies — all in one place.

[📚 Techniques](#-techniques-covered) · [🚀 Quick Start](#-quick-start) · [📂 Structure](#-project-structure) · [🧪 Examples](#-usage-examples)

</div>

---

## 📌 Overview

RAG (Retrieval-Augmented Generation) is the backbone of modern AI applications. This repository is a **structured learning and reference guide** covering every core RAG concept with clean, well-commented implementations.

Whether you're preparing for interviews, building production AI systems, or exploring state-of-the-art retrieval techniques — this repo has you covered.

> Built while studying **MSc Computer Science (AI)** at the University of Pisa 🇮🇹

---

## 📚 Techniques Covered

| # | Technique | File | Description |
|---|---|---|---|
| 1 | **Ingestion Pipeline** | `ingestion_pipeline.py` | Load → Chunk → Embed → Store |
| 2 | **Retrieval Pipeline** | `retrival_pipeline.py` | Query → Retrieve → Generate |
| 3 | **Retrieval Methods** | `retrivel_methods.py` | Similarity, Score Threshold, MMR |
| 4 | **History-Aware RAG** | `history_aware_gen.py` | Conversational RAG with memory |
| 5 | **Multi-Query Retrieval** | `multiQueryRetrivel.py` | Query expansion with LLM |
| 6 | **Reciprocal Rank Fusion** | `reciprocalRankfusion.py` | Fuse results from multiple queries |
| 7 | **Multimodal RAG** | `8_multi_modal_rag.ipynb` | RAG over text + tables + images |
| 8 | **Hybrid Search** | `12_hybrid_search.ipynb` | Dense (vector) + Sparse (BM25) |
| 9 | **Reranker** | `13_reranker.ipynb` | Cohere reranking for precision |

---

## 🏗️ Core RAG Architecture

```
📄 Document(s)
     │
     ▼
📦 Chunking Strategy
  ├── CharacterTextSplitter
  ├── chunk_by_title (Unstructured)
  └── Custom strategies
     │
     ▼
🔢 Embedding Generation
  └── OpenAI text-embedding-3-small
     │
     ▼
🗄️ Vector Store (ChromaDB)
  └── Cosine similarity index
     │
     ▼
❓ User Query
     │
     ├──────────────────────────────────┐
     ▼                                  ▼
🔍 Dense Retrieval              📝 Sparse (BM25)
  (Semantic Search)             (Keyword Search)
     │                                  │
     └──────────┬───────────────────────┘
                ▼
         🔀 Hybrid Fusion
         (EnsembleRetriever / RRF)
                │
                ▼
         📊 Reranking
         (Cohere Rerank v3)
                │
                ▼
         🤖 LLM Generation
         (GPT-4o / GPT-4o-mini)
                │
                ▼
         💬 Final Answer + Sources
```

---

## 📂 Project Structure

```
rag-all-in-one/
│
├── 📓 Notebooks/
│   ├── 8_multi_modal_rag.ipynb      # Multimodal RAG (text + images + tables)
│   ├── 12_hybrid_search.ipynb       # Hybrid search (BM25 + Vector)
│   └── 13_reranker.ipynb            # Cohere reranking pipeline
│
├── 🐍 Scripts/
│   ├── ingestion_pipeline.py        # Document loading + chunking + embedding
│   ├── retrival_pipeline.py         # Full RAG query pipeline
│   ├── retrivel_methods.py          # All retrieval strategy comparisons
│   ├── history_aware_gen.py         # Conversational RAG with chat memory
│   ├── multiQueryRetrivel.py        # LLM-generated query variations
│   ├── reciprocalRankfusion.py      # RRF algorithm from scratch
│   └── test_api.py                  # OpenAI API connection test
│
├── 📁 docs/                         # Place your .txt / .pdf documents here
├── 📁 db/
│   └── chroma_db/                   # Persistent vector database
│
├── .env.example                     # Environment variable template
├── requirements.txt
└── README.md
```

---

## 🔍 Technique Deep Dives

### 1. 📥 Ingestion Pipeline (`ingestion_pipeline.py`)

The foundation of every RAG system. Loads documents, splits them into chunks, generates embeddings, and stores them in ChromaDB.

```python
documents = load_documents(docs_path="docs")   # DirectoryLoader for .txt files
chunks    = split_documents(documents)          # CharacterTextSplitter (800 chars)
db        = create_vector_store(chunks)         # ChromaDB with cosine similarity
```

**Key config:** Chunk size `800`, embedding model `text-embedding-3-small`, distance metric `cosine`.

---

### 2. 🔎 Retrieval Methods (`retrivel_methods.py`)

Three retrieval strategies compared side by side:

```python
# Method 1: Basic similarity (top-k)
retriever = db.as_retriever(search_kwargs={"k": 3})

# Method 2: Score threshold (quality filter)
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 5, "score_threshold": 0.3}
)

# Method 3: MMR — Maximum Marginal Relevance (diverse results)
retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "fetch_k": 10, "lambda_mult": 0.5}
)
```

| Method | Best For |
|---|---|
| Basic Similarity | Fast, simple queries |
| Score Threshold | Avoiding irrelevant chunks |
| MMR | Diverse, non-redundant results |

---

### 3. 💬 History-Aware RAG (`history_aware_gen.py`)

Enables multi-turn conversations by rewriting follow-up questions to be standalone before retrieval.

```
User: "Who founded Microsoft?"   →  Bot answers...
User: "When was it?"             ←  Ambiguous!
         │
         ▼  LLM rewrites to:
"When was Microsoft founded?"
         │
         ▼
ChromaDB retrieval → GPT-4o-mini → Answer
```

---

### 4. 🔀 Multi-Query Retrieval (`multiQueryRetrivel.py`)

Generates 3 different query variations using an LLM to maximize document coverage:

```
Original: "How does Tesla make money?"

Generated:
  1. "What are Tesla's primary revenue streams?"
  2. "How does Tesla generate income from its products and services?"
  3. "What business segments contribute to Tesla's earnings?"

→ All 3 queries search ChromaDB independently
→ Results merged for broader coverage
```

---

### 5. 🏆 Reciprocal Rank Fusion (`reciprocalRankfusion.py`)

Implements RRF from scratch — a smart algorithm that fuses results from multiple query variations using position-based scoring:

```python
# RRF Score Formula
score(chunk) = Σ  1 / (k + rank_i)
# k=60,  rank_i = position in query_i results
# Documents appearing in multiple queries get boosted
```

---

### 6. 🖼️ Multimodal RAG (`8_multi_modal_rag.ipynb`)

Goes beyond text — processes PDFs containing text, tables, and images using Unstructured.io:

```python
elements = partition_pdf(
    filename=file_path,
    strategy="hi_res",                          # Accurate extraction
    infer_table_structure=True,                 # Tables as structured HTML
    extract_image_block_types=["Image"],        # Extract embedded images
    extract_image_block_to_payload=True         # Base64 image data
)
# Chunks contain: Text + Table HTML + Base64 Images
# GPT-4o handles all modalities in final generation
```

---

### 7. 🔀 Hybrid Search (`12_hybrid_search.ipynb`)

Combines dense (semantic) + sparse (keyword) retrieval:

```python
# Dense: understands meaning  ("space exploration company" → SpaceX)
vector_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Sparse: matches exact terms  ("Cybertruck" → Tesla Cybertruck)
bm25_retriever = BM25Retriever.from_documents(documents)

# Hybrid: best of both worlds
hybrid_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.7, 0.3]
)
```

---

### 8. 📊 Reranker (`13_reranker.ipynb`)

Applies Cohere Rerank v3 after hybrid search for precision:

```
Hybrid Search → Top 25 candidates
                      │
                      ▼
          Cohere Rerank (rerank-english-v3.0)
                      │
                      ▼
          Top 5 most relevant chunks → GPT-4o → Final Answer
```

This 2-stage approach (retrieve many → rerank → use few) consistently outperforms single-stage retrieval.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-all-in-one.git
cd rag-all-in-one
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env`:
```env
OPENAI_API_KEY=your_openai_api_key_here
CO_API_KEY=your_cohere_api_key_here     # Only needed for reranker notebook
```

### 4. Test your API connection

```bash
python test_api.py
```

### 5. Add your documents

Place `.txt` files in the `docs/` folder.

### 6. Run the ingestion pipeline

```bash
python ingestion_pipeline.py
```

### 7. Query your documents

```bash
python retrival_pipeline.py
```

---

## 📦 Requirements

```txt
langchain
langchain-community
langchain-openai
langchain-chroma
langchain-cohere
chromadb
openai
python-dotenv
rank-bm25
unstructured[all-docs]
pydantic
```

For multimodal RAG, also install system dependencies:

```bash
# Linux
apt-get install poppler-utils tesseract-ocr libmagic-dev

# macOS
brew install poppler tesseract libmagic
```

---

## 🧪 Usage Examples

**Basic RAG query**
```bash
python retrival_pipeline.py
```

**Conversational RAG with memory**
```bash
python history_aware_gen.py
```

**Multi-query + RRF**
```bash
python reciprocalRankfusion.py
```

**Hybrid search (notebook)**
```bash
jupyter notebook 12_hybrid_search.ipynb
```

**Reranker (notebook)**
```bash
jupyter notebook 13_reranker.ipynb
```

---

## 🧠 Key Concepts Learned

- RAG Architecture — Full end-to-end pipeline design
- Chunking Strategies — Character-based, title-based, semantic chunking
- Vector Embeddings — Dense representations with cosine similarity
- ChromaDB — Persistent local vector store with HNSW indexing
- Retrieval Methods — Similarity, threshold, MMR
- Hybrid Search — BM25 (sparse) + vector (dense) fusion
- Query Expansion — Multi-query retrieval with LLM rewriting
- Reciprocal Rank Fusion — Score-based result merging algorithm
- Reranking — Cohere cross-encoder for precision boosting
- Multimodal RAG — Processing text, tables, and images together
- Conversational Memory — History-aware question rewriting
- Prompt Engineering — Grounded, source-aware LLM prompting

---

## 📊 RAG Technique Comparison

| Technique | Recall | Precision | Speed | Complexity |
|---|---|---|---|---|
| Basic Similarity | ⭐⭐⭐ | ⭐⭐ | ⚡⚡⚡ | Low |
| Score Threshold | ⭐⭐ | ⭐⭐⭐ | ⚡⚡⚡ | Low |
| MMR | ⭐⭐⭐ | ⭐⭐⭐ | ⚡⚡ | Medium |
| Multi-Query + RRF | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⚡⚡ | Medium |
| Hybrid Search | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⚡⚡ | Medium |
| Hybrid + Reranker | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⚡ | High |

---

## ⚠️ Important Notes

- **Never commit your `.env` file** — add it to `.gitignore`
- ChromaDB stores data in `db/chroma_db/` — delete this folder to reset the vector store
- The multimodal notebook requires a PDF with embedded images/tables
- The reranker notebook requires a Cohere API key (free tier at [cohere.com](https://cohere.com))

---

## 🔮 Roadmap

- [ ] Self-RAG (self-reflection + retrieval)
- [ ] RAPTOR (recursive tree retrieval)
- [ ] Adaptive RAG (query routing)
- [ ] ColBERT / late interaction retrieval
- [ ] Evaluation pipeline (RAGAS metrics)
- [ ] FastAPI wrapper for all techniques

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👨‍💻 Author

**Hamas Raja**  
MSc Computer Science (AI) — University of Pisa, Italy 🇮🇹  
BSc Software Engineering — Pakistan 🇵🇰

[![YouTube](https://img.shields.io/badge/YouTube-Hamas_Raja!-FF0000?style=flat&logo=youtube&logoColor=white)](https://www.youtube.com/@HamasRaja)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github&logoColor=white)](https://github.com/your-username)

---

<div align="center">

**⭐ Star this repo if it helped you understand RAG!**

*Built with curiosity, LangChain, and too much coffee ☕*

</div>
