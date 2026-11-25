# BOT ACADEMY — RAG COURSE
# VIDEO GENERATION ACTION SCRIPT — SCRIPTS 21 TO 30

**Production tools:** Claude + Higgsfield + actual screen recordings  
**Voice source:** Finalized ElevenLabs narration for Scripts 21–30  
**Flagship project:** Enterprise Knowledge Assistant  
**Production style:** Premium technical education, realistic software demonstrations, precise technical diagrams and purposeful motion graphics.

---

# 1. GLOBAL PRODUCTION INSTRUCTIONS

These instructions apply to all ten episodes.

## 1.1 Follow the finalized narration exactly

The ElevenLabs audio is the single source of truth.

- Do not rewrite, shorten, rearrange or paraphrase narration.
- Do not remove any spoken sentence.
- Do not add explanations that are absent from the audio.
- Do not introduce concepts before they are mentioned.
- Every visual must correspond to the exact concept being discussed.
- Use actual audio duration to determine final scene timestamps.
- If an example is included in the narration, use that example.
- If a code demonstration is included, use the actual project implementation.
- Do not add quizzes unless the audio contains a quiz.
- Do not create visuals that imply functionality that the project does not have.

## 1.2 Maintain the established visual identity

Continue the visual style used in Scripts 1–20.

- Dark charcoal or near-black background.
- White typography.
- Cyan/blue for data flow and technical operations.
- Amber for documents and retrieved information.
- Green for verified results and successful operations.
- Red/amber for errors and warnings.
- Clean technical diagrams.
- Smooth transitions.
- Readable code.
- Restrained 2D and 3D motion graphics.

Avoid generic AI robots, random holograms, excessive particles, decorative effects and overloaded screens.

## 1.3 Maintain one project throughout

Continue using the same **Enterprise Knowledge Assistant**.

The application should remain consistent across all ten episodes.

Suggested project structure, subject to the actual repository:

```text
Enterprise-Knowledge-Assistant/
│
├── backend/
│   └── app/
│       ├── services/
│       │   ├── ingestion.py
│       │   ├── parsing.py
│       │   ├── chunking.py
│       │   ├── embeddings.py
│       │   ├── retrieval.py
│       │   ├── reranking.py
│       │   ├── generation.py
│       │   ├── citations.py
│       │   └── evaluation.py
│       │
│       ├── api/
│       └── main.py
│
├── evaluation/
│   ├── dataset.json
│   └── evaluate.py
│
├── frontend/
│
├── tests/
│
├── Dockerfile
└── README.md
```

Do not create or display files that do not exist in the actual implementation. Adapt this structure to the tested repository.

## 1.4 Practical demonstration rules

For every code demonstration:

1. Open the actual file in VS Code.
2. Show the code progressively.
3. Highlight the exact function being discussed.
4. Zoom in on important operations.
5. Show the actual input and output.
6. Run the implementation only when it has been tested.
7. Never fabricate output, evaluation scores or performance metrics.
8. Blur API keys, tokens and sensitive information.

If a feature is not implemented, use a conceptual diagram and clearly distinguish it from a working demonstration.

---

# 2. EPISODE-WISE VISUAL PRODUCTION SCRIPT

# SCRIPT 21 — RAPTOR: HIERARCHICAL RETRIEVAL

**Learning objective:** Explain how RAPTOR organizes information into hierarchical levels, allowing retrieval from both detailed chunks and higher-level summaries.

**Main visual idea:** Many small document chunks are organized into a hierarchy of increasingly broader summaries.

## Scene 01 — The limitation of flat retrieval

**Narration reference:** The opening explanation of why retrieving individual chunks may not always provide the broader context required.

**Visual type:** Conceptual comparison.

**Visual execution:**

- Show a large fictional employee handbook.
- Split it into multiple small chunks.
- Display all chunks in one flat horizontal collection.
- Show a user asking a question that requires understanding information across multiple sections.
- Highlight the difficulty of relying only on isolated chunks.
- Keep the original chunks visible.

**On-screen text:**

`FLAT CHUNK RETRIEVAL`

`LOCAL INFORMATION`

`BROADER CONTEXT`

Do not suggest that ordinary chunk retrieval is always inadequate. Show the specific limitation being discussed in the narration.

## Scene 02 — Creating a hierarchy

**Narration reference:** The explanation of grouping chunks and creating higher-level representations.

**Visual type:** Hierarchical architecture animation.

**Visual execution:**

- Start with multiple small chunk cards arranged in a row.
- Group related chunks together.
- Move each group into a summarization stage if summarization is covered in the audio.
- Generate a higher-level summary card above each group.
- Repeat the grouping process at a higher level only if the narration describes multiple levels.
- Arrange the result as a tree structure.

**On-screen text:**

`CHUNKS`

`GROUPING`

`SUMMARIZATION`

`HIGHER-LEVEL REPRESENTATION`

Use the exact hierarchy terminology from the narration.

## Scene 03 — RAPTOR tree visualization

**Narration reference:** The explanation of the hierarchical tree structure.

**Visual type:** Animated tree diagram.

**Visual execution:**

- Display the hierarchy vertically.
- Bottom level: original document chunks.
- Middle level: grouped summaries.
- Top level: broader summary or topic representation.
- Draw connections between parent and child nodes.
- Animate the tree from bottom to top as the hierarchy is created.
- Use consistent colors to distinguish original chunks from summaries.
- Keep all labels readable.

**On-screen text:**

`LOWER LEVEL`

`PARENT NODE`

`HIGHER LEVEL`

`RAPTOR TREE`

Do not make the tree appear to be a conventional folder hierarchy. It represents relationships between source chunks and higher-level representations.

## Scene 04 — Retrieving from different levels

**Narration reference:** The explanation of retrieving information from different levels of the hierarchy.

**Visual type:** Query-to-tree animation.

**Visual execution:**

- Show a user question entering the retrieval system.
- Animate the query moving toward the hierarchy.
- Highlight a relevant higher-level node if the query needs broad context.
- Highlight a lower-level chunk if the query needs detailed information.
- Show the selected representation being returned.
- If the narration explains how the original source chunks are recovered, animate the path from the parent representation to its child chunks.

**On-screen text:**

`USER QUERY`

`HIERARCHICAL RETRIEVAL`

`RELEVANT LEVEL`

## Scene 05 — RAPTOR versus flat retrieval

**Narration reference:** Any comparison between traditional chunk retrieval and hierarchical retrieval.

**Visual type:** Split-screen comparison.

**Visual execution:**

- Left: flat list of independent chunks.
- Right: hierarchical tree with chunks and summaries.
- Send the same query to both sides.
- Show the type of information each approach retrieves.
- Use the actual narrated example.
- Do not invent retrieval accuracy percentages or benchmark scores.

**On-screen text:**

`FLAT RETRIEVAL`

