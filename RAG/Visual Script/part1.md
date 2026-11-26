# BOT ACADEMY — RAG COURSE
# VIDEO GENERATION ACTION SCRIPT — SCRIPTS 01 TO 10

**Production tools:** Claude + Higgsfield + Video Editing Software  
**Voice source:** The ten finalized ElevenLabs RAG narration scripts supplied separately  
**Course:** Retrieval-Augmented Generation (RAG)  
**Main visual format:** Premium technical education video  
**Project continuity:** Enterprise Knowledge Assistant  
**Visual language:** English technical labels, English code, natural Tanglish narration  
**Output:** Detailed scene-by-scene visual production instructions

---

# GLOBAL PRODUCTION INSTRUCTIONS

These instructions apply to all ten scripts.

## 1. Voice and visual synchronization

The supplied ElevenLabs audio is the single source of truth.

- Do not rewrite, shorten, rearrange or paraphrase the narration.
- Do not omit any spoken sentence.
- Every visual must appear at the exact point where its corresponding concept is explained.
- Do not show a concept before the narration introduces it.
- Do not keep an old visual on screen after the narration moves to another concept.
- Break each audio script into individual scenes based on the actual spoken content.
- Use the actual audio waveform to determine final timestamps.
- Planned timestamps must never override the real narration timing.
- Do not add additional spoken explanations.

Every scene must contain:
1. Scene number.
2. Narration reference.
3. Exact visual action.
4. Visual type.
5. On-screen text.
6. Animation or screen-recording instructions.
7. Transition into the next scene.

## 2. Overall visual identity

Maintain one consistent premium educational technology aesthetic.

**Visual design:**
- Dark charcoal or deep navy backgrounds.
- White primary typography.
- Restrained cyan and blue highlights for data movement and retrieval.
- Warm amber highlights for documents and source evidence.
- Green for successful or verified states.
- Red or amber for warnings and failed retrieval.

**Typography:**
- Use clean, modern sans-serif typography.
- Large readable headings.
- Clear technical labels.
- Monospaced fonts for code.
- Avoid decorative fonts in technical demonstrations.

**Animation:**
- Use smooth, meaningful transitions.
- Use 2D and 3D motion graphics when they help explain technical concepts.
- Use realistic browser, terminal and VS Code interfaces.
- Keep diagrams minimal and technically accurate.
- Avoid random futuristic robots, floating holograms and meaningless AI imagery.
- Avoid making the video look like a PowerPoint presentation.

The video should feel like a professionally produced technology education series.

## 3. Code demonstration rules

Whenever the narration introduces Python, libraries, methods or actual implementation:

- Show a realistic VS Code interface.
- Show the correct project file.
- Reveal code progressively, in the same order it is discussed.
- Highlight the exact line currently being explained.
- Zoom into the relevant code.
- Show the cursor moving to the relevant variable, function or method.
- Execute code only after the narration reaches the execution step.
- Display actual program output.
- Never invent embeddings, token IDs, similarity scores, database records or terminal logs.
- If actual output is unavailable, mark the visual as a planned demonstration and do not present it as a successful execution.

Do not replace a coding demonstration with a generic animation when the narration is explaining actual code.

## 4. Project continuity

Use one consistent project throughout all ten scripts.

**PROJECT: Enterprise Knowledge Assistant**

The application should progressively evolve through the course.

Suggested project structure:

```text
enterprise-knowledge-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── services/
│   │   │   ├── ingestion.py
│   │   │   ├── parsing.py
│   │   │   ├── text_cleaning.py
│   │   │   ├── chunking.py
│   │   │   ├── embeddings.py
│   │   │   ├── vector_store.py
│   │   │   ├── retrieval.py
│   │   │   ├── reranking.py
│   │   │   └── context_builder.py
│   │   └── api/
│   │       └── routes.py
│   │
│   └── requirements.txt
│
├── sample_data/
│   └── sample_employee_handbook.pdf
│
├── tests/
│
└── README.md
```

This is the proposed recording structure. The production team must use the actual implemented project and its real function names. Do not pretend that unimplemented modules already exist.

Use a fictional sample handbook containing sections such as:
- Work-from-home policy.
- Annual leave policy.
- Travel reimbursement.
- Employee benefits.
- Maternity leave policy.

Keep the same fictional document throughout the relevant demonstrations.

---

# SCRIPT 01 — WHY RAG IS NEEDED

**Learning Objective:** Demonstrate the limitations of relying solely on an LLM's existing knowledge and introduce the need for retrieving relevant information from external knowledge sources.

---

## SCENE 01 — THE OPENING QUESTION

**Narration Reference:**  
The opening question about asking ChatGPT for the latest internal examination timetable of a college.

**Visual Type:**  
Realistic UI Demonstration

**Visual Action:**

1. Begin with a clean, dark background. Gradually reveal a laptop positioned at the centre of the frame.
2. Display a realistic, ChatGPT-style conversational interface on the laptop screen.
3. Move the cursor towards the chat input field.
4. Type the question being asked in the narration:  
   **"What is my college's latest internal examination timetable?"**
5. Press Enter and animate the response appearing on the screen.
6. Display an illustrative response indicating that the model does not have access to the college's latest timetable unless the relevant information is provided.
7. Pause briefly to allow viewers to read the response.
8. Highlight the absence of the actual college timetable as the key limitation.

**On-Screen Text:**

`WHAT IS MY COLLEGE'S LATEST INTERNAL EXAM TIMETABLE?`

`NO TIMETABLE DOCUMENT PROVIDED`

**Important Production Note:**  
The interface and response should be treated as an illustrative demonstration, not an actual ChatGPT response. Do not display an invented college timetable or present unverified information as factual.

**Transition:**  
Slowly zoom into the response. Fade in a question mark beside it, creating a visual sense of uncertainty. Then transition into the knowledge gap comparison.

---

## SCENE 02 — THE KNOWLEDGE GAP

**Narration Reference:**  
The explanation that a language model may not have access to the latest or college-specific information within its existing knowledge.

**Visual Type:**  
Split-Screen Comparison

**Visual Action:**

1. Divide the screen into two distinct sections.
2. On the left, display a visual representation of a general-purpose language model.
3. On the right, introduce a private college document folder.
4. Open the folder and reveal a document titled **Internal Examination Timetable**.
5. Keep the document folder visually separated from the language model.
6. Show the same user question appearing between the two sections.
7. Animate the language model attempting to respond without having access to the timetable.
8. Introduce a visual warning between the model and the document folder to indicate that no connection has been established.
9. Briefly highlight the disconnected document folder to reinforce that the required information exists, but is not available to the model.

**On-Screen Text:**

`MODEL'S EXISTING KNOWLEDGE`

`COLLEGE-SPECIFIC INFORMATION`

`NO CONNECTED SOURCE`

**Important Production Note:**  
Make it clear that a language model does not automatically access private college documents or live institutional information. The document must be explicitly provided or connected through an appropriate retrieval system.

**Transition:**  
Animate a connection line beginning to form between the private document folder and the language model. Use this movement to introduce other situations where external information is required.

---

## SCENE 03 — WHY EXISTING KNOWLEDGE IS NOT ENOUGH

**Narration Reference:**  
The explanation of why private, recently updated, and organization-specific information cannot always be answered using only a model's existing knowledge.

**Visual Type:**  
Motion Graphics / Animated Concept Illustration

**Visual Action:**

