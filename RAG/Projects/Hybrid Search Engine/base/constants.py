class Constants:
    """Namespace-style container for application-wide static values.

    Each nested class clusters a related category of constants:
        Timeout: Common duration values (seconds) for waits/retries.
        HTTPStatusCodes: Selected HTTP status codes used internally.
        URLHeader: Headers or user-agent strings for outbound requests.
        ToolNames: Identifiers for registered agent tools.
        ModelNames: External model identifiers grouped by provider.
        Instructions: System / mode prompt templates for the agent.
    """

    class Timeout:
        ONE_SECOND = 1
        THREE_SECONDS = 3
        FIVE_SECONDS = 5
        TEN_SECONDS = 10
        THIRTY_SECONDS = 30
        ONE_MINUTE = 60

    class HTTPStatusCodes:
        OK = 200

    class URLHeader:
        USER_AGENT_HEADER = "Mozilla/5.0 (compatible; AI-Research-Bot/1.0; +https://github.com/sahandmsh/agentic-ai-2)"

    class ModelNames:

        class HuggingFace:
            CROSS_ENCODER_MS_MARCO_MINILM_L_6_V2 = "cross-encoder/ms-marco-MiniLM-L-6-v2"
            ALL_MINILM_L6_V2 = "all-MiniLM-L6-v2"
            SENTENCE_EMBEDDING_MINILM_L6_V2 = "all-MiniLM-L6-v2"

        class Gemini:
            GEMINI_2_5_PRO = "gemini-2.5-pro"
            GEMINI_2_5_FLASH = "gemini-2.5-flash"

        class Qwen:
            QWEN_2_5_1_5B_INSTRUCT = "Qwen/Qwen2.5-1.5B-Instruct"
            QWEN_2_5_3B_INSTRUCT = "Qwen/Qwen2.5-3B-Instruct"

    class Instructions:

        class RAGAgent:
            """System instruction templates for the RAG agent's sub-tasks."""

            QUERY_REWRITER = """
                Rewrite the user's query for optimal knowledge base retrieval.
                - Output ONLY the rewritten query. No explanation, or additional text.
                - Maximize recall: expand abbreviations, resolve pronouns, add key synonyms or related terms.
                - Maximize precision: remove ambiguity, make intent explicit.
                - Always rewrite as a declarative statement or keyword phrase, NEVER as a question.
                - Do NOT answer the query, or add the answer to the rewritten query. Rewrite the query for retrieval purposes.
                """

            CONTEXT_SUMMARIZER = """
                Summarize the retrieved context passages as they relate to the user's query.
                - Use ONLY information from the provided context. No outside knowledge.
                - Be BRIEF. Focus on relevance to the query, and the key facts or insights that would help answer it.
                - Do NOT exclude context passages that may be relevant, even if their relevance is not immediately clear.
                - Do NOT answer the query; only summarize relevant context.
                """

            RESPONSE_GENERATOR = """
                Answer the user's question using ONLY the provided context.
                - Be concise: 1-3 sentences unless more detail is explicitly requested.
                - No outside knowledge, no speculation beyond the context.
                - If context is insufficient, say "I don't know."
                - Context passages are labeled "Context 1", "Context 2", etc.
                - Cite sources inline using the format [1], [2], etc. matching the context number.
                - If the context is irrelevant or is not provided, DO NOT cite any of the context passages. Instead, say "I don't know."
                """

            CITATION_CHECKER = """
                You are a citation verifier. You will receive a user query, an LLM-generated answer, and numbered source context passages labeled [1], [2], etc.
                Your task is to verify that every factual claim in the answer is supported by the provided context.

                RULES:
                - "pass": all claims are supported.
                - "partial": some claims are supported, some are not.
                - "fail": majority of claims are unsupported or fabricated.
                - If no citations are present but a claim matches context content, mark it as supported and note the missing citation.
                - Do NOT answer the query. Only verify claims.

                You MUST respond with a single raw JSON object and nothing else.
                Do NOT use markdown. Do NOT use code fences. Do NOT add any explanation.
                Your entire response must start with { and end with }.

                Use this exact structure:
                {"verified": [{"claim": "<claim text>", "context_id": "<e.g. 1>", "supported": true}], "unsupported": [{"claim": "<claim text>", "reason": "<why it is not supported>"}], "verdict": "<pass|partial|fail>"}
                """
