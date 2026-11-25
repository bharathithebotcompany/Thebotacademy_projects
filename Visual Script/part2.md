# BOT ACADEMY — RAG COURSE
# VIDEO GENERATION ACTION SCRIPT — SCRIPTS 11 TO 20

**Production tools:** Claude + Higgsfield + screen recordings  
**Voice source:** Finalized ElevenLabs narration for Scripts 11–20  
**Project:** Enterprise Knowledge Assistant  
**Visual format:** Premium technical education, realistic software demonstrations, precise motion graphics and clear technical diagrams.

---

# 1. GLOBAL PRODUCTION INSTRUCTIONS

These instructions apply to all ten episodes.

## 1.1 Narration synchronization

The finalized ElevenLabs audio is the single source of truth.

- Do not rewrite, shorten, rearrange or paraphrase narration.
- Do not omit any spoken sentence.
- Do not introduce concepts that are not explained in the audio.
- Do not display advanced concepts before the narration introduces them.
- Match every visual transition to the concept being spoken.
- Use the actual audio duration to determine final timestamps.
- Treat any timestamps in this document as visual planning references, not fixed audio timings.
- If the audio contains an example, use that exact example rather than replacing it with a different one.
- If an instruction in this document conflicts with the narration, follow the narration.

## 1.2 Visual identity

Maintain the same visual identity used in Scripts 1–10.

- Dark charcoal or near-black background.
- White typography.
- Cyan or blue for data movement and technical processes.
- Amber for documents and retrieved information.
- Green for verified evidence and successful results.
- Red or amber for errors, unsupported claims and retrieval failures.
- Premium, minimal, high-contrast design.
- Smooth transitions with purposeful motion.
- Readable code and diagrams.

Avoid:
- Generic AI robots.
- Random futuristic holograms.
- Unnecessary particles and decorative effects.
- Overloaded screens.
- Tiny technical labels.
- Repeated title animations.
- Fake terminal outputs or fabricated benchmark results.

## 1.3 Project continuity

Continue using the same fictional **Enterprise Knowledge Assistant**.

Use the same sample company handbook introduced in earlier episodes. It may contain sections such as:

- Annual leave policy.
- Work-from-home policy.
- Travel reimbursement.
- Employee benefits.
- Maternity leave.
- Expense approval procedures.

These are fictional demonstration documents. Do not present the sample policies as real company rules.

Keep the same UI, document naming conventions, project structure, typography and component styling established in Scripts 1–10.

Suggested project modules, where applicable:

- `generation.py`
- `prompt_builder.py`
- `citations.py`
- `retrieval.py`
- `query_expansion.py`
- `query_decomposition.py`
- `query_router.py`
- `query_builder.py`
- `indexing.py`
- `context_builder.py`

Only show files and code that actually exist or are being demonstrated. Do not pretend that an unimplemented feature is already working.

## 1.4 Code demonstration rules

Whenever narration explains implementation:

1. Open the relevant file in VS Code.
2. Show the actual code progressively.
3. Highlight the exact function or line being discussed.
4. Zoom in when an important operation is explained.
5. Show the input and output when the narration discusses them.
6. Run the code only if a real tested implementation is available.
7. Never invent successful execution results.
8. Blur API keys, tokens and credentials.

Use diagrams for conceptual explanations and real screen recordings for actual implementation.

---

# 2. EPISODE-WISE VISUAL PRODUCTION SCRIPT

# SCRIPT 11 — GENERATION, GROUNDING AND CITATIONS

**Learning objective:** Show how retrieved context is passed to the language model, how answers should remain grounded in evidence, and how source citations help users verify responses.

**Main visual idea:** Retrieved evidence becomes an answer, and every important answer claim should be traceable to its supporting source.

## Scene 01 — From retrieval to generation

**Narration reference:** The opening explanation of what happens after relevant chunks are retrieved.

**Visual type:** Animated RAG pipeline.

**Visual execution:**

- Begin with the retrieval result from the previous episode.
- Show three retrieved chunks entering the screen as separate document cards.
- Each card should contain a short fictional handbook passage.
- Add small source labels to the cards.
- Move the cards into a central container labelled `RETRIEVED CONTEXT`.
- Show the user question above the container.
- Connect both the question and retrieved context to the LLM block.
- Animate the LLM processing the combined input.
- Reveal a response card on the right.

**On-screen text:**

`USER QUESTION`

`RETRIEVED CONTEXT`

`LLM`

`GENERATED ANSWER`

**Important:** Do not make it look as though the LLM independently knows the private handbook content. Make the retrieved context visibly enter the generation process.

## Scene 02 — Prompt construction

**Narration reference:** The explanation of instructions, user questions and retrieved context being combined.

**Visual type:** Prompt composition animation and code editor.

**Visual execution:**

- Show three separate blocks:
  1. System instructions.
  2. User question.
  3. Retrieved document context.
- Animate these blocks joining into one structured prompt.
- Open `generation.py` or the actual prompt-building file.
- Show the prompt template progressively.
- Highlight the portions corresponding to instructions, question and context as the narration explains them.
- Show the final prompt being passed to the model.
- Keep the text readable; do not display a wall of code.

**On-screen text:**

`SYSTEM INSTRUCTIONS`

`USER QUESTION`

`RETRIEVED CONTEXT`

`PROMPT CONSTRUCTION`

Only display prompt fields that are actually covered in the narration.

## Scene 03 — Grounded answers

**Narration reference:** The explanation of generating answers using retrieved information rather than unsupported assumptions.

**Visual type:** Side-by-side comparison.

**Visual execution:**

- Show a question about annual leave.
- On the left, show a generic answer that makes a claim without visible evidence.
- On the right, show an answer generated from the fictional handbook passage.
- Highlight the exact sentence in the source passage supporting the answer.
- Draw a line from the source sentence to the corresponding answer claim.
- Show the unsupported answer with an amber warning.
- Show the evidence-supported answer with a green verification indicator.

**On-screen text:**

`UNSUPPORTED CLAIM`

`RETRIEVED EVIDENCE`

`GROUNDED ANSWER`