1. Display a language model on the left side of the screen.
2. On the right side, introduce three different documents one after another.

   - **Document One:** A recently updated college examination timetable.
   - **Document Two:** An internal company travel reimbursement policy.
   - **Document Three:** A recently updated product user manual.

3. Animate each document opening briefly to reveal relevant information inside.
4. Display a suitable label beside each document:

   - `UPDATED INFORMATION`
   - `PRIVATE INFORMATION`
   - `ORGANIZATION-SPECIFIC INFORMATION`

5. Keep all three documents outside the language model's existing knowledge boundary.
6. Show a user question appearing for each document, such as asking about an examination date, the maximum travel reimbursement amount, or a product procedure.
7. Animate the model receiving the questions while the required documents remain disconnected.
8. Highlight the gap between the user's required information and the information currently available to the model.

**On-Screen Text:**

`THE KNOWLEDGE GAP`

`INFORMATION EXISTS — BUT IS NOT CONNECTED`

**Transition:**  
Move the three documents towards the language model. As they approach, introduce a retrieval component between them. This component becomes the visual bridge into the RAG concept.

---

## SCENE 04 — INTRODUCING RAG

**Narration Reference:**  
The first explanation of Retrieval-Augmented Generation and how external information is retrieved and supplied to a language model before generating an answer.

**Visual Type:**  
Premium Animated Technical Diagram

**Visual Action:**

1. Begin with a clean, dark technical background.
2. Introduce a document library on the left side of the screen. Show multiple documents representing an external knowledge source.
3. Animate a user's question entering the system from the bottom of the screen.
4. Introduce a retrieval component between the document library and the language model.
5. Highlight the retrieval component as it receives the user's question.
6. Animate the system searching through the available documents.
7. Show only the relevant passages being selected from the larger document collection.
8. Move these selected passages towards the language model.
9. Introduce the user's original question alongside the retrieved passages, showing that both are provided as context to the language model.
10. Animate the language model processing the question and the retrieved information together.
11. Display the generated answer returning to the user.
12. Finally, highlight the source document from which the relevant information was retrieved.
13. Reveal the complete RAG workflow only after each individual stage has been introduced.

**On-Screen Text:**

`RETRIEVAL-AUGMENTED GENERATION`

`RETRIEVE → AUGMENT → GENERATE`

`USER QUESTION + RETRIEVED CONTEXT`

`GROUNDED ANSWER`

**Important Production Note:**  
Maintain a clear distinction between retrieving relevant information and generating the final answer. The retrieval component finds relevant information from the external knowledge source; the language model uses that information along with the user's question to generate the response.

**Transition:**  
Zoom out to reveal the complete RAG architecture. Briefly highlight the flow from the document library to retrieval, then to the language model, and finally to the user. Hold the complete diagram on screen before transitioning into Script 02.

---

# SCRIPT 02 — THE THREE STAGES OF RAG

**Learning objective:** Explain the three major stages of RAG: Indexing, Retrieval and Generation.

## SCENE 01 — INTRODUCING THE THREE STAGES

**Narration reference:** The narration introduces the three main stages of RAG.

**Visual type:** Animated architecture reveal.

**Visual action:**

1. Start with a blank dark screen.
2. Reveal three large connected blocks one after another.
3. First block: Indexing.
4. Second block: Retrieval.
5. Third block: Generation.
6. Connect the three blocks using directional arrows.
7. Keep the entire flow visible.

**On-screen text:**

`01 INDEXING`

`02 RETRIEVAL`

`03 GENERATION`

**Transition:** Zoom into Indexing.

## SCENE 02 — STAGE ONE: INDEXING

**Narration reference:** Documents are processed and prepared before users ask questions.

**Visual type:** Animated technical diagram.

**Visual action:**

1. Show multiple documents entering the system.
2. Show PDF, DOCX and TXT file icons.
3. Move the documents into a processing pipeline.
4. Show text extraction.
5. Show extracted text being divided into smaller chunks.
6. Show chunks entering an embedding model.
7. Show numerical vectors being generated.
8. Move the vectors into a vector database.

Reveal each stage only when the narration introduces it.

**On-screen text:**

`DOCUMENTS`

`TEXT EXTRACTION`

`CHUNKING`

`EMBEDDINGS`

`VECTOR DATABASE`

**Important:** Do not introduce advanced retrieval methods here.

**Transition:** Move from the stored vectors to a user question.

## SCENE 03 — STAGE TWO: RETRIEVAL

**Narration reference:** A user asks a question and the system finds relevant information.

**Visual type:** Animated diagram + application UI.

**Visual action:**

1. Show the Enterprise Knowledge Assistant interface.
2. Type the question from the narration.
3. Animate the question entering the retrieval pipeline.
4. Show the query being converted into a vector if that step is explained in the audio.
5. Show the vector database being searched.
6. Highlight the most relevant stored document chunks.
7. Bring the selected chunks out of the database.

**On-screen text:**

`USER QUESTION`

`RETRIEVAL`

`RELEVANT CHUNKS`

**Transition:** Selected chunks move towards the generation stage.

## SCENE 04 — STAGE THREE: GENERATION

**Narration reference:** Retrieved information is supplied to the language model to generate the answer.

**Visual type:** Animated architecture + realistic chat UI.

**Visual action:**

1. Show the original user question.
2. Show the retrieved document chunks.
3. Place both into a context panel.
4. Move the context panel into the LLM.
5. Animate the model generating an answer.
6. Show the answer in the chat interface.
7. If citations are part of the narration, show the relevant source reference.

**On-screen text:**

`QUESTION + RETRIEVED CONTEXT`

`LLM`

`GENERATED ANSWER`

**Important:** Do not suggest that generation alone guarantees correctness.

**Transition:** Zoom out to show the full three-stage pipeline.

## SCENE 05 — COMPLETE RAG WORKFLOW

**Narration reference:** The recap of Indexing, Retrieval and Generation.

**Visual type:** Full architecture animation.

**Visual action:**

Show the complete flow in two distinct lanes.

**Upper lane — Indexing:**

`Documents → Extraction → Chunking → Embeddings → Vector Database`

**Lower lane — Query processing:**

`User Question → Retrieval → Relevant Chunks → Context → Generation → Answer`

Animate the upper lane first. Then animate the lower lane.

Keep both lanes visible together at the end.

**Transition:** A document enters the indexing lane and fills the screen, introducing Script 03.

---

# SCRIPT 03 — DOCUMENT INGESTION AND EXTRACTION

**Learning objective:** Explain how source documents enter a RAG system and how their text is extracted and prepared for processing.

## SCENE 01 — WHY DOCUMENT INGESTION IS REQUIRED

**Narration reference:** The opening explanation about supplying documents to a RAG system.

**Visual type:** Real-world document animation.

**Visual action:**

1. Show a folder containing different documents.
2. Display PDF, DOCX, TXT and other formats mentioned in the narration.
3. Animate the documents moving into a central upload area.
4. Show the upload process starting.
5. Label the overall stage as Document Ingestion.

**On-screen text:**

`DOCUMENT INGESTION`

`SOURCE FILES → RAG PIPELINE`

**Transition:** Zoom into a PDF file.

## SCENE 02 — DOCUMENT UPLOAD

**Narration reference:** The explanation of loading documents into the application.

**Visual type:** Actual browser recording.

**Visual action:**

1. Open the Enterprise Knowledge Assistant in a browser.
2. Show the document upload section.
3. Select `sample_employee_handbook.pdf`.
4. Click Upload.
5. Show the actual upload state.
6. Show the filename and file type.
7. Do not fabricate a successful upload status.

