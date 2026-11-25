# Hybrid RAG — Grounded QA Agent

A feature-rich **Retrieval-Augmented Generation** system for grounded question answering. The pipeline combines hybrid retrieval (dense bi-encoder + BM25 keyword search), cross-encoder re-ranking, query rewriting, query-aware context summarization, inline citation generation, and automated citation verification — all orchestrated by a `RagAgent` class.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Why This Project?

This repository demonstrates a full RAG pipeline with every stage explicitly implemented:
- **Hybrid Retrieval**: Dense semantic search (FAISS) + BM25 lexical search fused with weighted linear combination
- **Two-Stage Re-ranking**: Cross-encoder re-ranks candidates for precision after initial retrieval
- **Query Rewriting**: LLM rewrites queries to maximize recall before retrieval
- **Query-Aware Summarization**: Each retrieved passage is summarized to highlight query-relevant information before generation
- **Grounded Generation with Citations**: Answers strictly cite retrieved context using `[1]`, `[2]`, … format
- **Automated Citation Verification**: JSON-structured verdict (`pass` / `partial` / `fail`) on every generated answer
- **Session History Corpus**: Previous responses are indexed and reused when a semantically similar query is re-encountered

It serves both as a learning project and a portfolio demonstration of advanced RAG design, applied NLP, and feature-rich information retrieval.

## 🌟 Features

### Core Agent Capabilities
- **Grounded QA with Citations**: Answers are generated strictly from retrieved context with inline `[N]` citations
- **Automated Citation Verification**: After every response the agent runs a citation checker that returns a structured `pass / partial / fail` verdict with per-claim support analysis
- **Query Rewriting**: LLM-powered query rewriting to expand abbreviations, resolve pronouns, and add synonyms before retrieval
- **Context Summarization**: Each retrieved passage is summarized with query-awareness before being fed to the generator
- **Session History Reuse**: Agent history is indexed in a separate FAISS corpus; similar past queries are answered instantly without re-retrieval
- **Structured JSON Logging**: Every interaction (query, improved query, response, context, citation verdict) is persisted to timestamped JSON log files

### Retrieval & Knowledge Management
- **Hybrid RAG Pipeline**:
  - Dense bi-encoder (FAISS inner-product index with `all-MiniLM-L6-v2`) for fast semantic retrieval
  - BM25 (`rank_bm25` + NLTK stemming) for lexical keyword retrieval
  - Weighted linear combination of normalized semantic and lexical scores
  - Cross-encoder re-ranking (`ms-marco-MiniLM-L-6-v2`) for high-precision final selection
  - Sliding-window chunking with configurable length and stride for context preservation
  - Overlapping chunk merging for coherent passage reconstruction
- **Automatic Deduplication**: Normalized text comparison prevents redundant document storage and re-indexing

### Technical Infrastructure
- **Flexible LLM Support**: Google Gemini (2.5 Pro / 2.5 Flash) and Hugging Face models (Qwen 2.5 1.5B/3B)
- **Modular Architecture**: Clean separation of corpus management, retrieval, agent logic, and utilities
- **Configurable Retrieval Parameters**: Weights, top-k values, chunk size, and stride are all tunable at runtime

## 🏗️ Architecture

```
hybrid_rag/
├── agent/                          # Core agent logic
│   └── rag_agent.py               # RagAgent: orchestrates query rewriting, retrieval,
│                                  #   summarization, generation, citation checking, and
│                                  #   history management using RAG components
├── rag/                           # Generic RAG components (corpus-agnostic)
│   ├── rag_corpus_manager.py      # Document chunking, embedding, FAISS & BM25 indexing
│   │                              #   (works with any corpus: knowledge base, history, etc.)
│   ├── rag_content_retriever.py   # Hybrid retrieval (semantic + lexical) with
│   │                              #   cross-encoder re-ranking (corpus-agnostic)
│   └── bm25_keyword_retriever.py  # BM25 keyword retriever (rank_bm25 + NLTK stemming)
├── utils/                         # Utilities
│   ├── model_loader.py            # Model initialization (Gemini, SentenceTransformer, CrossEncoder)
│   └── dataset_utils.py           # HuggingFace dataset loading (SQuAD default)
├── base/                          # Constants & configurations
│   └── constants.py               # Model names, timeouts, system prompt templates
├── config.py                      # Environment variable loading (HF_TOKEN, GOOGLE_API_KEY)
└── main.py                        # Entry point with end-to-end usage example
```

