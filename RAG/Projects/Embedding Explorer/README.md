# RAG from Scratch

Five Jupyter notebooks that build a retrieval pipeline layer by layer — chunking, embeddings, a
vector index, BM25 keyword search, and a hybrid retriever that merges both — with no retrieval
framework involved. Every index is hand-written so you can see exactly what a vector DB and a BM25
scorer actually do.

All five notebooks index the same sample document, `report.md`.

Notebooks are numbered in teaching order and are self-contained — each one re-declares its own
client and helper functions, so you can open any single notebook and run it top to bottom.

## Setup

1. Install dependencies:
   ```bash
   pip install voyageai python-dotenv jupyter
   ```
2. Add your API key to `.env`:
   ```
   VOYAGE_API_KEY=your-key-here
   ```
   See `VoyageAI_API_Key_Directions.pdf` for how to get one.
3. Launch Jupyter, or open a notebook directly in VS Code:
   ```bash
   jupyter lab
   ```

## Notebooks

- **01_rag_chunking.ipynb** — Three chunking strategies: fixed-size by character (with overlap), by
  sentence, and by markdown `##` section. No API key needed. Section chunking is what every later
  notebook uses.
- **02_rag_embeddings.ipynb** — Generating embeddings with VoyageAI (`voyage-3-large`) and the
  `input_type` query/document distinction.
- **03_rag_vectordb.ipynb** — A from-scratch `VectorIndex` with cosine distance. Chunk → embed →
  index → search for the nearest chunks to a user question.
- **04_rag_bm25.ipynb** — A from-scratch `BM25Index` for keyword search, which beats embeddings on
  exact identifiers like `INC-2023-Q4-011`. No API key needed.
- **05_rag_hybrid.ipynb** — A `Retriever` that fans a query out to both the vector and BM25 indexes
  and merges the rankings, getting semantic and keyword matching in one.

## Supporting files

| Path | What it is |
| --- | --- |
| `report.md` | The source document all five notebooks chunk and index |
| `VoyageAI_API_Key_Directions.pdf` | How to get the `VOYAGE_API_KEY` |

## Notes

- These notebooks call VoyageAI only — there are no Claude calls in the retrieval pipeline itself.
  Generation on top of the retrieved chunks is the natural next step, and isn't covered here.
- Run `04_rag_bm25` and `05_rag_hybrid` back to back on the query `"What happened with
  INC-2023-Q4-011?"` — that's the clearest demonstration of why hybrid retrieval exists.
- `03` and `05` embed all chunks in a single bulk call rather than one at a time, to stay under
  VoyageAI's rate limits.