Do not imply that RAG guarantees factual correctness. The visual should communicate that grounding improves traceability when relevant evidence is retrieved and used correctly.

## Scene 04 — Source citations

**Narration reference:** The explanation of showing where an answer came from.

**Visual type:** Product UI demonstration.

**Visual execution:**

- Display the generated answer in the Enterprise Knowledge Assistant interface.
- Add a citation chip beside the relevant answer statement.
- Show metadata such as:
  - Source filename.
  - Page number.
  - Section name.
- If the application supports it, click the citation chip.
- Open the corresponding source document and highlight the supporting passage.
- If this interaction is not implemented, show it as a clearly labelled design mock-up rather than a functional product recording.

**On-screen text:**

`SOURCE DOCUMENT`

`PAGE NUMBER`

`SUPPORTING PASSAGE`

`VERIFY THE ANSWER`

## Scene 05 — Missing evidence and fallback

**Narration reference:** The explanation of what should happen when the retrieved documents do not contain an answer.

**Visual type:** Live application demonstration or controlled mock-up.

**Visual execution:**

- Ask a question that is deliberately absent from the fictional handbook.
- Show the actual retrieval result.
- If no relevant evidence is retrieved, show an insufficient-evidence state.
- Display the actual tested fallback response if the application has one.
- Do not fabricate a successful answer.
- End by showing the complete generation flow with the citation stage highlighted.

**On-screen text:**

`INSUFFICIENT EVIDENCE`

`DO NOT INVENT AN ANSWER`

**Transition:** Move from the complete grounded-answer workflow into the next episode's problem: even a RAG system can fail.

---

# SCRIPT 12 — NAIVE RAG PITFALLS

**Learning objective:** Explain common failure points in a basic RAG system and show why retrieval quality, document processing and context selection matter.

**Main visual idea:** A RAG pipeline that appears to work but produces a poor answer because one or more stages fail.

## Scene 01 — A RAG system can still fail

**Narration reference:** The opening problem or example showing that having RAG does not automatically guarantee a correct answer.

**Visual type:** Failure demonstration.

**Visual execution:**

- Show the Enterprise Knowledge Assistant interface.
- Enter a realistic question about a company policy.
- Show a generated response.
- Highlight one incorrect or unsupported part of the answer.
- Pull back to reveal the RAG pipeline.
- Highlight the stages where problems can occur.

**On-screen text:**

`RAG DOES NOT GUARANTEE CORRECT ANSWERS`

`WHERE DID IT FAIL?`

Use only an example consistent with the narration.

## Scene 02 — Document ingestion and extraction problems

**Narration reference:** Any explanation of poor extraction, missing text or document-processing errors.

**Visual type:** Before-and-after document demonstration.

**Visual execution:**

- Show a sample document with a heading, paragraph and table.
- Show an incorrect extraction result where important structure or table relationships are lost.
- Highlight the missing or distorted information.
- Show a correctly extracted version beside it, if available.
- If OCR is discussed, show a scanned document entering OCR and the extracted text appearing.
- Make it clear that OCR is relevant to scanned/image-based content, not a universal requirement for every PDF.

**On-screen text:**

`DOCUMENT QUALITY`

`EXTRACTION ERROR`

`MISSING INFORMATION`

Only animate the failure types actually mentioned in the audio.

## Scene 03 — Chunking problems

**Narration reference:** The explanation of poor chunk boundaries or chunks losing important context.

**Visual type:** Chunk comparison animation.

**Visual execution:**

- Show a handbook section containing a policy heading and its explanation.
- Split the text at an inappropriate location.
- Show the heading in one chunk and its explanation in another.
- Highlight how the relationship between the two pieces becomes unclear.
- Compare it with a better chunk boundary that keeps the related information together.
- Reuse the same chunk visual language from the earlier chunking episode.

**On-screen text:**

`POOR CHUNK BOUNDARY`

`CONTEXT LOST`

`BETTER CHUNKING`

Do not suggest that one chunk size or overlap setting is always optimal.

## Scene 04 — Retrieval problems

**Narration reference:** The explanation of irrelevant or incomplete retrieved chunks.

**Visual type:** Search-result comparison.

**Visual execution:**

- Display a user question.
- Show a ranked list of retrieved chunks.
- Highlight irrelevant results.
- Show the relevant chunk appearing too low in the list or missing, depending on the narrated example.
- Display the difference between the retrieved content and the information actually required.
- If the narration discusses keyword mismatch or semantic mismatch, show only the corresponding example.

**On-screen text:**

`IRRELEVANT RESULTS`

`MISSING EVIDENCE`

`RETRIEVAL QUALITY`

## Scene 05 — Context and generation problems

**Narration reference:** The explanation of too much context, missing context or generation using unsupported information.

**Visual type:** Context-window animation.

**Visual execution:**

- Show several retrieved chunks entering the context container.
- Mark relevant chunks and irrelevant chunks distinctly.
- Show excessive or duplicate content competing for attention.
- Show the final prompt being constructed.
- If the narration discusses context overload, visually reduce the available context space without inventing a specific token limit.
- Show the generated answer and highlight the unsupported claim if the example includes one.

**On-screen text:**

`RELEVANT CONTEXT`

`NOISY CONTEXT`

`UNSUPPORTED ANSWER`

## Scene 06 — Locate the failure stage

**Narration reference:** The concluding explanation that RAG failures must be diagnosed rather than treated as one generic problem.

**Visual type:** Interactive-looking pipeline diagnosis.

**Visual execution:**

- Display the full pipeline:
  `INGESTION → CHUNKING → EMBEDDING → RETRIEVAL → CONTEXT → GENERATION`
- Animate a warning travelling through the pipeline.
- Stop at the stage associated with the narrated example.
- Show that each stage needs separate inspection.
- Transition toward the advanced techniques that aim to improve query understanding and retrieval.

**On-screen text:**

`DEBUG THE ACTUAL FAILURE`

`DO NOT GUESS`

---

# SCRIPT 13 — HyDE / QUERY EXPANSION

**Learning objective:** Explain how query transformation can help retrieval when a user's original wording does not closely match the wording in the documents.