## 🚀 Quick Start

```python
from agent.rag_agent import RagAgent
from rag.rag_content_retriever import RAGContentRetriever
from rag.rag_corpus_manager import RAGCorpusManager
from utils.model_loader import ModelLoader
from utils.dataset_utils import DataSetUtil
from base.constants import Constants
from config import HF_TOKEN, GOOGLE_API_KEY
from google.genai import types

# ── 1. Load models ────────────────────────────────────────────────────────────
model_loader         = ModelLoader()
sentence_transformer = model_loader.load_sentence_embedding_model(hugging_face_token=HF_TOKEN)
cross_encoder        = model_loader.load_hf_cross_encoder(hugging_face_token=HF_TOKEN)
generative_model     = model_loader.load_gemini_generative_model(
    google_api_key=GOOGLE_API_KEY,
    config=types.GenerateContentConfig(temperature=0.7, system_instruction=None),
    model_name=Constants.ModelNames.Gemini.GEMINI_2_5_PRO,
)

# ── 2. Build the knowledge-base corpus ───────────────────────────────────────
knowledge_base_corpus = RAGCorpusManager(sentence_transformer)
dataset_util = DataSetUtil()
knowledge_base = dataset_util.load_qa_dataset(samples_count=10000)
knowledge_base_corpus.add_update_data_and_index(
    texts=[item["context"] for item in knowledge_base],
    metadatas=[{k: v for k, v in item.items() if k != "context"} for item in knowledge_base],
)

# ── 3. Create a separate corpus for agent history ────────────────────────────
history_corpus = RAGCorpusManager(sentence_transformer)
rag_retriever  = RAGContentRetriever(cross_encoder)
rag_agent      = RagAgent(history_corpus, rag_retriever)

# ── 4. Ask questions ──────────────────────────────────────────────────────────
result = rag_agent.get_query_response(
    query="Which NFL team won Super Bowl 50?",
    rag_corpus=knowledge_base_corpus,
    similarity_score_threshold=6.5,
    generative_model=generative_model,
    semantic_similarity_weight=0.8,
    lexical_similarity_weight=0.2,
    cross_encoder_top_k=3,
)
context_str = "\n\n".join([f"{i+1}. {c}" for i, c in enumerate(result["context"])])
print(f"{result['response']}\n\nContext:\n{context_str}")
```

## RAG 2.0 Pipeline Example

Here's what happens internally when you call `rag_agent.get_query_response()`:

```python
result = rag_agent.get_query_response(
    query="What is in front of the Notre Dame Main Building?",
    rag_corpus=knowledge_base_corpus,
    similarity_score_threshold=6.5,
    generative_model=generative_model,
    semantic_similarity_weight=0.8,
    lexical_similarity_weight=0.2,
    cross_encoder_top_k=3,
)
```

**Behind the scenes:**

1. **Query Rewriting** — LLM rewrites the query for better retrieval:
   - `"What is in front of the Notre Dame Main Building?"` → expanded form with synonyms and resolved context

2. **History Check** — Agent searches the history corpus for a semantically similar past query. If the cross-encoder score ≥ `agent_history_similarity_threshold`, the cached response is returned immediately.

3. **Hybrid Retrieval** — If no cache hit, both retrievers run in parallel:
   - FAISS bi-encoder fetches top-100 candidates (semantic)
   - BM25 fetches top-100 candidates (lexical)
   - Scores are min-max normalized and fused: `0.8 × semantic + 0.2 × lexical`

4. **Cross-Encoder Re-ranking** — Top-N hybrid candidates are re-ranked by `ms-marco-MiniLM-L-6-v2` → top-3 passages selected

5. **Query-Aware Summarization** — Each of the 3 passages is individually summarized in the context of the original query

6. **Grounded Generation** — LLM generates a concise answer referencing the summaries with inline `[1]`, `[2]`, `[3]` citations

7. **Citation Verification** — A second LLM call checks every factual claim against the source passages and returns a structured JSON verdict: `{"verdict": "pass", "verified": [...], "unsupported": [...]}`