**On-screen text:**

`UPLOAD DOCUMENT`

`sample_employee_handbook.pdf`

**Transition:** The uploaded PDF moves into the backend processing pipeline.

## SCENE 03 — DOCUMENT PARSING

**Narration reference:** The narration explains reading and extracting document content.

**Visual type:** Technical animation + code demonstration if included in the audio.

**Visual action:**

1. Show a PDF page.
2. Highlight the text, headings and paragraphs.
3. Move the PDF into a component labelled Parser.
4. Animate extracted text appearing in a separate panel.
5. Show that the output is text rather than a PDF page image.

If the narration introduces parsing libraries or code:

- Open the actual parsing module in VS Code.
- Reveal the import and parsing method as spoken.
- Highlight the exact lines.
- Show the extracted text from the actual sample document.

**On-screen text:**

`PDF`

`PARSER`

`EXTRACTED TEXT`

**Important:** Use real extraction output. Do not fabricate text or claim OCR has occurred unless OCR is actually used.

**Transition:** Move to the difference between text-based and scanned documents, only if discussed in the narration.

## SCENE 04 — TEXT-BASED PDF AND SCANNED PDF

**Narration reference:** Any explanation of document extraction limitations or OCR.

**Visual type:** Side-by-side technical comparison.

**Visual action:**

Left panel:
- Show a PDF containing selectable text.
- Highlight a sentence.
- Show the sentence being extracted.

Right panel:
- Show a scanned page containing an image of text.
- Attempt to select the text.
- Show that ordinary text extraction may not retrieve readable text from the scanned image.
- If OCR is discussed, show an OCR processing stage converting the image into extracted text.

**On-screen text:**

`TEXT-BASED PDF`

`SCANNED PDF`

`OCR — OPTICAL CHARACTER RECOGNITION`

Only show the OCR label if the narration introduces OCR.

**Transition:** Extracted text moves into a cleaning stage.

## SCENE 05 — TEXT CLEANING

**Narration reference:** The explanation of cleaning extracted text before downstream processing.

**Visual type:** Before-and-after text comparison.

**Visual action:**

1. Show raw extracted text containing line breaks, irregular spacing and repeated headers if these exist in the actual sample.
2. Highlight the unwanted formatting.
3. Move the text into a cleaning stage.
4. Show a cleaned version beside it.
5. Keep the before-and-after comparison visible.

**On-screen text:**

`RAW EXTRACTED TEXT`

`TEXT CLEANING`

`CLEAN TEXT`

**Important:** Do not invent a cleaning transformation that is not described in the narration.

## SCENE 06 — SOURCE INFORMATION AND METADATA

**Narration reference:** If the audio mentions retaining document source information.

**Visual type:** Structured data animation.

**Visual action:**

Show an extracted text passage with its associated source information.

Display fields such as:

`SOURCE FILE`

`PAGE NUMBER`

`DOCUMENT ID`

`SECTION`

Only display fields actually mentioned or demonstrated.

**Transition:** The cleaned text moves towards the chunking stage, leading into Script 04.

---

# SCRIPT 04 — CHUNKING STRATEGIES

**Learning objective:** Explain why documents are divided into chunks and visually compare fixed-size, recursive, structure-aware and semantic chunking.

## SCENE 01 — WHY CHUNKING IS NECESSARY

**Narration reference:** The opening problem of handling a large document as one complete block.

**Visual type:** Document animation.

**Visual action:**

1. Show a large employee handbook.
2. Expand it into multiple pages of text.
3. Compress all pages into one giant text block.
4. Show the block becoming difficult to manage visually.
5. Highlight the need to divide the document into smaller sections.

**On-screen text:**

`LARGE DOCUMENT`

`ONE GIANT TEXT BLOCK`

**Transition:** The giant text block separates into smaller sections.

## SCENE 02 — WHAT IS A CHUNK?

**Narration reference:** The definition and simple explanation of a chunk.

**Visual type:** Animated educational diagram.

**Visual action:**

1. Show a continuous paragraph.
2. Draw boundaries around a smaller section.
3. Separate it from the rest of the document.
4. Label the selected section Chunk 1.
5. Repeat for Chunk 2 and Chunk 3.
6. Show each chunk as an independent unit.

**On-screen text:**

`CHUNK 1`

`CHUNK 2`

`CHUNK 3`

`CHUNK = A SMALL SECTION OF TEXT`

**Transition:** Move to the first chunking strategy.

## SCENE 03 — FIXED-SIZE CHUNKING

**Narration reference:** The explanation of dividing text based on a fixed number of tokens or characters.

**Visual type:** Animated text segmentation.

**Visual action:**

1. Show one continuous paragraph.
2. Place evenly spaced boundaries across the text.
3. Divide it into similarly sized blocks.
4. Label each block Chunk 1, Chunk 2 and Chunk 3.
5. Show that the boundaries follow a fixed size rather than document headings.

**On-screen text:**

`FIXED-SIZE CHUNKING`

`FIXED LENGTH`

**Transition:** Show the fixed boundary cutting through a sentence, if that is the example used in the narration.

## SCENE 04 — RECURSIVE CHUNKING

**Narration reference:** The explanation of splitting text using a hierarchy of separators.

**Visual type:** Step-by-step segmentation animation.

**Visual action:**

1. Start with a complete document.
2. Show larger structural separators first, such as paragraph breaks.
3. If a section is still too large, split it further into smaller sections.
4. Show the splitting process continuing only where necessary.
5. Keep the resulting chunks visually distinct.

**On-screen text:**

`RECURSIVE CHUNKING`

`LARGE SECTION → SMALLER SECTION`

**Important:** Do not depict recursive chunking as random splitting.

**Transition:** Move to a structured document layout.

## SCENE 05 — STRUCTURE-AWARE CHUNKING

**Narration reference:** The explanation of using document structure such as headings, sections and paragraphs.

**Visual type:** Document structure animation.

**Visual action:**

1. Show a handbook page containing a title, heading, subheading and paragraph.
2. Highlight the heading.
3. Draw a boundary around its related paragraph.
4. Create a chunk that preserves the heading and associated content.
5. Repeat for the next section.

**On-screen text:**

`STRUCTURE-AWARE CHUNKING`

`HEADING + RELATED CONTENT`

**Transition:** Move to a semantic text comparison.

## SCENE 06 — SEMANTIC CHUNKING

**Narration reference:** The explanation of identifying boundaries based on changes in meaning or topic.

**Visual type:** Semantic grouping animation.

**Visual action:**

1. Show a series of sentences.
2. Highlight sentences discussing one topic.
3. Change the visual emphasis when the topic changes.
4. Group related sentences together.
5. Show a new chunk beginning at the topic transition.

Use a fictional example with two clearly different topics.

**On-screen text:**

`SEMANTIC CHUNKING`

`GROUP BY MEANING`

**Important:** Do not portray semantic chunking as simply grouping identical keywords.

## SCENE 07 — STRATEGY COMPARISON

**Narration reference:** The recap or comparison of chunking strategies.

**Visual type:** Four-panel comparison.

**Visual action:**

Display four separate panels:

1. Fixed-size — evenly sized sections.
2. Recursive — hierarchical splitting.
3. Structure-aware — document headings and sections.
4. Semantic — topic-based boundaries.

Keep each strategy visually distinct.

**On-screen text:**

`FIXED-SIZE`

`RECURSIVE`

`STRUCTURE-AWARE`