**Main visual idea:** A short or vague user query is transformed into a more retrieval-friendly representation.

## Scene 01 — The query mismatch problem

**Narration reference:** The opening explanation of a user asking a question differently from how the document expresses the answer.

**Visual type:** Split-screen text comparison.

**Visual execution:**

- Show a user asking a short question.
- Show the corresponding handbook passage using different terminology.
- Highlight the wording mismatch.
- Place the two texts side by side.
- Animate the mismatch between the question and document passage.
- Make the retrieval challenge visually clear without suggesting that the information itself is absent.

**On-screen text:**

`USER QUERY`

`DOCUMENT WORDING`

`WORDING MISMATCH`

## Scene 02 — Query expansion

**Narration reference:** The explanation of adding related terms or alternative expressions to a query.

**Visual type:** Query transformation animation.

**Visual execution:**

- Show the original user query in a single search bar.
- Duplicate it into a transformation panel.
- Reveal related terms or alternative phrasings only when the narration introduces them.
- Show the expanded query representation.
- Send the transformed query into the retrieval stage.
- Display the retrieved document passage if the narration provides one.

**On-screen text:**

`ORIGINAL QUERY`

`EXPANDED QUERY`

`RETRIEVAL`

Do not confuse query expansion with generating a final answer.

## Scene 03 — HyDE concept

**Narration reference:** The explanation of Hypothetical Document Embeddings.

**Visual type:** Step-by-step conceptual animation.

**Visual execution:**

- Display the original user question.
- Move it into a block labelled `HYPOTHETICAL ANSWER GENERATION`.
- Show a hypothetical passage being generated as an intermediate retrieval aid.
- Clearly label the passage `HYPOTHETICAL DOCUMENT`.
- Pass the hypothetical document through the embedding stage.
- Show its embedding being used to search the document collection.
- Retrieve actual document chunks from the vector database.
- Highlight that the retrieved source documents—not the hypothetical passage—are the evidence used for the final answer.

**On-screen text:**

`USER QUERY`

`HYPOTHETICAL DOCUMENT`

`EMBEDDING`

`RETRIEVE REAL DOCUMENTS`

**Technical accuracy requirement:** Never visually present the hypothetical document as an authentic source, verified fact or actual company policy. It is an intermediate retrieval aid.

## Scene 04 — HyDE versus ordinary retrieval

**Narration reference:** Any comparison between the original query and transformed retrieval process.

**Visual type:** Side-by-side comparison.

**Visual execution:**

- Left panel: original query goes directly to retrieval.
- Right panel: query is transformed into a hypothetical document representation before retrieval.
- Show candidate documents emerging from each path.
- Use illustrative document cards, not fabricated performance scores.
- If the narration does not claim one method always performs better, do not use a universal winner indicator.

**On-screen text:**

`DIRECT QUERY`

`HYDE-ASSISTED RETRIEVAL`

`RETRIEVED DOCUMENTS`

## Scene 05 — Practical implementation or use case

**Narration reference:** Any narrated code example or practical use case.

**Visual type:** VS Code or conceptual workflow.

**Visual execution:**

- Open the actual query transformation module if one exists.
- Highlight the function that generates the hypothetical document or expanded query.
- Show the transformed text only if it is a real output from the demonstration.
- If the implementation is not available, use a labelled conceptual example rather than fake execution output.

**Transition:** The transformed query idea leads into the next episode: what happens when one query is expanded into several different searches?

---

# SCRIPT 14 — MULTI-QUERY RETRIEVAL

**Learning objective:** Explain how one user question can produce multiple query variations, allowing retrieval to explore different relevant expressions.

**Main visual idea:** One user query branches into several searches, and their results are consolidated.

## Scene 01 — One question, multiple interpretations

**Narration reference:** The opening problem explaining why one search formulation may miss relevant information.

**Visual type:** Query branching animation.

**Visual execution:**

- Show one user question in the centre.
- Animate three branches emerging from it.
- Each branch represents a different query formulation.
- Keep the original user intent visible above the branches.
- Use different wording in each query, but preserve the same underlying intent.

**On-screen text:**

`ORIGINAL QUESTION`

`QUERY 1`

`QUERY 2`

`QUERY 3`

Do not invent a different user intent for each query.

## Scene 02 — Generating query variations

**Narration reference:** The explanation of using an LLM or another method to produce multiple query formulations.

**Visual type:** Prompt and output animation.

**Visual execution:**

- Show the original question entering a query-generation component.
- Display a prompt requesting alternative search formulations, if the narration discusses prompting.
- Reveal the query variations one by one.
- Keep each query in a separate card.
- Highlight that all variations are intended to search for the same underlying information.

**On-screen text:**

`QUERY GENERATION`

`ALTERNATIVE SEARCH FORMULATIONS`

## Scene 03 — Parallel retrieval

**Narration reference:** The explanation of searching with multiple generated queries.

**Visual type:** Animated parallel retrieval diagram.

**Visual execution:**

- Send each query card toward the same retrieval system.
- Animate the searches running in parallel.
- Show each query returning its own ranked document list.
- Use the same fictional handbook document cards.
- Allow the same source document to appear in more than one result list.
- Highlight duplicate results without removing them prematurely.

**On-screen text:**

`PARALLEL SEARCH`

`RESULT SET 1`

`RESULT SET 2`

`RESULT SET 3`

## Scene 04 — Combining retrieved results

**Narration reference:** The explanation of consolidating results from multiple searches.

**Visual type:** Result-merging animation.

**Visual execution:**

- Bring the separate result lists into one central collection.
- Highlight duplicate chunks or repeated source documents.
- If deduplication is discussed, show duplicate entries being consolidated.
- Keep unique relevant chunks.
- Show the resulting candidate set moving forward to the next retrieval stage.
- Do not show RRF or ranking fusion unless the narration introduces it; that is the next episode.

**On-screen text:**

`MERGED RESULTS`

`DUPLICATE HANDLING`

`RETRIEVAL CANDIDATES`

## Scene 05 — Practical comparison

**Narration reference:** Any example comparing a single query with multiple queries.

**Visual type:** Before-and-after comparison.