`HIERARCHICAL RETRIEVAL`

**Transition:** Move from hierarchical representations to a different retrieval technique that focuses on fine-grained token-level matching.

---

# SCRIPT 22 — COLBERT: LATE INTERACTION

**Learning objective:** Explain how ColBERT uses contextual token-level representations and late interaction to compare queries and documents.

**Main visual idea:** Instead of representing an entire document with only one vector, show multiple token-level representations being compared.

## Scene 01 — Single-vector retrieval limitation

**Narration reference:** The opening explanation of document representation and why finer-grained matching can be useful.

**Visual type:** Comparison animation.

**Visual execution:**

- Show a document paragraph.
- Transform the paragraph into one abstract vector representation.
- Show a user query becoming another vector.
- Highlight that the entire document is represented in a compressed form.
- Transition into a more detailed token-level representation.
- Keep the comparison conceptual and technically accurate.

**On-screen text:**

`DOCUMENT REPRESENTATION`

`SINGLE VECTOR`

`FINE-GRAINED MATCHING`

Do not suggest that all embedding models use only one vector internally. The visual should represent the retrieval architecture being discussed.

## Scene 02 — Token-level representations

**Narration reference:** The explanation of representing individual tokens or token-level contextual embeddings.

**Visual type:** Token visualization.

**Visual execution:**

- Display a short document sentence.
- Split it into visible tokens.
- Pass the sentence through a contextual representation stage if discussed.
- Show each token producing a separate abstract vector representation.
- Repeat the process for the user query.
- Use separate colors for query tokens and document tokens.
- Do not assign human meanings to individual vector dimensions.

**On-screen text:**

`QUERY TOKENS`

`DOCUMENT TOKENS`

`TOKEN REPRESENTATIONS`

## Scene 03 — Late interaction

**Narration reference:** The explanation of comparing query and document representations during the interaction stage.

**Visual type:** Token matching animation.

**Visual execution:**

- Place query token representations on the left.
- Place document token representations on the right.
- Draw matching connections between query and document token representations.
- Animate the strongest matching document token for each query token if the narration explains MaxSim.
- Show the token-level matching contributions being aggregated into a document relevance score.
- Keep the mathematical explanation synchronized with the narration.

**On-screen text:**

`TOKEN-LEVEL INTERACTION`

`MATCHING`

`AGGREGATED RELEVANCE`

If MaxSim is discussed, display the formula only when the narration introduces it. Do not introduce the term independently.

## Scene 04 — ColBERT retrieval workflow

**Narration reference:** The explanation of how query and document representations are used for retrieval.

**Visual type:** Architecture animation.

**Visual execution:**

- Show documents entering the indexing stage.
- Display their token-level representations being stored or indexed according to the narrated architecture.
- Show a query entering the retrieval process.
- Animate token-level interaction.
- Reveal the ranked document results.
- Keep indexing and query-time interaction as separate stages.

**On-screen text:**

`DOCUMENT INDEXING`

`QUERY ENCODING`

`LATE INTERACTION`

`RANKED RESULTS`

## Scene 05 — Comparison with single-vector retrieval

**Narration reference:** Any narrated comparison of ColBERT and conventional dense retrieval.

**Visual type:** Side-by-side comparison.

**Visual execution:**

- Left: one query vector compared with one document vector.
- Right: multiple query-token and document-token representations interacting.
- Highlight the difference in granularity.
- Do not claim ColBERT always outperforms every dense retrieval model.
- Use the same document and query in both panels.

**Transition:** Move from improving relevance through token-level matching to a system that evaluates and corrects retrieval results.

---

# SCRIPT 23 — CRAG: CORRECTIVE RAG

**Learning objective:** Explain how Corrective RAG evaluates retrieved information and responds when the retrieved evidence is insufficient or unreliable.

**Main visual idea:** Retrieved documents pass through an evaluation stage before being used for answer generation.

## Scene 01 — Retrieval is not always reliable

**Narration reference:** The opening explanation of receiving irrelevant, incomplete or unreliable retrieved documents.

**Visual type:** Retrieval failure demonstration.

**Visual execution:**

- Show a user asking a question about a fictional company policy.
- Display the retrieved document chunks.
- Highlight one relevant passage.
- Highlight one irrelevant passage.
- Show one incomplete passage.
- Place the results inside a retrieval assessment area.
- Do not mark documents as incorrect unless the narration's example establishes that.

**On-screen text:**

`RETRIEVED DOCUMENTS`

`RELEVANCE CHECK`

`INSUFFICIENT EVIDENCE`

## Scene 02 — Evaluating retrieved information

**Narration reference:** The explanation of evaluating the relevance or quality of retrieved documents.

**Visual type:** Decision-stage animation.

**Visual execution:**

- Move the retrieved chunks into a central evaluator block.
- Show each document being assessed.
- Display the actual categories or labels used in the narration.
- If the narration discusses relevance grading, show the relevant/irrelevant distinction.
- Separate the evaluator from the language model generation stage.
- Keep the process understandable and uncluttered.

**On-screen text:**

`RETRIEVED CONTEXT`

`EVALUATION`

`RELEVANT`

`IRRELEVANT`

Only use the categories actually explained in the audio.

## Scene 03 — Corrective action

**Narration reference:** The explanation of what happens after retrieval quality is evaluated.

**Visual type:** Branching workflow animation.

**Visual execution:**

- Show the evaluator producing a decision.
- Animate the relevant result toward the context assembly stage.
- If the retrieved evidence is insufficient, show the correction path described in the narration.
- This may involve query refinement, another retrieval attempt or an external knowledge source only if that behavior is explicitly covered.
- Keep the correction path visually distinct from the normal path.
- Do not show every possible correction method if the audio covers only one.

**On-screen text:**

`RELEVANT EVIDENCE`

`CORRECTIVE ACTION`

`RE-RETRIEVAL`

Use only the exact correction stages included in the narration.

## Scene 04 — Corrected retrieval

**Narration reference:** The explanation of retrieving improved evidence after corrective processing.

**Visual type:** Before-and-after retrieval comparison.

**Visual execution:**

- Left: initial retrieval list containing irrelevant or incomplete chunks.
- Right: corrected retrieval result.
- Highlight the difference in retrieved evidence.
- Show the corrected evidence entering context assembly.
- Keep the source documents visible.
- Do not fabricate a better numerical score.

**On-screen text:**

`INITIAL RETRIEVAL`

`CORRECTED RETRIEVAL`

`EVIDENCE REVIEW`

## Scene 05 — CRAG workflow recap

**Narration reference:** The concluding explanation of Corrective RAG.

**Visual type:** Architecture recap.

**Visual execution:**

- Show:
  `USER QUERY → RETRIEVAL → EVALUATION → CORRECTION → CONTEXT → GENERATION`