`SEMANTIC`

**Transition:** Zoom into one chunk and introduce its numerical representation in Script 05.

---

# SCRIPT 05 — EMBEDDINGS: TOKENS TO VECTORS

**Learning objective:** Clearly demonstrate the transformation from text to tokens, token IDs, embedding vectors and sentence-level representations.

**Special instruction:** This episode has a detailed conceptual sequence. Do not skip steps or replace the explanation with a single text-to-vector animation.

## SCENE 01 — WHY TEXT NEEDS A NUMERICAL REPRESENTATION

**Narration reference:** The opening explanation of converting text into a form that an embedding model can process.

**Visual type:** Text-to-number animation.

**Visual action:**

1. Show a document chunk on screen.
2. Display the sentence from the audio.
3. Show a computer interface receiving the sentence.
4. Animate the sentence entering a processing pipeline.
5. Show the text moving towards a tokenizer.

**On-screen text:**

`TEXT`

`NUMERICAL REPRESENTATION`

**Transition:** Zoom into the tokenizer.

## SCENE 02 — TOKENIZATION

**Narration reference:** The explanation that tokenization divides text into smaller units called tokens.

**Visual type:** Text segmentation animation.

**Visual action:**

1. Display the exact sentence used in the narration.
2. Split it into tokens in sequence.
3. Show each token as a separate block.
4. If the narration explains that tokens are not always complete words, demonstrate one word splitting into smaller subword units.
5. Keep the complete sentence and token pieces visible together.

**On-screen text:**

`TOKENIZATION`

`TEXT → TOKENS`

`A TOKEN IS NOT ALWAYS A COMPLETE WORD`

**Important:** Any exact token split shown must come from the tokenizer used in the lesson, or be explicitly labelled illustrative.

## SCENE 03 — TOKEN IDs

**Narration reference:** The explanation that each token is associated with a numerical identification value.

**Visual type:** Numerical mapping animation.

**Visual action:**

1. Keep the token pieces on screen.
2. Add a corresponding numerical ID beside each token.
3. Animate the token and its ID connecting.
4. Highlight one token and its associated ID.
5. Show the same relationship for the other tokens.

**On-screen text:**

`TOKEN`

`TOKEN ID`

`TOKEN → TOKEN ID`

**Important:** Use actual token IDs if this is connected to the Python demonstration. Do not invent numerical IDs.

## SCENE 04 — TOKEN ID IS ONLY AN IDENTIFIER

**Narration reference:** The clarification that token IDs identify tokens but do not themselves contain the complete meaning.

**Visual type:** Conceptual comparison.

**Visual action:**

1. Show a token and its numerical ID.
2. Display an identification-card visual.
3. Highlight the ID as a lookup identifier.
4. Do not display a dictionary definition inside the ID.
5. Show a question mark leading to the next stage.

**On-screen text:**

`TOKEN ID = IDENTIFIER`

`NOT THE FULL MEANING`

**Transition:** Introduce the embedding layer.

## SCENE 05 — EMBEDDING VECTORS

**Narration reference:** The explanation that token IDs are mapped to numerical vectors.

**Visual type:** Technical animation.

**Visual action:**

1. Show a token ID entering an embedding layer.
2. Show the layer producing a vector.
3. Display an illustrative vector such as:

`[0.12, -0.34, 0.87, ...]`

4. Label the output Embedding Vector.
5. Keep the token, token ID and vector visible together.

**On-screen text:**

`TOKEN → TOKEN ID → EMBEDDING VECTOR`

**Important:** Mark displayed decimal values as illustrative. Do not present them as actual model output.

## SCENE 06 — CONTEXTUAL REPRESENTATION

**Narration reference:** If the audio explains how surrounding words influence contextual representations, including the example of the word bank.

**Visual type:** Split-screen contextual example.

**Visual action:**

Left panel:

`I went to the bank to deposit money.`

Show a financial bank visual.

Right panel:

`I sat near the bank of the river.`

Show a riverbank visual.

Highlight the word `bank` in both sentences.

Then show that the surrounding context differs.

If the narration explains contextual token representations, show the representation being processed with surrounding words rather than showing a fixed vector for the word in every context.

**On-screen text:**

`SAME WORD`

`DIFFERENT CONTEXT`

`CONTEXTUAL REPRESENTATION`

**Important:** Do not imply that every embedding API exposes the exact internal token-level representations shown in the animation. The animation should illustrate the general transformer-based concept being taught.

## SCENE 07 — SENTENCE EMBEDDINGS

**Narration reference:** The explanation of producing a fixed-size vector for a complete sentence or text chunk.

**Visual type:** Vector aggregation animation.

**Visual action:**

1. Show the token-level representations.
2. Move them into a sentence representation stage.
3. Show a pooling or special representation stage only as described in the narration.
4. Produce one fixed-size vector for the complete sentence.
5. Label it Sentence Embedding.

**On-screen text:**

`TOKEN REPRESENTATIONS`

`POOLING / SENTENCE REPRESENTATION`

`SENTENCE EMBEDDING`

**Important:** Do not imply that all embedding models use precisely the same pooling implementation.

## SCENE 08 — VECTOR SPACE

**Narration reference:** The explanation that vectors exist in a numerical space and semantically related sentences can be relatively close.

**Visual type:** Conceptual 2D vector-space animation.

**Visual action:**

1. Show several text chunks.
2. Transform them into abstract vectors.
3. Represent them as points in a simplified 2D space.
4. Place semantically related sentences relatively close together.
5. Place unrelated sentences farther apart.
6. Label the diagram as a conceptual illustration.

**On-screen text:**

`VECTOR SPACE`

`SEMANTICALLY RELATED TEXT`

`CONCEPTUAL ILLUSTRATION — REAL EMBEDDINGS ARE HIGH-DIMENSIONAL`

**Important:** Do not assign human-readable meanings to individual vector dimensions.

## SCENE 09 — EMBEDDINGS IN THE RAG PIPELINE

**Narration reference:** The explanation of generating embeddings for document chunks and user queries.

**Visual type:** Two-lane RAG diagram.

**Visual action:**

Upper lane:

`DOCUMENT → CHUNKS → EMBEDDING MODEL → DOCUMENT VECTORS`

Lower lane:

`USER QUERY → EMBEDDING MODEL → QUERY VECTOR`

Show both sets of vectors moving towards the retrieval stage.

Highlight that the document and query embeddings must use a compatible embedding configuration.

**On-screen text:**

`DOCUMENT EMBEDDINGS`

`QUERY EMBEDDING`

`VECTOR RETRIEVAL`

**Transition:** The query vector moves towards the stored vectors, introducing cosine similarity.

---

# SCRIPT 06 — COSINE SIMILARITY

**Learning objective:** Explain why vector similarity is needed, how cosine similarity compares vector directions and why similarity is used during semantic retrieval.

## SCENE 01 — WHY SIMILARITY SEARCH IS NEEDED

**Narration reference:** The opening explanation of finding relevant information from stored embeddings.

**Visual type:** Query and document comparison animation.

**Visual action:**

1. Show a user query.
2. Show multiple document chunks.
3. Display their corresponding vector representations.
4. Show that the system must identify which stored vectors are relevant to the query.
5. Highlight the need for a similarity calculation.

**On-screen text:**

`QUERY VECTOR`

`DOCUMENT VECTORS`

`FIND THE MOST RELEVANT MATCHES`

**Transition:** Zoom into a 2D coordinate plane.

## SCENE 02 — VECTOR DIRECTION