**Visual execution:**

- Left: one query returns a limited set of candidate chunks.
- Right: multiple query formulations return different candidate chunks.
- Show how the combined results can cover additional relevant wording.
- Do not fabricate numerical recall improvements.
- If the narration contains actual outputs, reproduce those outputs exactly.

**On-screen text:**

`SINGLE QUERY`

`MULTI-QUERY RETRIEVAL`

`BROADER SEARCH COVERAGE`

**Transition:** Multiple searches create multiple ranked lists. The next episode explains how rankings from different lists can be combined.

---

# SCRIPT 15 — RAG FUSION / RECIPROCAL RANK FUSION

**Learning objective:** Explain how multiple query result lists can be combined using ranking information, with Reciprocal Rank Fusion as the central technique.

**Main visual idea:** Multiple ranked result lists become one consolidated ranking.

## Scene 01 — The multiple-ranking problem

**Narration reference:** The opening explanation of having several retrieval lists and needing to combine them.

**Visual type:** Ranking comparison.

**Visual execution:**

- Show three ranked result lists side by side.
- Use consistent document IDs across lists.
- Some documents should appear in more than one list.
- Make their positions different in each list.
- Highlight the difficulty of combining these lists by simply copying them together.

**On-screen text:**

`RANKED LIST 1`

`RANKED LIST 2`

`RANKED LIST 3`

`HOW DO WE COMBINE THEM?`

Use illustrative rankings only. Do not label them as benchmark results.

## Scene 02 — Reciprocal Rank Fusion concept

**Narration reference:** The explanation of RRF and how a document's position in multiple ranked lists contributes to its combined score.

**Visual type:** Animated ranking calculation.

**Visual execution:**

- Select one document that appears in multiple result lists.
- Highlight its rank position in each list.
- Move the rank positions into a central scoring panel.
- Show the RRF concept using the formula only if it is included in the narration:

  `RRF(d) = Σ 1 / (k + rankᵢ(d))`

- Explain visually that contributions from multiple ranked lists are accumulated.
- Show the final combined ordering.
- Keep the formula large and readable.
- Do not introduce unexplained mathematical symbols.

**On-screen text:**

`RECIPROCAL RANK FUSION`

`RANK CONTRIBUTION`

`COMBINED SCORE`

## Scene 03 — Merging the result lists

**Narration reference:** The practical explanation of combining the rankings.

**Visual type:** Motion graphic.

**Visual execution:**

- Bring the three ranked lists into a central fusion block.
- Animate each document receiving contributions from the lists in which it appears.
- Show the combined ranking emerging on the right.
- Highlight a document that was ranked highly across multiple lists.
- Show a document with weaker combined support moving lower.
- Do not imply that RRF evaluates the semantic correctness of the document itself; it combines ranking signals.

**On-screen text:**

`MULTIPLE RANKINGS`

`RRF`

`FUSED RANKING`

## Scene 04 — Why ranking fusion matters

**Narration reference:** The explanation of why combining lists is useful.

**Visual type:** Before-and-after comparison.

**Visual execution:**

- Left: separate ranked lists with different orderings.
- Right: one fused list.
- Highlight the consolidation of results.
- Show the final candidate list moving into the next retrieval stage.
- If the narration mentions reranking, distinguish it visually from RRF: RRF combines rankings, while a reranker can subsequently score query-document relevance.

**On-screen text:**

`RANK FUSION`

`ONE CONSOLIDATED LIST`

Do not merge RRF and reranking into one indistinguishable operation.

## Scene 05 — Implementation view

**Narration reference:** Any actual implementation explanation.

**Visual type:** Code editor.

**Visual execution:**

- Open the actual fusion or retrieval module.
- Highlight where ranked lists are received.
- Highlight the RRF calculation or library call only if present.
- Show the final ranked output only from a real execution.
- Keep document IDs consistent with the animation.

**Transition:** The next episode moves from generating multiple searches to breaking one complex question into smaller questions.

---

# SCRIPT 16 — QUERY DECOMPOSITION

**Learning objective:** Explain how a complex question can be split into smaller sub-questions, retrieved separately and combined into a final response.

**Main visual idea:** One complex question becomes several manageable questions, each contributing evidence to the final answer.

## Scene 01 — A complex question

**Narration reference:** The opening example of a question that requires multiple pieces of information.

**Visual type:** Realistic user interface.

**Visual execution:**

- Show a user asking a multi-part question in the Enterprise Knowledge Assistant.
- Use the exact example from the narration.
- Highlight the different information requirements within the question.
- Keep the full original question visible.
- Animate separate highlights around each requirement.

**On-screen text:**

`COMPLEX USER QUESTION`

`MULTIPLE INFORMATION NEEDS`

## Scene 02 — Breaking the question down

**Narration reference:** The explanation of decomposition.

**Visual type:** Query decomposition animation.

**Visual execution:**

- Move the original question into a central block.
- Split it into smaller query cards.
- Number the cards in the order used by the narration.
- Each sub-question should represent one information requirement.
- Draw arrows from the original question to the corresponding sub-questions.
- Preserve the relationship between the original question and the sub-questions.

**On-screen text:**

`ORIGINAL QUESTION`

`SUB-QUESTION 1`

`SUB-QUESTION 2`

`SUB-QUESTION 3`

Only show as many sub-questions as the narration actually uses.

## Scene 03 — Retrieving evidence for each sub-question

**Narration reference:** The explanation of retrieving information separately for the smaller questions.

**Visual type:** Parallel retrieval animation.

**Visual execution:**

- Send each sub-question into the retrieval system.
- Show separate retrieved document chunks for each.
- Use the same handbook source documents.
- Label each result set with the sub-question it answers.
- Highlight relevant passages.
- If one sub-question has no evidence, show that honestly rather than inventing a source.

**On-screen text:**

`SUB-QUESTION 1 → EVIDENCE`

`SUB-QUESTION 2 → EVIDENCE`

`SUB-QUESTION 3 → EVIDENCE`

## Scene 04 — Combining the evidence

**Narration reference:** The explanation of bringing the sub-question results together.

**Visual type:** Context assembly animation.