- Animate the normal and corrective paths separately.
- Highlight the evaluator as the central decision point.
- End with a clean diagram that can be reused in the course recap.

**Transition:** CRAG responds to retrieval quality. The next episode explores how a RAG system can dynamically choose how much retrieval or processing a query needs.

---

# SCRIPT 24 — ADAPTIVE RAG

**Learning objective:** Explain how a RAG system can adapt its retrieval or processing strategy according to the complexity and requirements of a query.

**Main visual idea:** Different questions take different paths through the RAG system instead of using one fixed workflow for every query.

## Scene 01 — One pipeline is not always ideal

**Narration reference:** The opening explanation of why every query may not need the same retrieval strategy.

**Visual type:** Query comparison.

**Visual execution:**

- Display three queries with different complexity levels.
- Use the exact examples from the narration.
- Show a simple question, a question requiring retrieval and a more complex question only if these categories appear in the audio.
- Place all three queries beside a conventional fixed pipeline.
- Highlight the inefficiency of treating every query identically, where that is the narrated point.

**On-screen text:**

`SIMPLE QUERY`

`COMPLEX QUERY`

`FIXED RETRIEVAL PATH`

## Scene 02 — Adaptive decision stage

**Narration reference:** The explanation of deciding which processing strategy to use.

**Visual type:** Decision-flow animation.

**Visual execution:**

- Move each query into a central decision component.
- Show the decision component assessing the query.
- Animate different branches emerging.
- Use only the strategies mentioned in the narration.
- Highlight the selected route for each query.
- Keep the query's original intent visible.

**On-screen text:**

`QUERY ANALYSIS`

`ADAPTIVE DECISION`

`SELECTED STRATEGY`

## Scene 03 — Different processing paths

**Narration reference:** The explanation of the possible retrieval or generation paths.

**Visual type:** Multi-lane architecture animation.

**Visual execution:**

- Create separate lanes for the strategies explained in the audio.
- A simple query may take a direct path if the narration describes it.
- A retrieval-required query may take a standard RAG path.
- A complex query may take an advanced retrieval path if explained.
- Animate each query through its selected route.
- Do not show all paths executing for every query.

**On-screen text:**

Use only the relevant labels from the narration, such as:

`DIRECT RESPONSE`

`STANDARD RETRIEVAL`

`ADVANCED RETRIEVAL`

## Scene 04 — Adaptive retrieval example

**Narration reference:** The practical example or code explanation.

**Visual type:** Application or code demonstration.

**Visual execution:**

- Show the exact query used in the narration.
- Display the selected strategy.
- Open the actual routing or adaptive retrieval module.
- Highlight the decision logic.
- Show the real output if the code is implemented.
- Do not invent confidence scores or classification labels.
- If the implementation is conceptual, label it as a conceptual flow.

**On-screen text:**

`QUERY`

`STRATEGY SELECTION`

`EXECUTION`

## Scene 05 — Why adaptivity matters

**Narration reference:** The conclusion describing the purpose or trade-offs of Adaptive RAG.

**Visual type:** Architecture comparison.

**Visual execution:**

- Left: every query follows the same fixed retrieval path.
- Right: queries take different paths based on their needs.
- Highlight the adaptive decision component.
- If the narration discusses trade-offs, show a restrained balance between answer quality, latency and processing cost.
- Do not imply adaptive retrieval is automatically faster or more accurate in every situation.

**On-screen text:**

`FIXED WORKFLOW`

`ADAPTIVE WORKFLOW`

`QUERY-DEPENDENT PROCESSING`

**Transition:** The next episode looks at another retrieval improvement: reducing redundant results while preserving useful diversity.

---

# SCRIPT 25 — MMR: MAXIMAL MARGINAL RELEVANCE

**Learning objective:** Explain how MMR balances query relevance and diversity when selecting retrieval results.

**Main visual idea:** A search result list contains many similar chunks. MMR selects useful results while reducing unnecessary repetition.

## Scene 01 — The redundancy problem

**Narration reference:** The opening explanation of retrieving multiple similar or repetitive chunks.

**Visual type:** Search result visualization.

**Visual execution:**

- Show a user asking a question.
- Display a ranked list of retrieved chunks.
- Highlight that several chunks contain almost the same information.
- Show that another useful topic or supporting passage is missing from the selected results.
- Keep the repeated chunks visibly similar.

**On-screen text:**

`RETRIEVED RESULTS`

`DUPLICATE INFORMATION`

`LOW DIVERSITY`

## Scene 02 — Relevance versus diversity

**Narration reference:** The explanation of the two factors MMR considers.

**Visual type:** Two-axis conceptual graphic.

**Visual execution:**

- Show one axis labelled `QUERY RELEVANCE`.
- Show another axis or visual dimension labelled `DIVERSITY`.
- Place document cards in a conceptual selection space.
- Highlight one card that is highly relevant but very similar to an already selected result.
- Highlight another card that is relevant and adds different information.
- Keep the visualization conceptual rather than presenting invented numerical values.

**On-screen text:**

`RELEVANCE`

`DIVERSITY`

`BALANCED SELECTION`

## Scene 03 — MMR selection process

**Narration reference:** The explanation of selecting results using Maximal Marginal Relevance.

**Visual type:** Step-by-step retrieval animation.

**Visual execution:**

- Display the candidate result list.
- Select the first relevant result.
- For the next selection, compare candidate relevance with similarity to already selected results.
- Highlight a candidate that adds useful new information.
- Move it into the selected results area.
- Repeat only as many selection steps as the narration explains.
- If the narration introduces the formula, show it at that moment:

  `MMR = λ × Relevance − (1 − λ) × Redundancy`

- Explain visually that the balance depends on the relevance/diversity weighting parameter.

**On-screen text:**

`CANDIDATE RESULTS`

`SELECTED RESULTS`

`MMR`

Do not invent a value for λ or present one setting as universally optimal.

## Scene 04 — Similarity and diversity comparison

**Narration reference:** The explanation of how MMR reduces repetitive results.

**Visual type:** Before-and-after comparison.

**Visual execution:**

- Left: top results contain multiple similar passages.
- Right: selected results include relevant but less redundant information.
- Use the same source collection on both sides.
- Highlight the additional information captured in the diverse selection.
- Keep the comparison focused on selection behavior.

**On-screen text:**

`WITHOUT DIVERSITY CONTROL`

`MMR SELECTION`

`LESS REDUNDANCY`

## Scene 05 — Practical application

**Narration reference:** The practical use case or code explanation.

**Visual type:** Code editor or conceptual workflow.

**Visual execution:**

- Open the actual retrieval selection module if implemented.
- Highlight the candidate scoring or selection function.
- Show actual selected chunks from the test query.
- If the implementation is unavailable, show the MMR selection concept with illustrative cards.
- Do not present illustrative scores as real retrieval output.