**Narration reference:** The explanation of vectors and the direction they represent.

**Visual type:** 2D mathematical animation.

**Visual action:**

1. Draw a clean coordinate plane.
2. Draw two vectors starting from the origin.
3. Use arrowheads to show their directions.
4. Display the angle between them.
5. Highlight the angle as the important measurement for cosine similarity.

**On-screen text:**

`VECTOR A`

`VECTOR B`

`ANGLE (θ)`

**Important:** Label the drawing as a simplified 2D illustration of high-dimensional vectors.

## SCENE 03 — COSINE SIMILARITY

**Narration reference:** The explanation of cosine similarity.

**Visual type:** Mathematical animation.

**Visual action:**

1. Keep two vectors visible.
2. Highlight the angle between them.
3. Reveal the cosine similarity formula only when the narration introduces it:

`cos(θ) = (A · B) / (||A|| × ||B||)`

4. Highlight the dot product.
5. Highlight the vector magnitudes.
6. Show the denominator and final cosine calculation in the order spoken.

**On-screen text:**

`COSINE SIMILARITY`

`COMPARE VECTOR DIRECTIONS`

**Important:** Preserve the mathematical formula accurately.

## SCENE 04 — SIMILAR AND UNRELATED VECTORS

**Narration reference:** The explanation of how vector angles relate to similarity.

**Visual type:** Side-by-side comparison.

**Visual action:**

Create three separate examples:

1. Two vectors pointing in nearly the same direction.
2. Two vectors with a larger angle between them.
3. Two vectors pointing in opposite directions.

Show the corresponding cosine relationship conceptually.

**On-screen text:**

`SMALL ANGLE`

`LARGER ANGLE`

`OPPOSITE DIRECTIONS`

Do not fabricate numerical scores unless they come from an actual calculation in the narration or code.

## SCENE 05 — PYTHON OR NUMERICAL DEMONSTRATION

**Narration reference:** If the script contains a mathematical or Python example.

**Visual type:** Actual VS Code recording.

**Visual action:**

1. Open the exact Python file used in the lesson.
2. Reveal the vector definitions as narrated.
3. Highlight the vector variables.
4. Reveal the cosine calculation line.
5. Highlight the dot product and norm calculation separately if present.
6. Run the code.
7. Show the actual result.
8. Keep the output visible while the narration interprets it.

**Important:** Use the exact lesson implementation and actual output. Do not invent a score or change the example values.

## SCENE 06 — COSINE SIMILARITY IN RAG

**Narration reference:** The explanation of using similarity between query and document embeddings.

**Visual type:** Full RAG retrieval animation.

**Visual action:**

1. Show the user query becoming a query vector.
2. Show stored document vectors in a database.
3. Compare the query vector with document vectors.
4. Highlight the more relevant candidates.
5. Move the selected document chunks towards the retrieval stage.

**On-screen text:**

`QUERY EMBEDDING`

`COSINE SIMILARITY`

`RELEVANT DOCUMENT CHUNKS`

**Important:** Similarity is a retrieval signal, not proof that a document is factually correct.

**Transition:** Zoom into the storage layer, introducing Script 07.

---

# SCRIPT 07 — VECTOR DATABASES AND ANN

**Learning objective:** Explain why vector databases are needed, what they store and how Approximate Nearest Neighbor search helps find similar vectors efficiently.

## SCENE 01 — THE STORAGE PROBLEM

**Narration reference:** The opening question about where document embeddings are stored and retrieved.

**Visual type:** Scale animation.

**Visual action:**

1. Show a small collection of document chunks.
2. Convert each chunk into a vector.
3. Gradually increase the number of vectors on screen.
4. Show a large collection of stored vectors.
5. Display a user query approaching the collection.
6. Pause to introduce the storage and search problem.

**On-screen text:**

`DOCUMENT EMBEDDINGS`

`VECTOR COLLECTION`

**Transition:** Show a basic search process scanning the collection.

## SCENE 02 — WHY A VECTOR DATABASE?

**Narration reference:** The explanation of why ordinary manual storage and comparison are not sufficient for large-scale retrieval.

**Visual type:** Comparison animation.

**Visual action:**

Left side:
- Show a basic list of stored vectors.
- Animate a query comparing against each stored vector sequentially.
- Keep the illustration conceptual.

Right side:
- Show a vector database.
- Show a search request entering its retrieval interface.
- Show relevant candidate vectors being returned.

**On-screen text:**

`NAIVE VECTOR SCAN`

`VECTOR DATABASE`

**Important:** Do not display invented speed improvements or performance figures.

**Transition:** Zoom into the vector database.

## SCENE 03 — WHAT DOES A VECTOR DATABASE STORE?

**Narration reference:** The explanation of stored vectors and their associated information.

**Visual type:** Structured data animation.

**Visual action:**

Show one document chunk becoming a structured database record.

Display fields:

`ID`

`TEXT`

`EMBEDDING`

`METADATA`

Show the record entering a collection.

Repeat with two additional records.

**On-screen text:**

`VECTOR DATABASE RECORD`

**Important:** The fields shown must match the database configuration used in the actual project.

## SCENE 04 — INTRODUCING CHROMA

**Narration reference:** If the narration introduces Chroma as the vector database used in the project.

**Visual type:** Actual screen recording + architecture diagram.

**Visual action:**

1. Open the project's vector-store implementation.
2. Show the Chroma import and collection setup only when discussed.
3. Open the actual database collection if available.
4. Show stored document records.
5. Highlight the text, embedding and metadata fields.
6. Show a real collection query if implemented.

**On-screen text:**

`CHROMA`

`COLLECTION`

`VECTOR STORAGE`

**Important:** Do not fabricate record counts or collection output.

## SCENE 05 — INTRODUCING ANN

**Narration reference:** The explanation of Approximate Nearest Neighbor search.

**Visual type:** Technical search animation.

**Visual action:**

1. Show a large vector space with many stored points.
2. Highlight a query point.
3. First show the conceptual challenge of finding the nearest candidates across a large collection.
4. Introduce a search structure that helps locate promising nearby candidates without requiring an exhaustive exact comparison in every case.
5. Animate a search path moving through the structure.
6. Highlight the candidate vectors returned.

**On-screen text:**

`APPROXIMATE NEAREST NEIGHBOR`

`ANN`

`SEARCH EFFICIENTLY`

**Important:** Do not claim ANN always returns the mathematically exact nearest neighbors. Do not invent a specific index implementation unless the narration identifies it.

## SCENE 06 — EXACT SEARCH VS APPROXIMATE SEARCH

**Narration reference:** If the narration compares exact and approximate nearest-neighbor search.

**Visual type:** Side-by-side comparison.

**Visual action:**

Left:
- Show an exhaustive comparison against all stored vectors.
- Label it Exact Search.

Right:
- Show a search path exploring a smaller candidate region.
- Label it Approximate Search.

Use a conceptual diagram rather than claiming a fixed percentage of vectors are checked.

**On-screen text:**

`EXACT NEAREST NEIGHBOR`

`APPROXIMATE NEAREST NEIGHBOR`

**Transition:** A set of retrieved candidates appears, leading to Top-K.

---

# SCRIPT 08 — TOP-K AND THRESHOLDING

**Learning objective:** Explain how many documents are retrieved and how similarity thresholds can filter weak matches.

## SCENE 01 — TOO MANY RETRIEVED DOCUMENTS

**Narration reference:** The opening problem of retrieving relevant information from many stored chunks.

