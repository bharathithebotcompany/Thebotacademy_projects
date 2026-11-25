---
title: Semantic RAG
emoji: "🔎"
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.58.0
app_file: app.py
pinned: false
---

# Semantic RAG — Hybrid Retrieval & Evaluation Pipeline

An end-to-end Retrieval-Augmented Generation project combining **SentenceTransformers semantic embeddings, TF-IDF lexical reranking, PyTorch/Hugging Face question answering, reusable caching, intent-sensitive retrieval, batch prediction and EM/F1 evaluation**.

The project is more than a minimal RAG UI: it includes corpus/data loading, chunk preprocessing, reusable embedding caches, hybrid candidate retrieval, answer inference, interactive and batch execution, evaluation tooling, smoke tests, pipeline orchestration and a deployed Streamlit interface on Hugging Face Spaces.

## Engineering Evidence

- **Hybrid retrieval:** semantic embedding search combined with lexical TF-IDF reranking
- **Embedding pipeline:** SentenceTransformers representations with reusable local embedding caches
- **Question answering:** PyTorch/Hugging Face QA model operating on retrieved context
- **Retrieval behaviour:** intent-sensitive retrieval/reranking logic rather than one fixed ranking path
- **Evaluation:** Exact Match (EM) and F1 reporting over validation examples
- **Pipeline tooling:** preprocessing, batch prediction, evaluation and top-level orchestration
- **Reliability checks:** practical end-to-end smoke testing
- **Application layer:** Streamlit UI with Hugging Face Spaces deployment

## Live UI

- Live Streamlit app: https://ebiaraz-semantic-rag.hf.space/
- Hugging Face Space: https://huggingface.co/spaces/EbiAraz/semantic-rag

Run locally:

```powershell
streamlit run src/streamlit_app.py
```

Then open `http://localhost:8501`.

## Retrieval / QA Flow

```text
Hugging Face QA dataset
        |
        v
corpus + questions
        |
        v
chunk preprocessing
        |
        +----> reusable corpus / chunk / embedding caches
        |
        v
semantic embedding retrieval
        |
        +----> lexical TF-IDF reranking
        |
        +----> intent-sensitive ranking behaviour
        |
        v
retrieved context
        |
        v
Hugging Face QA reader
        |
        +----> interactive answer
        +----> batch predictions
        +----> EM / F1 evaluation
```

## What It Does

- Downloads a Hugging Face QA dataset instead of relying only on hand-written documents.
- Builds chunked semantic retrieval over the downloaded corpus.
- Combines embedding search with lexical reranking.
- Uses a tuned Hugging Face question-answering model to answer from retrieved context.
- Caches reusable preprocessing and embeddings for repeatable local runs.
- Supports interactive inference, batch prediction and evaluation.

## Main Files

- `src/data-loader.py` — loads the dataset corpus and batch questions
- `src/inference.py` — hybrid retrieval and answer-generation pipeline
- `src/preprocess.py` — builds reusable corpus, chunk and embedding caches
- `src/main.py` — interactive CLI
- `src/batch-predict.py` — batch prediction runner
- `src/evaluate-model.py` — computes EM and F1 over the validation set
- `src/smoke-test.py` — practical end-to-end checks
- `src/streamlit_app.py` — Streamlit UI implementation
- `app.py` — Hugging Face Spaces and local Streamlit entry point
- `run_pipeline.py` — preprocessing, batch and evaluation orchestration

## Run the Pipeline

Preprocess and cache the corpus:

```powershell
python src/preprocess.py
```

Interactive CLI:

```powershell
python src/main.py
```

Batch prediction:

```powershell
python src/batch-predict.py
```

Evaluation:

```powershell
python src/evaluate-model.py --limit 25
python src/evaluate-model.py --fast
```

Smoke test:

```powershell
python src/smoke-test.py
```

Streamlit UI:

```powershell
streamlit run src/streamlit_app.py
```

Full orchestration:

```powershell
python run_pipeline.py
python run_pipeline.py --fast-evaluate
```

## Outputs & Caching

Preprocessing can create reusable caches including:

- `data/squad_corpus.json`
- `data/squad_questions.json`
- `data/squad_chunks.json`
- `data/squad_chunk_embeddings.npy`

Batch predictions are written to `outputs/batch_predictions.jsonl`, and evaluation reports to `outputs/evaluation_report.json`.

## Hugging Face Spaces

The repository root `app.py` is the Streamlit entry point and `requirements.txt` defines deployment dependencies. Local-only folders and generated artifacts are excluded through `.gitignore` / `.hfignore`.

Recommended settings:

- SDK: `Streamlit`
- App file: `app.py`
- Python: `3.10+`
- CPU Basic can boot the application, although model loading/evaluation will be slower than accelerated hardware
- Persistent storage is optional and useful for retaining model/retrieval caches

## Technology Focus

**RAG • SentenceTransformers • TF-IDF • PyTorch • Hugging Face • Hybrid Retrieval • Semantic Search • Evaluation • Streamlit • Hugging Face Spaces**