**Transition:** MMR improves the diversity of selected evidence. The next episode explores questions that require information from multiple connected sources.

---

# SCRIPT 26 — MULTI-HOP RETRIEVAL

**Learning objective:** Explain how answering a complex question may require retrieving information through multiple connected retrieval steps.

**Main visual idea:** The first retrieved result provides information needed to formulate the next retrieval step.

## Scene 01 — A question requiring multiple pieces of information

**Narration reference:** The opening example of a question that cannot be answered from one isolated passage.

**Visual type:** User query demonstration.

**Visual execution:**

- Show the exact multi-part question from the narration.
- Highlight the separate information requirements.
- Show the relevant fictional handbook or company documents.
- Make it visually clear that the answer depends on connecting information from more than one source or passage.

**On-screen text:**

`COMPLEX QUESTION`

`MULTIPLE EVIDENCE SOURCES`

## Scene 02 — First retrieval hop

**Narration reference:** The explanation of retrieving the first piece of information.

**Visual type:** Retrieval animation.

**Visual execution:**

- Send the original query into the retrieval system.
- Show the first relevant document chunk being retrieved.
- Highlight the information obtained from it.
- Show how this information creates a new search requirement.
- Keep the original question visible in a small panel.

**On-screen text:**

`ORIGINAL QUERY`

`HOP 1`

`FIRST EVIDENCE`

## Scene 03 — Second retrieval hop

**Narration reference:** The explanation of using the first result to retrieve another piece of information.

**Visual type:** Sequential retrieval animation.

**Visual execution:**

- Take the relevant information from the first retrieved passage.
- Transform it into the next retrieval query only if the narration describes this.
- Send the new query into the retrieval system.
- Show the second supporting passage being retrieved.
- Connect the second passage to the first with a visible relationship arrow.
- If additional hops are explained, repeat the same visual pattern.

**On-screen text:**

`HOP 2`

`FOLLOW-UP QUERY`

`CONNECTED EVIDENCE`

## Scene 04 — Connecting the evidence

**Narration reference:** The explanation of combining information from multiple retrieval steps.

**Visual type:** Evidence relationship diagram.

**Visual execution:**

- Display the first and second retrieved passages.
- Highlight the relevant facts in each.
- Draw a relationship line showing how they contribute to the original question.
- Bring the evidence into one context container.
- Keep source references visible.
- Do not invent a logical connection that the source passages do not support.

**On-screen text:**

`EVIDENCE 1`

`EVIDENCE 2`

`CONNECTED INFORMATION`

## Scene 05 — Final answer synthesis

**Narration reference:** The explanation of generating the answer from the connected evidence.

**Visual type:** Context and generation animation.

**Visual execution:**

- Display the original question above the combined evidence.
- Move both into the generation stage.
- Reveal the final answer when the narration reaches it.
- Connect the answer's claims to the appropriate source passages if citations are part of the example.
- Show the full multi-hop path in a compact recap.

**On-screen text:**

`MULTI-HOP RETRIEVAL`

`EVIDENCE CHAIN`

`FINAL ANSWER`

**Transition:** The next episode introduces a system that can evaluate its own retrieval and generation process through reflection.

---

# SCRIPT 27 — SELF-RAG AND REFLECTION

**Learning objective:** Explain how Self-RAG uses reflection or critique signals to assess retrieval and generated responses.

**Main visual idea:** The system does not simply retrieve and generate. It evaluates whether retrieval is needed and whether the generated answer is supported.

## Scene 01 — The limitation of always retrieving

**Narration reference:** The opening explanation of why retrieving documents for every question may not always be necessary or useful.

**Visual type:** Query comparison.

**Visual execution:**

- Display two different questions.
- Use the exact examples from the narration.
- Show one question that requires external document evidence.
- Show another that may not require the same retrieval process, if the narration uses that distinction.
- Highlight the difference in retrieval requirements.

**On-screen text:**

`RETRIEVAL REQUIRED?`

`QUERY ASSESSMENT`

Do not imply that the system can safely answer every question without retrieval.

## Scene 02 — Retrieval decision

**Narration reference:** The explanation of deciding whether retrieval should be performed.

**Visual type:** Decision-flow diagram.

**Visual execution:**

- Move the user query into a decision component.
- Display the retrieval decision stage.
- Animate the selected path.
- If retrieval is required, move the query toward the document collection.
- If the narration includes a no-retrieval path, show that separately.
- Keep the original question visible.

**On-screen text:**

`RETRIEVAL DECISION`

`RETRIEVE`

`GENERATE`

Use the exact decision labels from the audio.

## Scene 03 — Retrieved evidence assessment

**Narration reference:** The explanation of checking whether retrieved passages are relevant or useful.

**Visual type:** Evidence evaluation animation.

**Visual execution:**

- Display the retrieved document chunks.
- Show an evaluation stage examining their relevance.
- Highlight the supporting passage.
- Mark irrelevant or insufficient content appropriately.
- If the narration explains critique tokens or reflection signals, introduce those labels only at this point.
- Do not invent the exact token vocabulary if it is not specified in the audio.

**On-screen text:**

`RETRIEVED EVIDENCE`

`RELEVANCE CHECK`

`CRITIQUE`

## Scene 04 — Answer generation and reflection

**Narration reference:** The explanation of checking the generated answer or reflecting on its support.

**Visual type:** Answer verification animation.

**Visual execution:**

- Show the evidence entering the generation stage.
- Reveal a draft answer.
- Display an evaluation layer that checks the answer against the retrieved evidence.
- Highlight supported claims.
- Mark an unsupported claim with an amber warning.
- If the narrated workflow includes regeneration or correction, animate that step only when explained.

**On-screen text:**

`GENERATED ANSWER`

`SUPPORT CHECK`

`REFLECTION`

## Scene 05 — Self-RAG workflow recap

**Narration reference:** The concluding explanation of the reflection-based process.

**Visual type:** Full architecture recap.

**Visual execution:**

- Display the complete narrated workflow:
  query assessment → retrieval decision → retrieval → evidence evaluation → generation → reflection.
- Use arrows to show the actual order.
- Highlight the reflection stage.
- Keep the architecture clean and readable.
- Avoid adding unrelated agent loops or external tool-calling behavior.

**On-screen text:**

`RETRIEVE`

`GENERATE`

`REFLECT`

**Transition:** Move from improving retrieval and generation behavior to an important architectural decision: when should we use RAG, and when should we fine-tune a model?

---

# SCRIPT 28 — RAG VS FINE-TUNING

**Learning objective:** Explain the difference between retrieval-augmented generation and fine-tuning, including the different problems they solve.

**Main visual idea:** Two distinct approaches shown side by side, with clear use cases and trade-offs.

## Scene 01 — Two different approaches

**Narration reference:** The opening explanation of RAG and fine-tuning as different ways to adapt an AI application.

**Visual type:** Side-by-side architecture introduction.