**Visual type:** Retrieval animation.

**Visual action:**

1. Show a user query.
2. Show a vector database containing many document chunks.
3. Animate the database returning a ranked list.
4. Show the list expanding with multiple results.
5. Highlight the need to control how many results are returned.

**On-screen text:**

`RETRIEVAL RESULTS`

`HOW MANY CHUNKS SHOULD WE RETURN?`

**Transition:** Focus on the first few results.

## SCENE 02 — TOP-K RETRIEVAL

**Narration reference:** The explanation of Top-K and selecting the first K retrieved results.

**Visual type:** Ranked list animation.

**Visual action:**

1. Display a ranked result list.
2. Show multiple document chunks with their rank positions.
3. Highlight the first K results based on the K value used in the narration.
4. Dim the remaining results.
5. Show the selected chunks moving into the context stage.

**On-screen text:**

`TOP-K RETRIEVAL`

`K = NUMBER OF RESULTS REQUESTED`

If the narration uses a numerical example, use the exact same value and number of displayed results.

**Important:** Top-K controls the requested number of results; it does not guarantee every returned result is relevant.

## SCENE 03 — TOO FEW VS TOO MANY RESULTS

**Narration reference:** The explanation of how choosing K affects retrieval.

**Visual type:** Comparison animation.

**Visual action:**

Left panel:
- Show a small K value.
- Only a few document chunks are selected.
- Visually demonstrate that useful information could be missed if the selection is too narrow.

Right panel:
- Show a larger K value.
- More chunks enter the context area.
- Show that some additional chunks may be less relevant.

**On-screen text:**

`TOO FEW RESULTS`

`TOO MANY RESULTS`

**Important:** Do not invent a universally optimal K value.

## SCENE 04 — SIMILARITY THRESHOLD

**Narration reference:** The explanation of setting a minimum similarity or maximum distance condition.

**Visual type:** Score filtering animation.

**Visual action:**

1. Show a ranked retrieval list with actual scores if the narration uses a numerical example.
2. Introduce a horizontal threshold line.
3. Move results through a filtering gate.
4. Keep results that satisfy the configured threshold.
5. Remove results that do not satisfy it.
6. Show the remaining candidates.

**On-screen text:**

`SIMILARITY THRESHOLD`

`KEEP QUALIFYING RESULTS`

**Important:** The direction of the comparison must match the metric being used. Similarity scores and distance scores do not necessarily have the same interpretation.

## SCENE 05 — TOP-K VS THRESHOLD

**Narration reference:** The explanation of the difference between Top-K and threshold filtering.

**Visual type:** Side-by-side technical comparison.

**Visual action:**

Left panel:
- Show Top-K selecting a fixed number of ranked results.

Right panel:
- Show thresholding selecting results that meet a configured score condition.

Bring both panels together to show that they can be used together when the retrieval design requires it.

**On-screen text:**

`TOP-K = HOW MANY?`

`THRESHOLD = HOW GOOD A MATCH?`

Only use this wording if it accurately reflects the narration's explanation.

**Transition:** Show a keyword-based search result appearing alongside vector search, introducing Script 09.

---

# SCRIPT 09 — HYBRID SEARCH, BM25 AND METADATA

**Learning objective:** Explain the limitations of relying on only one retrieval method and demonstrate how keyword search, vector search and metadata filtering can work together.

## SCENE 01 — THE LIMITATION OF ONE SEARCH METHOD

**Narration reference:** The opening explanation of cases where semantic search or keyword search alone may miss relevant information.

**Visual type:** Search comparison animation.

**Visual action:**

1. Show a user asking a question containing a specific policy code or technical term.
2. Show a semantic search panel.
3. Show a keyword search panel.
4. Highlight how the two methods can retrieve different candidate documents.
5. Avoid claiming that one method always wins.

**On-screen text:**

`SEMANTIC SEARCH`

`KEYWORD SEARCH`

**Transition:** Zoom into keyword search.

## SCENE 02 — KEYWORD SEARCH AND BM25

**Narration reference:** The explanation of BM25 and matching important query terms.

**Visual type:** Document highlighting animation.

**Visual action:**

1. Show a query containing a few important words.
2. Display three document passages.
3. Highlight exact matching terms inside the documents.
4. Show a ranked list of documents produced by keyword retrieval.
5. Introduce BM25 as the ranking method only when spoken.

**On-screen text:**

`BM25`

`KEYWORD-BASED RETRIEVAL`

**Important:** Do not explain BM25's formula or internal scoring details unless they are present in the narration.

## SCENE 03 — SEMANTIC / VECTOR SEARCH

**Narration reference:** The explanation of using embedding similarity to retrieve conceptually related content.

**Visual type:** Vector search animation.

**Visual action:**

1. Show the same user query.
2. Convert it into a query vector.
3. Show the document vectors.
4. Highlight semantically related passages even when the exact wording differs.
5. Display the returned candidate list.

**On-screen text:**

`DENSE VECTOR RETRIEVAL`

`SEMANTIC SIMILARITY`

**Transition:** Bring the two retrieval paths side by side.

## SCENE 04 — HYBRID SEARCH

**Narration reference:** The explanation of combining keyword and vector retrieval.

**Visual type:** Detailed dual-path architecture animation.

**Visual action:**

1. Place the user query at the top.
2. Split it into two parallel retrieval paths.
3. Left path: BM25 keyword search.
4. Right path: dense vector search.
5. Show each path returning its own ranked candidate list.
6. Bring both lists into a combined retrieval stage.
7. If the narration explains RRF, show a fusion component and label it Reciprocal Rank Fusion.
8. Show the combined results moving forward.

**On-screen text:**

`BM25 SEARCH`

`VECTOR SEARCH`

`HYBRID RETRIEVAL`

`RRF` — only if discussed.

**Important:** Keep the two search methods visually distinct. Do not show fusion before the narration introduces it.

## SCENE 05 — METADATA FILTERING

**Narration reference:** The explanation of using metadata to narrow the search space.

**Visual type:** Database filtering animation.

**Visual action:**

1. Show stored document chunks.
2. Display metadata fields beside them.
3. Use only fields introduced in the audio, such as:
   - `source`
   - `page`
   - `department`
   - `document_type`
4. Show a user query with a relevant filter condition.
5. Apply the filter before or during retrieval according to the implementation being taught.
6. Show only eligible records remaining.

**On-screen text:**

`METADATA`

`FILTER`

`ELIGIBLE DOCUMENTS`

**Important:** Do not imply metadata filtering is a replacement for proper authorization and access control.

## SCENE 06 — COMBINING RETRIEVAL SIGNALS

**Narration reference:** The recap of hybrid retrieval and metadata filtering.

**Visual type:** Full retrieval pipeline.

**Visual action:**

Show the complete process:

`USER QUERY`

↓

`METADATA FILTER`

↓

`BM25 + VECTOR SEARCH`

↓

`COMBINED CANDIDATES`

↓

`RELEVANT RESULTS`

Use the actual order described in the narration. If metadata filtering is applied at a different stage in the implementation, match the actual system.

**Transition:** The combined candidate list moves into a reranking stage.

---

# SCRIPT 10 — RERANKING AND CONTEXT ASSEMBLY

**Learning objective:** Explain why initial retrieval results may need reordering and how selected chunks are prepared as context for generation.

## SCENE 01 — THE INITIAL RETRIEVAL RESULTS

**Narration reference:** The opening explanation that retrieved results are not necessarily in the ideal final order.