8. **Logging & History Update** — The interaction is appended to a JSON log file, and the improved query + full response dict are indexed into the history corpus for future reuse. The method always returns a `dict` with keys: `query`, `improved_query`, `response_type` (`"agent_history"` or `"generative_model"`), `response`, `context`, `citation_check_response`, and `agent_history_metadata`.

## 💡 Usage Examples

### 1. Knowledge Base Queries (SQuAD default)
```python
knowledge_base = dataset_util.load_qa_dataset(samples_count=10000)
knowledge_base_corpus.add_update_data_and_index(
    texts=[item["context"] for item in knowledge_base],
    metadatas=[{k: v for k, v in item.items() if k != "context"} for item in knowledge_base],
)

result = rag_agent.get_query_response(
    query="Which NFL team won Super Bowl 50?",
    rag_corpus=knowledge_base_corpus,
    similarity_score_threshold=6.5,
    generative_model=generative_model,
    semantic_similarity_weight=0.8,
    lexical_similarity_weight=0.2,
    cross_encoder_top_k=3,
)
print(result["response"])               # Answer text
print(result["response_type"])          # "generative_model" or "agent_history"
print(result["citation_check_response"])  # {"verdict": "pass", "verified": [...], "unsupported": [...]}
```

### 2. Custom Documents
```python
knowledge_base_corpus.add_update_data_and_index(
    texts=["Notre Dame was founded in 1842...", "The current president is Rev. John Jenkins..."],
    metadatas=[{"source": "wiki"}, {"source": "official"}],
)
result = rag_agent.get_query_response(
    query="Who is the president of Notre Dame?",
    rag_corpus=knowledge_base_corpus,
    similarity_score_threshold=6.5,
    generative_model=generative_model,
    semantic_similarity_weight=0.8,
    lexical_similarity_weight=0.2,
    cross_encoder_top_k=3,
)
print(result["response"])
```

### 3. Query Rewriting Only
```python
improved_query = rag_agent.improve_query("What's the capital of France?", generative_model)
print(improved_query)
# → "Capital city of France"
# (Converts to declarative form, expands abbreviations, adds synonyms for better retrieval)
```

### 4. Citation Checking Only
```python
verdict = rag_agent.check_citation_correctness(
    query="When was Notre Dame founded?",
    response="Notre Dame was founded in 1842 [1].",
    context="Context 1: The University of Notre Dame was established in 1842.",
    generative_model=generative_model,
)
print(verdict)
# → {"verified": [...], "unsupported": [], "verdict": "pass"}
```

### Model Selection

Models are configured as constants in `base/constants.py`:

```python
# Embedding & re-ranking (HuggingFace)
Constants.ModelNames.HuggingFace.SENTENCE_EMBEDDING_MINILM_L6_V2        # "all-MiniLM-L6-v2"
Constants.ModelNames.HuggingFace.CROSS_ENCODER_MS_MARCO_MINILM_L_6_V2  # "cross-encoder/ms-marco-MiniLM-L-6-v2"

# Generative (Gemini)
Constants.ModelNames.Gemini.GEMINI_2_5_PRO    # "gemini-2.5-pro"
Constants.ModelNames.Gemini.GEMINI_2_5_FLASH  # "gemini-2.5-flash"

# Generative (Qwen / local)
Constants.ModelNames.Qwen.QWEN_2_5_1_5B_INSTRUCT  # "Qwen/Qwen2.5-1.5B-Instruct"
Constants.ModelNames.Qwen.QWEN_2_5_3B_INSTRUCT    # "Qwen/Qwen2.5-3B-Instruct"
```

### Environment Variables

Create a `.env` file in the project root:

```env
HF_TOKEN=your_hugging_face_token
GOOGLE_API_KEY=your_google_api_key
```

These are loaded automatically by `config.py` via `python-dotenv`.

### RAG Parameters

Customize chunking in `RAGCorpusManager`:

```python
rag_corpus = RAGCorpusManager(
    sentence_transformer=sentence_transformer,
    max_data_chunk_len=300,   # Maximum words per chunk (default: 300)
    data_chunk_stride=75,     # Overlap between consecutive chunks (default: 75)
)
```

Tune retrieval in `RAGContentRetriever.find_top_similar_items()`:

```python
indices, scores = rag_retriever.find_top_similar_items(
    rag_corpus=corpus,
    query=query,
    initial_retrieval_top_k=100,      # Candidates fetched by bi-encoder and BM25 (default: 100)
    cross_encoder_top_k=5,            # Final passages after cross-encoder re-ranking (default: 5)
    cross_encoder_batch_size=16,      # Batch size for cross-encoder inference (default: 16)
    semantic_similarity_weight=0.8,   # Weight for FAISS bi-encoder score (default: 1.0)
    lexical_similarity_weight=0.2,    # Weight for BM25 score (default: 0.0; BM25 is skipped when 0)
)
```

### Per-Step Generative Model Kwargs

`get_query_response` exposes separate `dict` parameters so you can pass different configs (e.g. a faster/cheaper model config for query rewriting vs. full inference for response generation):

```python
result = rag_agent.get_query_response(
    query=query,
    rag_corpus=knowledge_base_corpus,
    similarity_score_threshold=6.5,
    generative_model=generative_model,
    semantic_similarity_weight=0.8,
    lexical_similarity_weight=0.2,
    cross_encoder_top_k=3,
    improve_query_kwargs_dict={"config": config},
    summarize_context_kwargs_dict={"config": config},
    generate_response_kwargs_dict={"config": config},
    citation_check_kwargs_dict={"config": config},
    rag_retriever_kwargs_dict={"initial_retrieval_top_k": 50},
)
```

### Agent History Threshold

The `similarity_score_threshold` parameter in `get_query_response()` controls when the agent reuses a cached response. The threshold is compared against the raw cross-encoder score:

```python
# Reuse history only for very high-confidence matches
result = rag_agent.get_query_response(
    query=query,
    rag_corpus=knowledge_base_corpus,
    similarity_score_threshold=6.5,  # Tune to balance cache hits vs. freshness
    ...
)
```

Pass `use_agent_history=False` to skip the history check unconditionally:

```python
result = rag_agent.get_query_response(
    query=query,
    rag_corpus=knowledge_base_corpus,
    similarity_score_threshold=6.5,
    use_agent_history=False,   # skip history check entirely
    ...
)
```

## 🧠 How It Works

### 1. RAG 2.0 Pipeline

```
Query
  │
  ▼
Query Rewriting (LLM)
  │
  ▼
History Check (if use_agent_history=True) ──(cache hit)──► Return cached result dict
  │ (miss)
  ▼
Hybrid Retrieval
  ├── FAISS bi-encoder  ─┐
  └── BM25 (if weight>0) ├─► min-max normalize → weighted fusion → top-K candidates
                         ┘
  │
  ▼
Cross-Encoder Re-ranking → top-N passages
  │
  ▼
Query-Aware Context Summarization (per passage)
  │
  ▼
Grounded Generation with Inline Citations [1][2]…
  │
  ▼
Citation Verification → JSON verdict {pass|partial|fail}
  │
  ▼
Log to JSON + Index into History Corpus → return result dict
```

### 2. Four System Prompt Modes

All prompts are defined in `Constants.Instructions.RAGAgent` in `base/constants.py`:

| Mode | Purpose | Output Format |
|---|---|---|
| **QUERY_REWRITER** | Rewrites query for better retrieval (expand, disambiguate) | Plain text |
| **CONTEXT_SUMMARIZER** | Query-aware summary of a retrieved passage | Plain text |
| **RESPONSE_GENERATOR** | Grounded answer with `[N]` inline citations | Plain text |
| **CITATION_CHECKER** | Verifies every claim against source passages | Raw JSON |

### 3. Corpus Management & History

The RAG components (`RAGCorpusManager` and `RAGContentRetriever`) are **corpus-agnostic** and can work with any dataset. The `RagAgent` leverages this by maintaining two separate `RAGCorpusManager` instances:

- **Knowledge Base Corpus**: Your indexed documents (e.g., SQuAD dataset, custom documents, web content)
- **History Corpus**: Indexed past (improved\_query → response) pairs for caching

On each new query, the agent searches the history corpus first; if the cross-encoder score meets the threshold, the cached answer is returned, avoiding redundant retrieval and generation. The same `RAGContentRetriever` performs hybrid search (semantic + lexical) and cross-encoder re-ranking on **both** corpus types.