**Visual execution:**

- Split the screen into two equal panels.
- Left panel: RAG architecture.
- Right panel: fine-tuning workflow.
- Show the same base language model conceptually, but do not suggest that the two methods perform the same operation.
- Keep each workflow visually distinct.

**On-screen text:**

`RETRIEVAL-AUGMENTED GENERATION`

`FINE-TUNING`

## Scene 02 — RAG workflow

**Narration reference:** The explanation of retrieving external knowledge at query time.

**Visual type:** RAG architecture animation.

**Visual execution:**

- Show company documents being ingested.
- Show chunking and embedding generation.
- Show vectors stored in the vector database.
- Show a user query triggering retrieval.
- Show retrieved context entering the model.
- Reveal an answer with source citations if the narrated example includes them.
- Highlight that the knowledge source can be updated independently of model training, subject to indexing and freshness.

**On-screen text:**

`EXTERNAL KNOWLEDGE`

`RETRIEVAL`

`CONTEXT`

`GROUNDED ANSWER`

## Scene 03 — Fine-tuning workflow

**Narration reference:** The explanation of updating model parameters using training examples.

**Visual type:** Fine-tuning process animation.

**Visual execution:**

- Show a dataset of training examples.
- Move the dataset into a training pipeline.
- Show a base model entering the fine-tuning stage.
- Animate the model being updated.
- Show a resulting adapted model.
- Do not represent fine-tuning as simply uploading a document or adding text to a prompt.
- Do not show a live training run unless an actual one is performed.

**On-screen text:**

`TRAINING DATA`

`FINE-TUNING`

`UPDATED MODEL`

## Scene 04 — Compare the approaches

**Narration reference:** The explanation of differences, strengths or limitations.

**Visual type:** Comparison table or split-screen.

**Visual execution:**

Show a clean comparison using only the dimensions discussed in the narration.

Possible comparison rows:

| Dimension | RAG | Fine-tuning |
|---|---|---|
| Main purpose | Retrieve external knowledge | Adapt model behavior or capabilities |
| Knowledge updates | Update the indexed source | May require another training process |
| Source citations | Can preserve retrieved source references | Not inherently provided |
| Model parameters | Not necessarily changed | Updated during training |

Do not imply that fine-tuning is a reliable substitute for a frequently changing knowledge base.

**On-screen text:**

`KNOWLEDGE ACCESS`

`MODEL ADAPTATION`

`DIFFERENT PURPOSES`

## Scene 05 — When to choose each approach

**Narration reference:** The explanation of use cases or selection criteria.

**Visual type:** Scenario-based decision screen.

**Visual execution:**

- Show a company that needs answers from frequently updated documents.
- Highlight the RAG route.
- Show a scenario requiring consistent output style, specialized behavior or task adaptation, if discussed.
- Highlight fine-tuning where appropriate.
- If the narration mentions combining both, show a third combined architecture only at that point.
- Do not declare one technique universally better.

**On-screen text:**

`CHOOSE BASED ON THE PROBLEM`

`RAG`

`FINE-TUNING`

**Transition:** The next episode moves beyond text-only documents and introduces multimodal and graph-based knowledge representations.

---

# SCRIPT 29 — MULTIMODAL RAG AND GRAPH RAG

**Learning objective:** Introduce retrieval from different data modalities and retrieval that uses relationships represented in a knowledge graph.

**Main visual idea:** A knowledge system can work with more than plain text, and it can represent relationships between entities.

## Scene 01 — Beyond text documents

**Narration reference:** The opening explanation of information existing in multiple formats.

**Visual type:** Multimodal document overview.

**Visual execution:**

- Show the familiar Enterprise Knowledge Assistant document collection.
- Introduce different information types one by one:
  - Text.
  - Images.
  - Tables.
  - Audio.
  - Video.
- Use only the modalities actually discussed in the narration.
- Keep each item visually distinct.
- Show all selected items entering a common processing area.

**On-screen text:**

`TEXT`

`IMAGE`

`TABLE`

`AUDIO`

`VIDEO`

Only display modality labels that are included in the audio.

## Scene 02 — Multimodal ingestion

**Narration reference:** The explanation of processing different kinds of input.

**Visual type:** Multimodal processing diagram.

**Visual execution:**

- Show each input entering an appropriate processing stage.
- Text goes through text extraction.
- Images go through the image-processing or vision stage if covered.
- Audio goes through transcription or audio processing if covered.
- Tables retain their structured information if discussed.
- Show the outputs entering the relevant indexing or retrieval representation.
- Keep the processing paths separate until the point where the narration says they are combined.

**On-screen text:**

`MULTIMODAL INPUT`

`PROCESSING`

`REPRESENTATION`

`INDEXING`

Do not imply that every modality is processed identically.

## Scene 03 — Multimodal retrieval

**Narration reference:** The explanation of retrieving information from non-text or mixed-format content.

**Visual type:** Query and retrieval animation.

**Visual execution:**

- Show a user asking a question about the exact multimodal example used in the narration.
- Show the retrieval system locating the relevant image, table or other source.
- Display the retrieved source item.
- If the narration discusses text and image embeddings, show their representation paths separately.
- Keep the source references visible.
- Do not show unsupported image or video capabilities as already implemented in the project.

**On-screen text:**

`MULTIMODAL QUERY`

`RETRIEVED SOURCE`

`RELEVANT CONTENT`

## Scene 04 — Graph RAG introduction

**Narration reference:** The explanation of representing entities and their relationships.

**Visual type:** Knowledge graph animation.

**Visual execution:**

- Show a set of company-related entities from the fictional knowledge base.
- Display them as separate nodes.
- Connect related entities with labelled edges.
- Use only relationships supported by the narrated example.
- Show a small graph growing as relationships are added.
- Keep the labels clear and avoid creating an unnecessarily dense network.

**On-screen text:**

`ENTITY`

`RELATIONSHIP`

`KNOWLEDGE GRAPH`

## Scene 05 — Graph-based retrieval

**Narration reference:** The explanation of using relationships to retrieve connected information.

**Visual type:** Graph traversal animation.

**Visual execution:**

- Show a user question.
- Highlight the starting entity.
- Animate the retrieval path across relevant relationships.
- Highlight connected nodes.
- Show the related information being collected.
- If the narration discusses combining graph retrieval with vector retrieval, show two distinct paths converging into a common context stage.
- Do not portray graph traversal as identical to vector similarity search.

**On-screen text:**

`STARTING ENTITY`

`RELATIONSHIP PATH`

`CONNECTED INFORMATION`

## Scene 06 — Multimodal RAG versus Graph RAG

**Narration reference:** Only if the narration compares the two approaches.

**Visual type:** Side-by-side comparison.

**Visual execution:**