**Visual execution:**

- Bring all retrieved evidence cards into a central context container.
- Keep their source labels visible.
- Show the original question above the combined context.
- Animate the context moving to the generation stage.
- Reveal the final answer only after the narration reaches the generation step.
- If the narration discusses synthesis, visually show the answer integrating the different evidence pieces.

**On-screen text:**

`COMBINED EVIDENCE`

`ORIGINAL QUESTION`

`FINAL RESPONSE`

## Scene 05 — Why decomposition helps

**Narration reference:** The concluding explanation of complex questions becoming easier to retrieve and answer.

**Visual type:** Before-and-after comparison.

**Visual execution:**

- Left: one complex question sent directly to retrieval.
- Right: the same question broken into smaller sub-questions.
- Show the separate evidence paths on the right.
- Bring the final evidence together.
- Avoid claiming that decomposition always improves every query.

**On-screen text:**

`ONE COMPLEX QUERY`

`MULTIPLE SUB-QUERIES`

`EVIDENCE-BASED SYNTHESIS`

**Transition:** Decomposition breaks a question into smaller parts. The next technique takes a different approach: first understand the broader idea behind the question.

---

# SCRIPT 17 — STEP-BACK PROMPTING

**Learning objective:** Explain how a system can move from a specific question to a broader conceptual question before retrieving information for the original question.

**Main visual idea:** Move one level above the specific question, retrieve broader context, then return to the original question.

## Scene 01 — A narrow question

**Narration reference:** The opening example of a specific question that may benefit from broader context.

**Visual type:** User query interface.

**Visual execution:**

- Show the exact question used in the narration.
- Highlight the specific details in the question.
- Show the related broader topic or concept as a separate visual layer.
- Keep the distinction between the original question and the broader concept clear.

**On-screen text:**

`SPECIFIC QUESTION`

`BROADER CONCEPT`

## Scene 02 — Stepping back

**Narration reference:** The explanation of converting a specific question into a broader conceptual question.

**Visual type:** Zoom-out concept animation.

**Visual execution:**

- Begin with the original question in a focused card.
- Slowly zoom out to reveal the broader topic surrounding it.
- Display the step-back question separately.
- Draw a clear arrow from the original question to the broader question.
- Do not replace the original question permanently.

**On-screen text:**

`ORIGINAL QUESTION`

`STEP-BACK QUESTION`

`BROADER CONTEXT`

## Scene 03 — Retrieving broader information

**Narration reference:** The explanation of retrieving information using the broader question.

**Visual type:** Retrieval animation.

**Visual execution:**

- Send the step-back question into the retrieval system.
- Show relevant broader-context chunks being retrieved.
- Display their source metadata.
- Keep the retrieved passages visually separate from the original question.
- If the narration shows both broad and direct retrieval, display them as separate paths.

**On-screen text:**

`BROADER RETRIEVAL`

`RELEVANT CONTEXT`

## Scene 04 — Returning to the original question

**Narration reference:** The explanation of using broader context to answer the specific question.

**Visual type:** Context-to-answer animation.

**Visual execution:**

- Bring the broader retrieved context back to the original question.
- Place the original question at the top.
- Place the retrieved evidence below it.
- Send both into the generation stage.
- Reveal the answer using the supporting context.
- If the narration mentions limitations, show that broader context alone may not contain the exact answer.

**On-screen text:**

`BROADER CONTEXT`

`ORIGINAL QUESTION`

`GROUNDED RESPONSE`

## Scene 05 — Step-back versus decomposition

**Narration reference:** Only if the narration explicitly compares these approaches.

**Visual type:** Two-column conceptual comparison.

**Visual execution:**

- Left: query decomposition splits one question into multiple smaller questions.
- Right: step-back prompting transforms a specific question into a broader conceptual question.
- Use arrows and labels to distinguish their purpose.
- Do not add this comparison if it is absent from the narration.

**On-screen text:**

`QUERY DECOMPOSITION`

`STEP-BACK PROMPTING`

**Transition:** The next episode explores another decision: not every query should follow the same retrieval path.

---

# SCRIPT 18 — ROUTING

**Learning objective:** Explain how a RAG system can choose an appropriate retrieval path or data source based on the user's query.

**Main visual idea:** A query enters a decision point and is directed toward the appropriate route.

## Scene 01 — Different questions need different sources

**Narration reference:** The opening explanation that different types of questions may require different information sources or retrieval methods.

**Visual type:** Multi-source overview.

**Visual execution:**

- Show three example questions, using the examples from the narration.
- Place different source cards around them.
- Sources may include:
  - Employee handbook.
  - Technical documentation.
  - Structured company database.
- Keep the sources consistent with the narrated example.
- Show that a single retrieval path may not be suitable for every query.

**On-screen text:**

`USER QUERY`

`MULTIPLE KNOWLEDGE SOURCES`

## Scene 02 — Router decision

**Narration reference:** The explanation of routing a query to an appropriate path.

**Visual type:** Decision-flow animation.

**Visual execution:**

- Move one user query into a central block labelled `QUERY ROUTER`.
- Show the router analysing the query.
- Animate a decision branch.
- Direct the query to the relevant source or retrieval path.
- Keep the other paths visible but inactive.
- Show the selected route with a clear cyan highlight.

**On-screen text:**

`QUERY ROUTER`

`ROUTE SELECTION`

`SELECTED PATH`

## Scene 03 — Different retrieval paths

**Narration reference:** The explanation of the different paths or tools available.

**Visual type:** Split-screen architecture.

**Visual execution:**

- Display the selected paths as separate lanes.
- For a document-based question, show the vector retrieval lane.
- For a structured-data question, show the database/query lane only if the narration covers it.
- For a different knowledge source, show the corresponding route only if it appears in the narration.
- Animate the query entering the correct path.
- Show the result returning to the common answer-generation stage.

**On-screen text:**

Use only the routes present in the narration, for example:

`DOCUMENT RETRIEVAL`

`STRUCTURED QUERY`

`SPECIALIZED TOOL`

## Scene 04 — Result integration

**Narration reference:** The explanation of what happens after the selected route returns information.