### 4. BM25 Keyword Retriever

`BM25KeywordRetriever` wraps `rank_bm25.BM25Okapi` with NLTK tokenization and Porter stemming. It is built automatically when documents are added via `RAGCorpusManager.add_update_data_and_index()` and participates in the hybrid score fusion step. When `lexical_similarity_weight=0.0` is passed to `find_top_similar_items`, the BM25 search is skipped entirely for performance.

## 📊 Components

### RagAgent (`agent/rag_agent.py`)
Orchestrates the full RAG 2.0 pipeline.

**Key Methods:**
- `get_query_response(*, query, rag_corpus, ...)` — Main entry point; runs the full pipeline and returns a `dict` with keys: `query`, `improved_query`, `response_type`, `response`, `context`, `citation_check_response`, `agent_history_metadata`
- `improve_query(query, generative_model)` — LLM-powered query rewriting
- `summarize_context(query, context, generative_model)` — Query-aware passage summarization
- `check_citation_correctness(query, response, context, generative_model)` — Citation verification returning a parsed JSON dict
- `retrieve_relevant_context_from_corpus(query, corpus, ...)` — Wraps the retriever with positive-score filtering
- `_summarize_and_build_contexts_string(query, retrieved_context, generative_model, ...)` — Summarizes each passage and formats a numbered context string
- `_add_query_and_response_to_history_corpus(query, metadata)` — Indexes interactions for future reuse
- `_check_agent_history_for_relevant_info(query, threshold)` — Searches history corpus; returns a history dict or `None`
- `_save_responses_and_context_to_json_logs(**kwargs)` — Appends structured log entry to timestamped JSON file

### RAGCorpusManager (`rag/rag_corpus_manager.py`)
Handles document ingestion, chunking, embedding, FAISS indexing, and BM25 indexing.

**Key Features:**
- Sliding-window chunking (configurable `max_data_chunk_len` and `data_chunk_stride`)
- Automatic deduplication via normalized text comparison
- FAISS `IndexFlatIP` (inner product = cosine after L2 normalization) for semantic search
- Integrated `BM25KeywordRetriever` built and updated alongside the FAISS index
- `_clear_corpus()` — Resets all stored documents, chunks, embeddings, and indices

### RAGContentRetriever (`rag/rag_content_retriever.py`)
Performs three-stage retrieval: hybrid scoring → cross-encoder re-ranking → chunk merging.

**Constructor:**
```python
rag_retriever = RAGContentRetriever(cross_encoder)
```

**Retrieval Pipeline:**
1. FAISS bi-encoder search (fast, approximate, semantic)
2. BM25 search (fast, exact keyword matching)
3. Min-max normalization + weighted linear fusion (BM25 step is skipped when `lexical_similarity_weight=0.0`)
4. Cross-encoder re-ranking (precise, pairwise scoring)
5. Overlapping chunk merging for coherent passage reconstruction

### BM25KeywordRetriever (`rag/bm25_keyword_retriever.py`)
Lightweight BM25 wrapper with NLTK tokenization and Porter stemming.

**Key Methods:**
- `build_index(documents)` — Builds `BM25Okapi` index from a list of text strings
- `search(query, top_k)` — Returns `(indices, scores)` for top-k relevant documents

### ModelLoader (`utils/model_loader.py`)
Stateless utility for loading all model types.

**Supported Models:**
- `load_sentence_embedding_model()` — `SentenceTransformer` (bi-encoder)
- `load_hf_cross_encoder()` — `CrossEncoder` (re-ranker)
- `load_hf_tokenizer()` — `AutoTokenizer`
- `load_gemini_generative_model()` — Returns a callable `generate(prompt, system_instructions="", config=...)`. Prepends current date/time to every prompt; overrides the system instruction per-call without mutating the base config.
- `load_hf_generative_model()` — Returns a callable backed by a local Qwen (or other HF causal-LM) model; supports `system_instructions` at load time.

### DataSetUtil (`utils/dataset_utils.py`)
Utility for loading benchmark datasets.

**Key Methods:**
- `load_qa_dataset(dataset_name, samples_count, random_sampling, dataset_split)` — Loads a QA dataset from HuggingFace Hub and returns a list of `{"id", "question", "context", "answers"}` dicts. Defaults to the SQuAD `"train"` split; supports optional shuffle via `random_sampling`.