- Left: multiple content modalities entering retrieval.
- Right: entities and relationships forming a graph.
- Show the distinct purpose of each approach.
- If the narration describes a combined system, show how both can contribute to a shared answer-generation workflow.
- Keep the final architecture consistent with what is actually explained.

**On-screen text:**

`MULTIMODAL RAG`

`GRAPH RAG`

**Transition:** Move from advanced architectures to the final episode: how to evaluate, operate and improve a complete RAG application.

---

# SCRIPT 30 — EVALUATION, PRODUCTION AND HUMAN PROJECT

**Learning objective:** Bring together the RAG engineering workflow, demonstrate how to evaluate it, explain production considerations and showcase the completed Enterprise Knowledge Assistant.

**Main visual idea:** Transform the concepts taught throughout the course into one complete, testable application.

## Scene 01 — The complete RAG system

**Narration reference:** The opening recap of the complete RAG architecture or the final project.

**Visual type:** Full-screen architecture reveal.

**Visual execution:**

- Begin with a dark background.
- Reveal the complete Enterprise Knowledge Assistant architecture.
- Animate the document ingestion lane.
- Show parsing, cleaning and chunking.
- Show embedding generation and vector storage.
- Animate the user query entering the retrieval lane.
- Show retrieval, context assembly and generation.
- End with the final answer and source citation.
- Reuse the same architecture elements shown throughout Scripts 1–29.

**On-screen text:**

`ENTERPRISE KNOWLEDGE ASSISTANT`

`COMPLETE RAG PIPELINE`

Do not introduce new architecture components in the recap unless the narration covers them.

## Scene 02 — Evaluation dataset

**Narration reference:** The explanation of evaluating whether the RAG system works correctly.

**Visual type:** Real code and dataset demonstration.

**Visual execution:**

- Open `evaluation/dataset.json`.
- Show a small synthetic test dataset.
- Highlight the questions and expected evidence or expected answers.
- Show different test cases:
  - Answerable question.
  - Question with incomplete evidence.
  - Question with no supporting document.
- Use actual project data.
- Keep personal or confidential information out of the recording.

**On-screen text:**

`EVALUATION DATASET`

`TEST QUESTIONS`

`EXPECTED EVIDENCE`

## Scene 03 — Retrieval evaluation

**Narration reference:** The explanation of measuring retrieval quality.

**Visual type:** Metric visualization.

**Visual execution:**

- Show the query entering the retrieval system.
- Display the retrieved chunks.
- Compare retrieved evidence with the expected relevant evidence.
- Show only the retrieval metrics explicitly discussed in the narration.
- If precision@K, recall@K, MRR or another metric is mentioned, reveal its name at the exact point it is explained.
- Use real measured results if available.
- If using illustrative values, label them clearly as illustrative.

**On-screen text:**

Use only the narrated metric names, for example:

`PRECISION@K`

`RECALL@K`

`MRR`

Do not fabricate numerical results.

## Scene 04 — Answer evaluation

**Narration reference:** The explanation of evaluating generated answers separately from retrieval.

**Visual type:** Answer assessment visualization.

**Visual execution:**

- Show retrieved context beside the generated answer.
- Highlight answer claims.
- Compare each claim with the retrieved evidence.
- Show whether the answer is supported, incomplete or irrelevant.
- Display only the evaluation metrics covered in the narration.
- If faithfulness or answer relevancy is discussed, reveal those labels at the corresponding moment.

**On-screen text:**

`FAITHFULNESS`

`ANSWER RELEVANCY`

`CONTEXT QUALITY`

Keep retrieval metrics and answer-generation metrics visually separate.

## Scene 05 — Debugging a failed query

**Narration reference:** The explanation of investigating why an answer was incorrect or incomplete.

**Visual type:** Real debugging demonstration.

**Visual execution:**

- Open the actual application.
- Submit a question that produces a known failure in the test environment.
- Show the query trace.
- Display the retrieved chunk IDs and relevant content.
- Show the assembled context.
- Show the generated answer.
- Trace the problem back to the stage responsible.
- If the issue is caused by retrieval, highlight retrieval.
- If the issue is caused by missing source content or generation, highlight that stage instead.
- Show the corrected behavior only if it has actually been tested.

**On-screen text:**

`QUERY TRACE`

`RETRIEVED CHUNKS`

`CONTEXT`

`GENERATED ANSWER`

`ROOT CAUSE`

## Scene 06 — Production architecture

**Narration reference:** The explanation of taking a RAG system from a working demonstration toward production.

**Visual type:** Production architecture diagram.

**Visual execution:**

- Show the frontend, backend API, RAG services and vector database.
- Add the production components discussed in the narration.
- Possible elements include:
  - Authentication.
  - Authorization.
  - Document access control.
  - Logging.
  - Monitoring.
  - Error handling.
  - Caching.
  - Rate limiting.
  - Document updates.
- Only add components covered in the audio.
- Show the flow from a user request through the backend and retrieval pipeline.
- Highlight the security boundary between authorized users and protected documents.

**On-screen text:**

Use only the relevant labels from the narration:

`AUTHENTICATION`

`AUTHORIZATION`

`MONITORING`

`LOGGING`

`DOCUMENT FRESHNESS`

`ERROR HANDLING`

**Security requirement:** Never portray a prompt instruction as a replacement for actual authorization checks. If document permissions are discussed, show permission enforcement before unauthorized content reaches the generation context.

## Scene 07 — Latency, cost and reliability

**Narration reference:** Any discussion of performance, resource usage, reliability or production trade-offs.

**Visual type:** Monitoring dashboard.

**Visual execution:**

- Show a realistic monitoring dashboard.
- Display the metrics discussed in the narration.
- Use real measurements only if a working system has been instrumented.
- If values are illustrative, label the dashboard `ILLUSTRATIVE`.
- Show a request moving through the pipeline.
- Highlight the relevant stage when latency or failure is discussed.
- Do not fabricate system performance claims.

**On-screen text:**

Use only relevant narrated labels:

`LATENCY`

`COST`

`ERROR RATE`

`RETRIEVAL QUALITY`

`SYSTEM HEALTH`

## Scene 08 — Final project demonstration

**Narration reference:** The practical final demonstration of the Enterprise Knowledge Assistant.

**Visual type:** Actual product screen recording.

**Visual execution:**

This must be a real demonstration of the completed project.

Show the following actions in order, provided they are implemented:

1. Open the application.
2. Show the document collection.
3. Upload a supported document.
4. Show actual processing progress.
5. Ask a question.
6. Show the actual retrieval result if the application exposes it.
7. Show the generated answer.
8. Open or inspect the source citation if implemented.
9. Ask a second question that tests a different part of the knowledge base.
10. Demonstrate an unanswerable question and the application's actual fallback behavior.

Do not simulate successful outputs. Record the real application.

**On-screen text:**

`DOCUMENT UPLOAD`

`ASK A QUESTION`