**Visual type:** Pipeline animation.

**Visual execution:**

- Show the selected route returning its result.
- Move the result into a common context or response stage if that is part of the narrated workflow.
- Display source metadata where applicable.
- Reveal the answer only at the point the narration explains generation.
- Keep the route-selection stage distinct from retrieval and generation.

**On-screen text:**

`ROUTED RESULT`

`CONTEXT`

`RESPONSE`

## Scene 05 — Routing decision example

**Narration reference:** The practical example or code explanation.

**Visual type:** Application or code demonstration.

**Visual execution:**

- Show the exact example query from the narration.
- Display the router's actual decision if the implementation is available.
- Open the actual routing function in VS Code.
- Highlight the classification or routing logic.
- If an LLM makes the routing decision, show the actual structured output only if it has been tested.
- Never fabricate router confidence values or execution logs.

**Transition:** Routing selects the path. The next episode focuses on constructing a more structured query for the selected retrieval system.

---

# SCRIPT 19 — QUERY CONSTRUCTION

**Learning objective:** Explain how natural-language questions can be transformed into structured search queries or filters for more precise retrieval.

**Main visual idea:** A natural-language request becomes a structured query with fields, filters and conditions.

## Scene 01 — Natural language versus structured data

**Narration reference:** The opening explanation of a user asking a question that requires structured filtering.

**Visual type:** Split-screen comparison.

**Visual execution:**

- Show the exact natural-language question from the narration.
- On the left, display the question as typed by the user.
- On the right, display a structured data representation.
- Highlight the information that must be extracted from the question.
- Use only the fields and conditions actually discussed in the narration.

**On-screen text:**

`NATURAL-LANGUAGE QUERY`

`STRUCTURED QUERY`

## Scene 02 — Extracting query conditions

**Narration reference:** The explanation of identifying entities, fields, filters or conditions.

**Visual type:** Text annotation animation.

**Visual execution:**

- Display the original question.
- Highlight relevant entities, dates, categories or conditions only if they appear in the example.
- Move each highlighted element into a structured field card.
- Show how the original question becomes a set of query parameters.
- Keep the original wording visible for comparison.

**On-screen text:**

`ENTITY`

`FIELD`

`FILTER`

`CONDITION`

Only use labels that match the narration.

## Scene 03 — Structured query generation

**Narration reference:** The explanation of converting the extracted information into a structured query.

**Visual type:** Code and data demonstration.

**Visual execution:**

- Open the actual query construction module.
- Highlight the input natural-language query.
- Show the structured output format being built.
- If the narration discusses metadata filters, show a simple filter representation.
- If it discusses SQL or another query language, show only the actual syntax being taught.
- Do not mix SQL, vector-store filters and metadata expressions as if they were interchangeable.

**On-screen text:**

`QUERY CONSTRUCTION`

`STRUCTURED OUTPUT`

## Scene 04 — Applying the query

**Narration reference:** The explanation of using the constructed query to retrieve relevant records or documents.

**Visual type:** Database or vector-store screen recording.

**Visual execution:**

- Show the constructed query entering the relevant retrieval component.
- Highlight the fields and conditions being applied.
- Display the returned records or chunks from an actual test.
- Show how filtering narrows the candidate set.
- If the application does not yet implement this function, use a conceptual diagram and label it clearly.

**On-screen text:**

`APPLY FILTERS`

`SEARCH RESULTS`

`RELEVANT RECORDS`

## Scene 05 — Precision and validation

**Narration reference:** The explanation of why structured query construction matters or any limitations discussed.

**Visual type:** Before-and-after comparison.

**Visual execution:**

- Left: broad retrieval without the structured condition.
- Right: retrieval with the intended condition.
- Highlight the difference in returned records.
- If the narration discusses invalid filters or schema errors, show a validation failure and its correction.
- Do not claim that structured filtering alone guarantees relevance.

**On-screen text:**

`BROAD SEARCH`

`STRUCTURED FILTERING`

`VALIDATED QUERY`

**Transition:** A query can be structured more effectively, but document representation also affects what the retriever can find. This leads into multi-representation indexing.

---

# SCRIPT 20 — MULTI-REPRESENTATION INDEXING

**Learning objective:** Explain how a document can be represented in multiple forms for retrieval, rather than relying on only one representation.

**Main visual idea:** One source document produces multiple retrieval representations, which help the system locate relevant information.

## Scene 01 — One document, different representations

**Narration reference:** The opening explanation of why a single document representation may not be enough for every retrieval need.

**Visual type:** Document transformation animation.

**Visual execution:**

- Show one fictional handbook document.
- Display its original structure:
  - Title.
  - Sections.
  - Paragraphs.
  - Tables, if relevant to the narration.
- Animate the document into separate representation cards.
- Use only the representations covered by the audio.
- Keep the original document visible as the common source.

**On-screen text:**

`SOURCE DOCUMENT`

`MULTIPLE REPRESENTATIONS`

## Scene 02 — Creating representations

**Narration reference:** The explanation of generating alternative representations from the source document.

**Visual type:** Transformation diagram.

**Visual execution:**

- Show the original document entering an indexing pipeline.
- Create separate output cards for the representation types explained in the narration.
- Possible examples, only if explicitly covered:
  - Original text chunks.
  - Summaries.
  - Parent sections.
  - Child chunks.
  - Structured metadata.
- Label each representation clearly.
- Use arrows to show that each representation originates from the same source document.

**On-screen text:**

Use only the actual representation types discussed in the audio.

`SOURCE`

`REPRESENTATION`

`INDEX`

## Scene 03 — Indexing the representations

**Narration reference:** The explanation of storing or indexing multiple representations for retrieval.

**Visual type:** Vector database and metadata diagram.

**Visual execution:**

- Show the different representation cards moving toward the indexing stage.
- Display their corresponding IDs and source relationships.
- If embeddings are discussed, show each eligible representation being converted into an embedding.
- Show the resulting records entering the vector database.
- Keep source document references visible so that retrieved representations can be traced back to their source.
- Do not imply that every representation must always be embedded separately; follow the specific narrated architecture.