## 📝 System Prompts

All prompts live in `Constants.Instructions.RAGAgent` (`base/constants.py`) and can be edited directly for customization:

| Constant | Role |
|---|---|
| `QUERY_REWRITER` | Expand, disambiguate, and sharpen the query; output only the rewritten query |
| `CONTEXT_SUMMARIZER` | Summarize retrieved passage relative to the query; no outside knowledge |
| `RESPONSE_GENERATOR` | Answer from context only; cite with `[N]`; say "I don't know" if context is absent |
| `CITATION_CHECKER` | Verify claims against source passages; return raw JSON with `verdict` field |

## 🔮 Future Work

### Fully-Loaded Agentic RAG
The current `RagAgent` follows a fixed pipeline. The next evolution is a **tool-calling agent** that can dynamically select and orchestrate actions based on the query:

- **Multi-Tool Support**: Equip the agent with pluggable tools — RAG knowledge-base lookup, live web search, date/time utilities, calculator, code execution, and corpus management operations (add/remove/reset documents)
- **Dynamic Tool Selection**: The LLM decides at runtime which combination of tools to invoke, rather than always executing a predetermined pipeline
- **Autonomous Operation**: With a richer action space, the agent can plan multi-step operations, execute them sequentially or in parallel, verify outcomes, and adapt its strategy based on intermediate results
- **Corpus Management Tools**: Expose `add_update_data_and_index` and `_clear_corpus` as callable tools so the agent can self-manage its knowledge base mid-session based on user requests or discovered information gaps

### Fine-Grained Corpus Operations
- **Selective Document Deletion**: Currently `_clear_corpus()` resets the entire knowledge base. Implement targeted delete-by-ID operations to remove specific documents or chunks without rebuilding the full FAISS and BM25 indices
- **Incremental Updates**: Add support for updating individual documents in-place, preserving their position in the index while refreshing their content and embeddings
- **Advanced Text Chunking**: The current sliding-window approach chunks by word count, which can split sentences mid-way. Implement semantic-aware chunking strategies that respect sentence and paragraph boundaries while maintaining token-level max length constraints (e.g., using sentence segmentation to create chunks from complete sentences/paragraphs up to a token limit)

### Advanced Query Handling
- **Query Decomposition**: The current RAG agent only performs query _rewriting_ (single-pass reformulation). The next step is teaching the agent to **decompose** complex or multi-part questions into simpler sub-queries, execute each independently, and synthesize results into a coherent answer
- **Adaptive Routing**: The agent should intelligently route queries based on complexity and information needs — direct retrieval for simple factual questions, decomposition for complex multi-part queries, and web search for time-sensitive or out-of-corpus information

## 🤝 Contributing

Contributions are welcome!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Semantic embeddings by [Sentence-Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
- Vector indexing powered by [FAISS](https://github.com/facebookresearch/faiss) (Meta AI)
- Cross-encoder re-ranking via [Sentence-Transformers](https://www.sbert.net/) (`ms-marco-MiniLM-L-6-v2`)
- Lexical retrieval by [rank_bm25](https://github.com/dorianbrown/rank_bm25) with [NLTK](https://www.nltk.org/) tokenization
- LLM inference via [Google Gemini](https://deepmind.google/technologies/gemini/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- All architecture, design decisions, and code are my own. [GitHub Copilot](https://github.com/features/copilot) helped with writing this README, docstrings, and the occasional refactoring.

## 📧 Contact

**Sahand Mosharafian**
- GitHub: [@sahandmsh](https://github.com/sahandmsh)
- Project Link: [https://github.com/sahandmsh/hybrid-rag](https://github.com/sahandmsh/hybrid-rag)

## 🔖 Citation

If you use this project in your research, please cite:

```bibtex
@software{mosharafian2026hybridrag,
  author = {Mosharafian, Sahand},
  title  = {Hybrid RAG: Grounded QA agent with Hybrid Retrieval, Citation Generation, and Automated Verification},
  year   = {2026},
  url    = {https://github.com/sahandmsh/hybrid-rag}
}
```

---

⭐ **Star this repository if you find it helpful!**