`RETRIEVAL`

`GROUNDED ANSWER`

`SOURCE CITATION`

## Scene 09 — Project architecture and codebase

**Narration reference:** The explanation of how the complete project is organized or built.

**Visual type:** VS Code and project structure recording.

**Visual execution:**

- Open the actual Git repository.
- Show the project folder structure.
- Highlight the important modules.
- Show the API entry point.
- Show the retrieval and generation modules.
- Show the evaluation files.
- Show tests and README if available.
- Do not show unimplemented modules as finished.

**On-screen text:**

`PROJECT STRUCTURE`

`MODULAR ARCHITECTURE`

`TESTED IMPLEMENTATION`

## Scene 10 — Final course architecture recap

**Narration reference:** The concluding summary of what learners have built or learned.

**Visual type:** Full-screen course journey.

**Visual execution:**

- Start with the initial problem from Script 1.
- Show the RAG pipeline developing across the course.
- Briefly revisit the most important technical milestones:
  - Document ingestion.
  - Chunking.
  - Embeddings.
  - Vector databases.
  - Retrieval engineering.
  - Generation and citations.
  - Advanced RAG.
  - Evaluation and production.
- Bring all components into one complete architecture.
- End on the working Enterprise Knowledge Assistant.
- Use a smooth camera pullback to reveal the full system.

**On-screen text:**

`FROM CONCEPT TO WORKING RAG SYSTEM`

`ENTERPRISE KNOWLEDGE ASSISTANT`

Do not add a new lesson or technical claim during the final recap.

---

# 3. MASTER SCREEN-RECORDING CHECKLIST

Create the following recording assets for Scripts 21–30.

| Asset ID | Episode | Required recording |
|---|---|---|
| SR-43 | 21 | RAPTOR hierarchy conceptual or implemented workflow |
| SR-44 | 21 | Actual hierarchical retrieval output, if implemented |
| SR-45 | 22 | Token-level representation illustration or tested output |
| SR-46 | 22 | ColBERT retrieval implementation, if available |
| SR-47 | 23 | Initial retrieval results with relevance assessment |
| SR-48 | 23 | Corrective retrieval path, if implemented |
| SR-49 | 24 | Adaptive query strategy example |
| SR-50 | 24 | Actual strategy selection code, if implemented |
| SR-51 | 25 | Candidate retrieval list with repeated chunks |
| SR-52 | 25 | Actual MMR selection output, if implemented |
| SR-53 | 26 | First retrieval hop |
| SR-54 | 26 | Follow-up retrieval hop |
| SR-55 | 27 | Retrieval decision or reflection workflow |
| SR-56 | 27 | Actual critique or evaluation output, if implemented |
| SR-57 | 28 | RAG architecture demonstration |
| SR-58 | 28 | Fine-tuning workflow conceptual demonstration |
| SR-59 | 29 | Multimodal input processing, if implemented |
| SR-60 | 29 | Knowledge graph visualization |
| SR-61 | 30 | Evaluation dataset and evaluation code |
| SR-62 | 30 | Actual retrieval and answer evaluation output |
| SR-63 | 30 | Debugging trace |
| SR-64 | 30 | Production architecture |
| SR-65 | 30 | Complete final project demonstration |
| SR-66 | 30 | Final project repository and README |

**Recording rule:** If an advanced method is not implemented in the flagship application, do not pretend that it is. Use a conceptual demonstration or a separate clearly labelled experimental implementation.

---

# 4. MASTER ANIMATION AND DIAGRAM ASSET LIST

| Diagram ID | Episode | Diagram title | Main visual purpose |
|---|---|---|---|
| DG-43 | 21 | RAPTOR hierarchy | Show chunks, grouped summaries and hierarchy |
| DG-44 | 21 | Hierarchical retrieval | Show retrieval from different hierarchy levels |
| DG-45 | 22 | ColBERT token representations | Show multiple token-level vectors |
| DG-46 | 22 | Late interaction | Show query-document token matching |
| DG-47 | 23 | CRAG evaluation | Show retrieved evidence being assessed |
| DG-48 | 23 | Corrective retrieval | Show the correction path |
| DG-49 | 24 | Adaptive RAG decision | Show query-dependent processing |
| DG-50 | 24 | Adaptive retrieval paths | Show different strategies |
| DG-51 | 25 | MMR relevance and diversity | Show the relevance-diversity trade-off |
| DG-52 | 25 | MMR result selection | Show redundant candidates being reduced |
| DG-53 | 26 | Multi-hop retrieval | Show sequential retrieval steps |
| DG-54 | 26 | Evidence chain | Connect evidence across multiple sources |
| DG-55 | 27 | Self-RAG reflection | Show retrieval, generation and reflection |
| DG-56 | 27 | Answer critique | Show evidence-supported and unsupported claims |
| DG-57 | 28 | RAG versus fine-tuning | Show two distinct adaptation approaches |
| DG-58 | 28 | Selection decision | Show when each approach may be appropriate |
| DG-59 | 29 | Multimodal ingestion | Show multiple data modalities |
| DG-60 | 29 | Graph RAG | Show entities and relationships |
| DG-61 | 29 | Graph retrieval | Show relationship-based retrieval |
| DG-62 | 30 | Complete RAG architecture | Bring together the complete course workflow |
| DG-63 | 30 | Evaluation architecture | Separate retrieval and answer evaluation |
| DG-64 | 30 | Production architecture | Show security, monitoring and application components |

---

# 5. HIGGSFIELD / MOTION GRAPHIC PROMPTS

Use these prompts to generate supporting animations. Maintain the same dark visual style and use English labels.

## DG-43 — RAPTOR hierarchical retrieval

"Create a premium 16:9 technical educational animation. Begin with a large document split into many small text chunks. Group related chunks into clusters. Create higher-level summary nodes above the groups and organize the representations into a hierarchical tree. Show original chunks at the bottom and higher-level summaries above them. Use amber for source chunks and cyan for summary nodes. Keep parent-child relationships clear. Do not make the hierarchy look like a file-folder system."

## DG-45 — ColBERT token representations

"Create a technically accurate educational animation showing a query sentence and a document sentence split into tokens. Pass the tokens through a contextual representation stage. Show multiple abstract vector representations for query tokens and document tokens. Do not assign human meanings to individual vector dimensions. Keep query and document token representations visually distinct. Use readable labels: QUERY TOKENS, DOCUMENT TOKENS, TOKEN REPRESENTATIONS."

## DG-46 — ColBERT late interaction

"Create a clean technical motion graphic. Place query token representations on the left and document token representations on the right. Animate token-level matching connections between them. Show the strongest matching document representation for each query token, then aggregate the matching contributions into a document relevance score. If MaxSim is displayed, use the correct terminology. Do not imply that this is ordinary single-vector cosine similarity."

## DG-47 — CRAG evaluation