**Visual type:** Ranked document list.

**Visual action:**

1. Show a user query.
2. Show a retrieval system returning several document chunks.
3. Display the initial ranked list.
4. Highlight that the first-stage results are candidate documents.
5. Show a few relevant and less relevant candidates mixed in the list.

**On-screen text:**

`INITIAL RETRIEVAL`

`CANDIDATE DOCUMENTS`

**Important:** Use a conceptual example unless the narration provides actual retrieved results.

**Transition:** Introduce a second scoring stage.

## SCENE 02 — WHAT IS RERANKING?

**Narration reference:** The explanation of reranking retrieved candidates based on their relevance to the query.

**Visual type:** Animated two-stage retrieval diagram.

**Visual action:**

1. Show the user query entering the first-stage retriever.
2. Show the candidate document list.
3. Move the candidates into a second component labelled Reranker.
4. Show the reranker comparing the query with each candidate.
5. Display the revised ranking.
6. Highlight the change in order.

**On-screen text:**

`FIRST-STAGE RETRIEVAL`

`RERANKER`

`FINAL RANKING`

**Important:** Do not confuse reranking with the initial vector search. Make the two stages visually separate.

## SCENE 03 — CROSS-ENCODER OR RERANKING MODEL

**Narration reference:** If the narration introduces a cross-encoder or a specific reranking model.

**Visual type:** Technical architecture animation.

**Visual action:**

1. Show the query and one candidate document entering a reranking model together.
2. Show a relevance score being produced.
3. Repeat for the other candidates.
4. Show the candidates being sorted according to the new scores.
5. If the narration explains the difference between bi-encoder retrieval and cross-encoder reranking, show two separate diagrams.

**On-screen text:**

`QUERY + DOCUMENT`

`RERANKING MODEL`

`RELEVANCE SCORE`

Only display a cross-encoder label if the audio explicitly introduces it.

## SCENE 04 — BEFORE AND AFTER RERANKING

**Narration reference:** The comparison of original retrieval order and improved ranking.

**Visual type:** Side-by-side comparison.

**Visual action:**

Left panel:

`BEFORE RERANKING`

Show the original candidate order.

Right panel:

`AFTER RERANKING`

Show the revised order.

Animate the document cards changing position.

Use the exact sample ranking from the narration if one is given. Otherwise use neutral illustrative document labels and clearly mark the ranking as conceptual.

**Important:** Do not invent benchmark scores or claim a specific accuracy improvement.

## SCENE 05 — CONTEXT ASSEMBLY

**Narration reference:** The explanation of selecting and preparing retrieved chunks before sending them to the language model.

**Visual type:** Detailed context construction animation.

**Visual action:**

1. Show the final ranked candidate chunks.
2. Select the chunks that will be passed forward.
3. Arrange them into one context panel.
4. Show the original user question above the context.
5. Show the source information associated with each selected chunk.
6. Display the assembled context as a structured input.
7. Move the context towards the generation stage.

**On-screen text:**

`USER QUESTION`

`SELECTED CHUNKS`

`SOURCE INFORMATION`

`ASSEMBLED CONTEXT`

**Important:** Do not add prompt construction or citation-generation details unless the narration covers them.

## SCENE 06 — CONTEXT SIZE AND RELEVANCE

**Narration reference:** If the narration discusses limiting the amount of context or choosing the most useful retrieved passages.

**Visual type:** Context comparison animation.

**Visual action:**

1. Show a context panel containing many chunks.
2. Highlight the most relevant chunks.
3. Show the selected context being organized.
4. If the audio discusses token or context limits, represent the available context area as a bounded container.
5. Show that the selected passages must fit within the configured context budget.

**On-screen text:**

`RELEVANT CONTEXT`

`CONTEXT BUDGET`

Only use the context-budget visual if it matches the actual narration.

## SCENE 07 — HANDING CONTEXT TO GENERATION

**Narration reference:** The final explanation of how assembled context is passed to the LLM.

**Visual type:** Full RAG pipeline animation.

**Visual action:**

1. Show the original question.
2. Show the final ranked and selected document chunks.
3. Combine them into the context.
4. Move the context into the language model.
5. Show the answer being generated.
6. Keep the source chunks visible beside the answer if the narration mentions source evidence.

**On-screen text:**

`QUESTION + ASSEMBLED CONTEXT`

`GENERATION`

`ANSWER`

**Transition:** End with the complete first ten scripts' retrieval pipeline, ready for the next episode.

---

# 2. SCREEN RECORDING MASTER CHECKLIST

Use actual recordings for the following activities.

| Asset ID | Script | Application / File | Required recording |
|---|---|---|---|
| SR-01 | 01 | Browser / Chat UI | Ask the opening college timetable question |
| SR-02 | 02 | RAG architecture diagram | Show indexing, retrieval and generation |
| SR-03 | 03 | Browser | Upload the sample PDF |
| SR-04 | 03 | VS Code / parsing.py | Show actual text extraction code |
| SR-05 | 03 | Terminal | Show actual extracted text output |
| SR-06 | 04 | VS Code / chunking.py | Show the implemented chunking method if code is narrated |
| SR-07 | 04 | Terminal | Display actual generated chunks |
| SR-08 | 05 | VS Code / embeddings.py | Show the tokenizer and embedding implementation used in the lesson |
| SR-09 | 05 | Terminal | Display actual tokenization/vector output where safe and appropriate |
| SR-10 | 06 | VS Code | Show actual cosine similarity calculation if present in narration |
| SR-11 | 06 | Terminal | Display the actual similarity output |
| SR-12 | 07 | VS Code / vector_store.py | Show Chroma collection setup |
| SR-13 | 07 | Database inspection | Display actual stored records |
| SR-14 | 08 | VS Code / retrieval.py | Show Top-K and threshold configuration |
| SR-15 | 08 | Terminal | Show actual retrieval results |
| SR-16 | 09 | VS Code / retrieval.py | Show BM25 and vector retrieval implementation if narrated |
| SR-17 | 09 | Database / terminal | Show actual metadata and filtered results |
| SR-18 | 10 | VS Code / reranking.py | Show actual reranking code if narrated |
| SR-19 | 10 | VS Code / context_builder.py | Show actual context assembly code if narrated |
| SR-20 | 10 | Terminal | Display actual selected chunks and assembled context |

**Recording rule:** These are planned recording requirements. If a feature has not been implemented, do not fake the screen recording. Use an accurately labelled conceptual animation instead.

---

# 3. ANIMATION AND DIAGRAM MASTER LIST