**On-screen text:**

`INDEXING`

`REPRESENTATION ID`

`SOURCE REFERENCE`

`VECTOR DATABASE`

## Scene 04 — Retrieval using different representations

**Narration reference:** The explanation of how different representations can help retrieve relevant information.

**Visual type:** Query-to-representation animation.

**Visual execution:**

- Show the user query entering the retrieval system.
- Display the relevant representation being matched or retrieved.
- If the narration explains parent-child retrieval, show a small child chunk linking back to its larger parent section.
- If the narration explains summaries or other representations, display those exact relationships.
- Show the system locating the original source content where appropriate.
- Keep the distinction between a retrieval representation and the final source evidence clear.

**On-screen text:**

`USER QUERY`

`RETRIEVED REPRESENTATION`

`SOURCE CONTENT`

## Scene 05 — Returning useful context

**Narration reference:** The explanation of using the retrieved representation to provide useful context for generation.

**Visual type:** Context assembly animation.

**Visual execution:**

- Show the retrieved representation.
- Follow its source reference to the original document or source section.
- Bring the relevant original content into the context container if the narrated method requires it.
- Move the context toward the generation stage.
- Show the final answer only if the narration reaches that point.
- Keep source provenance visible.

**On-screen text:**

`RETRIEVAL`

`SOURCE MAPPING`

`CONTEXT ASSEMBLY`

## Scene 06 — Final concept recap

**Narration reference:** The concluding explanation of multi-representation indexing.

**Visual type:** Clean architecture recap.

**Visual execution:**

- Display the source document on the left.
- Show the representation-generation stage in the centre.
- Show indexed representations on the right.
- Animate a user query entering the retrieval system.
- Highlight the path from the retrieved representation back to its source.
- End with the same visual language used in earlier RAG episodes.

**On-screen text:**

`ONE SOURCE`

`MULTIPLE REPRESENTATIONS`

`BETTER RETRIEVAL OPTIONS`

Do not claim that multi-representation indexing automatically improves every retrieval task. The visual should show the design principle, not promise a universal performance result.

---

# 3. MASTER SCREEN-RECORDING CHECKLIST

Claude should create a recording checklist for the practical portions of these ten episodes.

Use actual application recordings wherever the narration requires implementation.

| Asset ID | Episode | Recording requirement |
|---|---|---|
| SR-21 | 11 | Prompt construction in the actual generation module |
| SR-22 | 11 | Generated answer with source citation |
| SR-23 | 11 | Source document verification, if implemented |
| SR-24 | 11 | Insufficient-evidence example, if implemented |
| SR-25 | 12 | Poor extraction versus correct extraction, if discussed |
| SR-26 | 12 | Poor chunk boundary versus improved chunk boundary |
| SR-27 | 12 | Retrieval failure example |
| SR-28 | 13 | Original query and transformed query |
| SR-29 | 13 | HyDE hypothetical document and retrieval flow |
| SR-30 | 14 | Multiple query variations |
| SR-31 | 14 | Separate retrieval result lists |
| SR-32 | 15 | Ranked result lists and RRF combination |
| SR-33 | 15 | Actual fusion code or output, if implemented |
| SR-34 | 16 | Original complex query and decomposed sub-questions |
| SR-35 | 16 | Separate evidence retrieval for sub-questions |
| SR-36 | 17 | Original question and step-back question |
| SR-37 | 18 | Router decision and selected retrieval path |
| SR-38 | 18 | Actual routing implementation, if available |
| SR-39 | 19 | Natural-language query and structured query |
| SR-40 | 19 | Actual metadata filter or query execution |
| SR-41 | 20 | Source document and its representations |
| SR-42 | 20 | Indexing and source-reference mapping |

**Recording rule:** Do not record a simulated output and present it as actual execution. If the feature is not implemented, create a conceptual animation and label it as a conceptual example.

---

# 4. MASTER ANIMATION AND DIAGRAM ASSET LIST

Create these diagrams using consistent design language.

| Diagram ID | Episode | Diagram | Main teaching purpose |
|---|---|---|---|
| DG-27 | 11 | Grounded generation | Show retrieved context entering generation |
| DG-28 | 11 | Citation and evidence mapping | Connect answer claims to source passages |
| DG-29 | 12 | RAG failure map | Show possible failure points across the pipeline |
| DG-30 | 12 | Chunking and retrieval failure | Show how poor input affects retrieval |
| DG-31 | 13 | Query expansion | Show original and expanded query |
| DG-32 | 13 | HyDE workflow | Show hypothetical document used for retrieval |
| DG-33 | 14 | Multi-query branching | Show one query becoming multiple searches |
| DG-34 | 14 | Parallel retrieval | Show separate result lists |
| DG-35 | 15 | Reciprocal Rank Fusion | Show ranking contributions being combined |
| DG-36 | 16 | Query decomposition | Show one complex query becoming sub-questions |
| DG-37 | 16 | Evidence synthesis | Show separate evidence being combined |
| DG-38 | 17 | Step-back prompting | Show specific query becoming broader query |
| DG-39 | 18 | Query routing | Show router selecting a path |
| DG-40 | 19 | Query construction | Show natural language becoming structured filters |
| DG-41 | 20 | Multi-representation indexing | Show one source becoming multiple representations |
| DG-42 | 20 | Source mapping | Show retrieved representations linking back to original content |

---

# 5. HIGGSFIELD / MOTION GRAPHIC PROMPTS

Use these prompts to create supporting animations. Keep all labels in English and preserve the dark visual identity of the course.

## DG-27 — Grounded generation

"Create a premium technical educational animation in 16:9. Show a user question and three retrieved document chunks entering a prompt assembly component. The combined context moves into a language model block. A generated answer appears on the right. Draw clear links between the retrieved evidence and the corresponding answer claims. Use amber for source documents, cyan for data movement, green for supported claims and restrained amber warnings for unsupported claims. Keep the architecture technically accurate. Do not imply that RAG guarantees factual correctness."

## DG-28 — Citation and evidence mapping