"Create a technically accurate RAG workflow in a dark premium style. Show a user query entering retrieval. Three retrieved document chunks move into a relevance evaluation component. Show one relevant result and two results that are insufficient or irrelevant. Direct the results through an evaluation stage before they reach generation. Use clear labels: RETRIEVAL, EVALUATION, RELEVANT, INSUFFICIENT EVIDENCE. Do not imply that an LLM automatically verifies all facts."

## DG-48 — Corrective retrieval

"Create an educational branching workflow. A query retrieves initial document candidates. An evaluator assesses their relevance. The relevant path moves toward context assembly, while the insufficient-evidence path moves toward a correction or additional retrieval stage. Keep both paths separate and animate only the correction method specified in the lesson. Use labels: INITIAL RETRIEVAL, EVALUATION, CORRECTIVE ACTION, RETRIEVAL AGAIN."

## DG-49 — Adaptive RAG decision

"Create a clean technical animation showing three user queries with different levels of complexity. Each query enters an adaptive decision component. The component selects a different processing path according to the query. Animate only the selected route for each query. Use readable labels: QUERY ANALYSIS, ADAPTIVE DECISION, SELECTED STRATEGY. Do not claim that the system is always faster or more accurate."

## DG-51 — MMR relevance and diversity

"Create a premium technical visualization showing a set of candidate document chunks. Several candidates are highly similar to one another. Display two conceptual dimensions labelled QUERY RELEVANCE and DIVERSITY. Highlight one candidate that is relevant but redundant, and another that is relevant while contributing different information. Use no fabricated numerical scores. Make the relevance-diversity trade-off visually clear."

## DG-53 — Multi-hop retrieval

"Create a technically accurate retrieval animation. A complex user question enters a retrieval system and returns a first source passage. Information from the first passage leads to a follow-up query. The follow-up query retrieves a second passage. Connect the two passages with a visible relationship line. Show the combined evidence moving toward context assembly. Use labels: ORIGINAL QUERY, HOP 1, FOLLOW-UP QUERY, HOP 2, CONNECTED EVIDENCE."

## DG-55 — Self-RAG reflection

"Create a clean educational architecture diagram showing query assessment, retrieval decision, retrieval, evidence evaluation, answer generation and reflection. Display retrieved source passages beside the generated answer. Highlight a supported claim in green and an unsupported claim with an amber warning. Keep the reflection stage visible as a distinct evaluation process. Do not add unrelated external tools or multi-agent components."

## DG-57 — RAG versus fine-tuning

"Create a premium 16:9 split-screen educational animation. On the left, show RAG: external documents, indexing, retrieval, context and a language model producing an evidence-grounded answer. On the right, show fine-tuning: training examples entering a training process that updates model parameters and produces an adapted model. Clearly distinguish retrieval at query time from model training. Do not represent fine-tuning as document upload."

## DG-59 — Multimodal ingestion

"Create a technically accurate dark-theme animation showing different source modalities entering a knowledge system: text, image, table, audio and video. Give each modality an appropriate processing path. Show text extraction for text documents, vision processing for images, and audio processing or transcription for audio only where appropriate. Keep the paths distinct and show their resulting representations entering indexing. Do not imply every modality uses the same processing method."

## DG-60 — Graph RAG

"Create a clean technical knowledge graph animation. Display fictional company entities as separate nodes and their relationships as labelled edges. Use a small number of nodes so every relationship is readable. Animate the graph growing as relationships are added. Use labels such as ENTITY, RELATIONSHIP and KNOWLEDGE GRAPH. Do not create unsupported relationships or turn the graph into an ordinary flowchart."

## DG-61 — Graph retrieval

"Create a technically accurate graph retrieval animation. A user query identifies a starting entity. Highlight the entity and animate traversal through relevant labelled relationships to connected entities. Show the connected information being collected as retrieval evidence. Keep graph traversal visually distinct from vector similarity search."

## DG-62 — Complete RAG architecture

"Create a premium full-screen 16:9 technical architecture animation for an Enterprise Knowledge Assistant. Show the document indexing lane: document upload, parsing, cleaning, chunking, embedding and vector storage. Show the query lane: user question, query processing, retrieval, context assembly, language model generation and grounded answer with source citation. Reuse a consistent visual language and animate the complete data flow. Do not add unsupported components."

## DG-63 — RAG evaluation

"Create a clear evaluation architecture showing a test dataset feeding a RAG system. Separate retrieval evaluation from answer evaluation. Show retrieved chunks compared with expected evidence, then generated answers compared with supporting context. Display only the metric names supplied by the lesson. Do not invent numerical benchmark results."

## DG-64 — Production RAG architecture

"Create a technically accurate enterprise RAG production diagram. Show user authentication, authorization, backend API, retrieval services, vector database, language model and response delivery. Add monitoring, logging, error handling and document freshness components only where the lesson covers them. Show access permissions being enforced before unauthorized document content can enter context. Use a clean dark background and readable labels. Do not suggest that prompt instructions replace security controls."

---

# 6. FINAL CLAUDE EXECUTION INSTRUCTIONS

Before generating the final video production plan:

1. Inspect the ten finalized narration files for Scripts 21–30.
2. Identify every concept and example in each narration.
3. Use the narration as the final authority.
4. Preserve the original episode numbering and exact titles.
5. Synchronize each visual to the actual spoken sentence.
6. Use the same Enterprise Knowledge Assistant project.
7. Maintain visual continuity with Scripts 1–20.
8. Use actual code and tested outputs for implementation demonstrations.
9. Use diagrams for conceptual methods that are not implemented.
10. Do not invent benchmark scores, evaluation results or system performance.
11. Do not show fictional source documents as real company policies.
12. Do not introduce content from outside the narrated scope.
13. Use actual audio duration for final timestamps.
14. Ensure every on-screen technical term is correctly spelled.
15. Keep all important text readable.
16. Do not add a quiz unless the supplied audio includes one.
17. Keep the final project demonstration authentic.

## Required output for every episode

Return:

- Episode number and exact title.
- Actual audio duration.
- Learning objective.
- Detailed scene-by-scene storyboard.
- Exact narration reference for each scene.
- Visual type.
- Exact screen content.
- Detailed execution instructions for the editor.
- On-screen text.
- Animation instructions.
- Transition instructions.
- Required screen recordings.
- Required generated assets.
- Technical accuracy checklist.

## Final production standard

The editor must be able to understand:

- What appears on screen.
- When it appears.
- What changes during the scene.
- Which part of the application must be recorded.
- Which code or output must be highlighted.
- What the viewer should understand.
- When the scene must transition.

The final ten videos must feel like the natural continuation and completion of the same RAG course—not a collection of disconnected advanced-topic animations.

**The final outcome should take learners from understanding advanced RAG techniques to seeing how a complete, evaluated and production-conscious RAG application is engineered.**