| Asset ID | Script | Diagram / Animation | Main purpose |
|---|---|---|---|
| DG-01 | 01 | LLM without connected knowledge vs RAG | Explain the knowledge gap |
| DG-02 | 01 | RAG introduction | Introduce retrieval, augmentation and generation |
| DG-03 | 02 | Three-stage RAG architecture | Show indexing, retrieval and generation |
| DG-04 | 03 | Document ingestion pipeline | Show source documents entering the system |
| DG-05 | 03 | Parsing and extraction | Show PDF becoming extracted text |
| DG-06 | 03 | Text cleaning | Show raw and cleaned text |
| DG-07 | 04 | Chunking concept | Show one document becoming smaller chunks |
| DG-08 | 04 | Fixed-size chunking | Show equal-size segmentation |
| DG-09 | 04 | Recursive chunking | Show hierarchical splitting |
| DG-10 | 04 | Structure-aware chunking | Preserve headings and sections |
| DG-11 | 04 | Semantic chunking | Split based on topic changes |
| DG-12 | 05 | Tokenization | Show text becoming tokens |
| DG-13 | 05 | Token IDs | Map tokens to actual identifiers |
| DG-14 | 05 | Embedding vectors | Show numerical vector representation |
| DG-15 | 05 | Contextual embeddings | Explain surrounding context |
| DG-16 | 05 | Sentence embeddings | Show sentence-level vector generation |
| DG-17 | 06 | Cosine similarity | Show vector angle and formula |
| DG-18 | 07 | Vector database structure | Show IDs, text, embeddings and metadata |
| DG-19 | 07 | ANN search | Explain approximate nearest-neighbor retrieval |
| DG-20 | 08 | Top-K retrieval | Select the first K results |
| DG-21 | 08 | Threshold filtering | Filter results based on a score condition |
| DG-22 | 09 | BM25 keyword retrieval | Highlight matching query terms |
| DG-23 | 09 | Hybrid search | Combine keyword and vector retrieval |
| DG-24 | 09 | Metadata filtering | Filter records by metadata |
| DG-25 | 10 | Reranking | Reorder retrieved candidates |
| DG-26 | 10 | Context assembly | Organize selected chunks for generation |

---

# 4. ASSET GENERATION PROMPTS FOR HIGGSFIELD

Use these prompts when a scene requires a standalone animation. Do not use generated visuals to replace real code or application recordings.

## DG-03 — COMPLETE THREE-STAGE RAG ARCHITECTURE

Create a premium, technically accurate sixteen-by-nine educational motion graphic on a deep charcoal background. Show three connected stages: Indexing, Retrieval and Generation. Animate document files entering the indexing stage, moving through text extraction, chunking, embeddings and vector storage. Then animate a user query entering retrieval, relevant chunks being selected and the selected context moving into a language model. Finish with a grounded answer returning to a chat interface. Use white typography and restrained cyan highlights. Keep all labels readable. Do not introduce agents, tools or unrelated architecture.

## DG-07 — DOCUMENT CHUNKING

Show a fictional employee handbook as a continuous page of text. Divide it into three clearly separated sections labelled Chunk 1, Chunk 2 and Chunk 3. Use clean visual boundaries and a premium dark background. Keep the text visually readable but use placeholder content. Do not imply that all chunking methods create identical boundaries.

## DG-14 — EMBEDDING VECTORS

Show a text chunk entering a numerical embedding model and emerging as an abstract vector representation. Display a small illustrative vector with decimal values. Show another semantically related text becoming another vector. Place both in a simplified two-dimensional conceptual space. Add the visible disclaimer: "Conceptual illustration — real embeddings are high-dimensional." Do not assign meaning to individual vector dimensions.

## DG-17 — COSINE SIMILARITY

Create a clean two-dimensional coordinate plane with two vectors starting at the origin. Animate the angle between the vectors. Reveal the cosine similarity formula accurately. Show a smaller angle and a larger angle in separate panels. Use clear labels and avoid invented numerical scores. Make it suitable for a technical education video.

## DG-19 — APPROXIMATE NEAREST NEIGHBOR

Show a large conceptual vector space containing many points. Highlight a query vector. Demonstrate the difference between exhaustive comparison and a search structure that explores promising candidates to find approximate nearest neighbors. Do not claim exact results, specific index algorithms or fixed performance improvements. Use a clean educational diagram.

## DG-23 — HYBRID SEARCH

Show one user query splitting into two independent retrieval paths. The first path performs BM25 keyword retrieval and highlights exact matching terms. The second path performs dense vector retrieval and finds semantically related passages. Show both paths returning ranked candidate lists. If the narration covers RRF, combine the lists through a clearly labelled Reciprocal Rank Fusion component. Keep the two retrieval methods visually distinct.

## DG-25 — RERANKING

Show a query entering an initial retrieval system. Display several candidate document cards in an initial order. Pass the cards through a reranking model. Animate the cards changing order according to their relevance to the query. Clearly label the first-stage retrieval and second-stage reranking. Do not show fabricated scores or benchmark improvements.

---

# 5. FINAL TECHNICAL ACCURACY CHECKLIST

Before final editing, verify all of the following.

## Narration synchronization

- Every spoken sentence has a corresponding visual.
- No narration is skipped.
- No future concept is shown early.
- No visual introduces an explanation absent from the audio.
- All ten audio files are in the correct order.
- Final scene timings match the actual ElevenLabs recordings.

## RAG technical accuracy

- Indexing and query-time retrieval are shown as distinct processes.
- Document parsing is not confused with OCR.
- Chunking strategies are represented accurately.
- Token IDs are shown as identifiers, not semantic meanings.
- Embedding vectors are labelled as numerical representations.
- Contextual representations are not confused with every embedding API's sentence-level output.
- Cosine similarity is represented through vector direction and the correct formula.
- Vector databases are not portrayed as LLMs.
- ANN is not described as guaranteeing exact nearest neighbors.
- Top-K is not presented as a relevance guarantee.
- Similarity and distance threshold directions are not mixed up.
- BM25 and dense vector retrieval are shown as separate methods.
- Metadata filtering is not confused with access control.
- Reranking is shown as a second-stage process.
- Context assembly uses selected retrieved chunks rather than every stored document.

## Code and application accuracy

- All code comes from the actual project.
- Code is revealed in the order narrated.
- All terminal output is genuine.
- All displayed vector values and IDs are verified.
- Chroma collection details are actual.
- No API keys or private data are visible.
- Any unimplemented feature is labelled as a conceptual demonstration or pending recording.

---

# 6. FINAL HANDOFF INSTRUCTIONS FOR CLAUDE

You will receive two inputs:

1. This visual action script.
2. The ten finalized ElevenLabs narration scripts/audio files.

Your job is to convert this production plan into a complete, detailed, shot-by-shot visual production document.

Follow these instructions:

1. Inspect all ten narration scripts before preparing the final storyboard.
2. Match each visual scene to the exact spoken narration.
3. Preserve the original script titles and numbering.
4. Do not rewrite the Tanglish narration.
5. Do not invent additional narration.
6. Expand scenes wherever the audio introduces multiple distinct actions or explanations.
7. Do not force every episode into the same number of scenes.
8. Use actual audio duration to calculate timestamps.
9. Clearly distinguish real screen recordings, animations, diagrams, UI mock-ups and editorial transitions.
10. Specify the exact application, screen, file, code and output required for every practical demonstration.
11. Keep the Enterprise Knowledge Assistant project visually and technically consistent.
12. Use the same sample documents across demonstrations wherever applicable.
13. Provide exact on-screen text and labels.
14. Provide clear transition instructions.
15. Do not create generic AI visuals that fail to explain the narrated concept.
16. Do not use fabricated code execution, database output or model results.
17. Keep all technical terminology in English.
18. Do not add a quiz or new learning interaction unless it exists in the supplied narration.
19. Create the final output in the same detailed scene-by-scene style as the supplied LLM Video Generation Action Script sample.
20. The finished document must be executable by a video editor, screen-recording specialist and motion graphics designer without requiring them to guess what should appear on screen.

**FINAL OUTPUT REQUIRED:**

`BOT ACADEMY — RAG COURSE — VIDEO GENERATION ACTION SCRIPT — SCRIPTS 01 TO 10`

The output must be a complete visual production document, not a short summary, not a list of animation ideas and not a generic prompt.

END OF ACTION SCRIPT — SCRIPTS 01 TO 10.