"Create a clean 16:9 educational motion graphic. Show a generated answer with three separate claims. Beneath it, show retrieved source passages with filename, page and section metadata. Draw a visible connection from each supported claim to its exact source passage. Mark one unsupported claim with an amber warning. Use readable English labels: ANSWER CLAIM, SOURCE PASSAGE, PAGE, CITATION, UNSUPPORTED. Do not imply citations are functional links unless the actual application implements them."

## DG-29 — RAG failure map

"Create a technically accurate RAG pipeline diagram in a premium dark theme. Display DOCUMENT INGESTION, EXTRACTION, CHUNKING, EMBEDDINGS, RETRIEVAL, CONTEXT ASSEMBLY and GENERATION. Show separate warning indicators at different stages to communicate that failures can originate at different points. Do not show every stage failing simultaneously. Use amber for warnings and red only for an actual failure. Keep labels readable."

## DG-31 — Query expansion

"Create a clean educational animation showing one original user query branching into multiple related search formulations. Keep all query variations aligned to the same user intent. Show the variations entering a retrieval component. Use clear arrows and readable English labels: ORIGINAL QUERY, EXPANDED QUERY, RETRIEVAL. Do not add unrelated questions."

## DG-32 — HyDE workflow

"Create a technically accurate 16:9 animation of Hypothetical Document Embeddings. Show USER QUERY entering a hypothetical document generation step. A clearly labelled HYPOTHETICAL DOCUMENT is produced and passed into an embedding model. Its representation is used to search a vector database containing REAL SOURCE DOCUMENTS. Retrieved real documents are then passed toward context assembly. Make it visually unmistakable that the hypothetical document is not a real source or verified evidence."

## DG-33 — Multi-query branching

"Create a premium dark-theme motion graphic showing one user question branching into three alternative search queries. Preserve the same underlying intent across all branches. Each query enters a separate retrieval lane and returns its own ranked document list. Use consistent document IDs so duplicates can be recognized. Use readable labels: ORIGINAL QUERY, QUERY 1, QUERY 2, QUERY 3, RESULT LIST."

## DG-35 — Reciprocal Rank Fusion

"Create a clean technical animation with three ranked result lists displayed side by side. Use consistent document IDs but different positions in each list. Select one document and highlight its rank contribution from each list. Move the contributions into a central RECIPROCAL RANK FUSION block. Show one combined ranking emerging on the right. If displaying the formula, use RRF(d) = sum of 1/(k + rank). Do not fabricate benchmark scores or imply that RRF itself evaluates semantic relevance."

## DG-36 — Query decomposition

"Create a technically accurate animation showing one complex user question splitting into three smaller sub-questions. Send each sub-question into a separate retrieval lane. Show different source passages returning for each sub-question. Bring the evidence into one context assembly component and connect it to the original question. Use labels: ORIGINAL QUESTION, SUB-QUESTION, RETRIEVED EVIDENCE, FINAL SYNTHESIS."

## DG-38 — Step-back prompting

"Create a premium educational motion graphic. Start with a specific user question in the foreground. Zoom out to reveal a broader conceptual question connected to it. Send the broader question into retrieval and show relevant context returning. Then reconnect the broader context to the original specific question. Keep the two questions visibly distinct. Use labels: SPECIFIC QUESTION, STEP-BACK QUESTION, BROADER CONTEXT, ORIGINAL QUESTION."

## DG-39 — Query routing

"Create a technically accurate dark-theme architecture animation. A user query enters a QUERY ROUTER block. The router directs it to one of several distinct retrieval paths, such as document retrieval or structured data retrieval, only if those paths are part of the narrated lesson. Highlight the selected route and show the result returning to a common response stage. Do not animate every route as active at the same time."

## DG-40 — Query construction

"Create a clean technical educational animation showing a natural-language question being converted into a structured query. Highlight relevant entities, fields and filter conditions in the original question. Move each element into a structured representation. Show the structured query entering a retrieval system and returning filtered results. Do not mix SQL syntax with vector database filter syntax."

## DG-41 — Multi-representation indexing

"Create a premium technical animation showing one source document being transformed into multiple retrieval representations. Display only the representation types required by the narration. Show each representation being indexed while preserving its relationship to the original source. Then show a user query retrieving one representation and tracing it back to the source content. Use readable labels and technically accurate data flow. Do not suggest that all representations must always be embedded separately."

---

# 6. FINAL CLAUDE EXECUTION INSTRUCTIONS

Before producing the final video plan:

1. Inspect all ten finalized narration files for Scripts 11–20.
2. Identify the exact narration sequence and the concepts introduced in each script.
3. Use the narration—not this storyboard—as the final authority.
4. Preserve the original episode numbering and titles.
5. Map every spoken explanation to a corresponding visual.
6. Break each episode into individual shots based on the actual audio.
7. Use real screen recordings for implementation demonstrations.
8. Use diagrams for abstract concepts.
9. Use Higgsfield only for supporting motion graphics where appropriate.
10. Maintain the same Enterprise Knowledge Assistant project throughout.
11. Maintain continuity with the visuals already established in Scripts 1–10.
12. Do not introduce concepts from Scripts 21–30 early.
13. Do not add quizzes unless the supplied narration contains them.
14. Do not add extra spoken explanations or subtitles that alter the narration.
15. Do not invent terminal output, benchmark scores, retrieval results or application functionality.
16. Verify all code and technical diagrams before final production.
17. Use actual audio duration for final timestamps.
18. Keep all important text readable on a standard 16:9 video screen.

## Required output from Claude

For each of Scripts 11–20, return:

- Episode identifier and exact title.
- Actual audio duration.
- Learning objective.
- Complete shot-by-shot visual storyboard.
- Exact narration reference for each shot.
- Visual type.
- Detailed screen content.
- Exact editor instructions.
- On-screen text.
- Animation and transition instructions.
- Required screen recordings.
- Required diagrams or generated assets.
- Any implementation dependencies.
- Technical accuracy checks.

**Final quality requirement:** A video editor should be able to understand exactly what to display, what to animate, what to record, what to highlight and when to transition without having to guess what the narration means.

The final output must feel like a continuation of Scripts 1–10—not a separate course, a different project or a disconnected set of animations.