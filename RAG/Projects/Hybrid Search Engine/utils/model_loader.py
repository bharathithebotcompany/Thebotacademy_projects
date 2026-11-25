from base.constants import Constants
from google import genai
from google.genai import types as genai_types
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import Callable
import datetime


class ModelLoader:
    """Utility class for loading various NLP and generative models.

    Attributes:
        None (stateless utility class).
    """

    def __init__(self):
        """Initialize the ModelLoader (currently stateless)."""
        pass

    def load_hf_tokenizer(
        self,
        hugging_face_token: str,
        tokenizer_model: str = Constants.ModelNames.HuggingFace.CROSS_ENCODER_MS_MARCO_MINILM_L_6_V2,
    ) -> AutoTokenizer:
        """Load a pretrained Hugging Face tokenizer.

        Args:
            hugging_face_token (str): Authentication token for private or gated Hugging Face models.
            tokenizer_model (str, optional): Model name or path. Defaults to cross-encoder/ms-marco-MiniLM-L-6-v2.

        Returns:
            AutoTokenizer: Pretrained tokenizer compatible with the specified model.
        """
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_model, token=hugging_face_token)
        return tokenizer

    def load_hf_cross_encoder(
        self,
        hugging_face_token: str,
        cross_encoder_model: str = Constants.ModelNames.HuggingFace.CROSS_ENCODER_MS_MARCO_MINILM_L_6_V2,
        max_length: int = 512,
    ) -> CrossEncoder:
        """Load a pretrained cross-encoder model for semantic reranking.

        Args:
            hugging_face_token (str): Authentication token for private or gated Hugging Face models.
            cross_encoder_model (str, optional): Model name or path. Defaults to cross-encoder/ms-marco-MiniLM-L-6-v2.
            max_length (int, optional): Maximum input length for the model. Defaults to 512.

        Returns:
            CrossEncoder: Reranking model for scoring query–passage pairs.
        """
        cross_encoder = CrossEncoder(
            cross_encoder_model, max_length=max_length, token=hugging_face_token
        )
        return cross_encoder

    def load_sentence_embedding_model(
        self,
        hugging_face_token: str,
        sentence_embedding_model: str = Constants.ModelNames.HuggingFace.SENTENCE_EMBEDDING_MINILM_L6_V2,
    ) -> SentenceTransformer:
        """Load a pretrained SentenceTransformer for text embedding.

        Args:
            hugging_face_token (str): Authentication token for private or gated Hugging Face models.
            sentence_embedding_model (str, optional): Model name or path. Defaults to all-MiniLM-L6-v2.

        Returns:
            SentenceTransformer: Bi-encoder model for embedding sentences or text chunks.
        """
        sentence_transformer = SentenceTransformer(
            sentence_embedding_model, token=hugging_face_token
        )
        return sentence_transformer

    def load_gemini_generative_model(
        self,
        google_api_key: str,
        config,
        model_name: str = Constants.ModelNames.Gemini.GEMINI_2_5_PRO,
    ) -> Callable[[str], str]:
        """Load a Gemini generative model for text generation.

        Args:
            google_api_key (str): API key for the Google Generative AI service.
            config: Model configuration object (e.g., temperature, max_output_tokens).
                    If the caller also passes `system_instructions` at generate-time, a new config
                    is derived from this base config with `system_instruction` overridden.
            model_name (str, optional): Name of the generative model. Defaults to Gemini 2.5 Pro.

        Returns:
            Callable[[str, str], str]: Function `generate(prompt, system_instructions="") -> str`
                that produces text for a given prompt.  Pass a non-empty `system_instructions`
                string to override the system instruction for that single call without
                mutating the base config.
        """
        client = genai.Client(api_key=google_api_key)

        def generate(prompt: str, system_instructions: str = "", config=config):
            date_time = f"[CURRENT DATE AND TIME: {datetime.datetime.now().strftime('%B %d, %Y %I:%M %p')}]\n"
            effective_config = config
            if system_instructions:
                config_with_provided_instructions = genai_types.GenerateContentConfig(
                    **{
                        **config.__dict__,
                        "system_instruction": system_instructions,
                    }
                )
                effective_config = config_with_provided_instructions
            response = client.models.generate_content(
                model=model_name,
                contents=date_time + prompt,
                config=effective_config,
            )
            return response.text

        return generate

    def load_hf_generative_model(
        self,
        hugging_face_token: str,
        model_name: str = Constants.ModelNames.Qwen.QWEN_2_5_1_5B_INSTRUCT,
        device: str = "cpu",
        temperature: float = 0.7,
        system_instructions: str = "",
    ) -> Callable[[str], str]:
        """Load a Hugging Face causal LM for text generation.

        Automatically selects MPS (Apple Silicon) or CPU device. Generates up to 500 new tokens per call.

        Args:
            hugging_face_token (str): Authentication token for private or gated Hugging Face models.
            model_name (str, optional): Model name or path. Defaults to Qwen 2.5 1.5B Instruct.
            device (str, optional): Device to load the model onto. Defaults to "cpu".
            temperature (float, optional): Sampling temperature for generation. Defaults to 0.7.
            system_instructions (str, optional): Default system instructions for generation. Defaults to "".

        Returns:
            Callable[[str], str]: Function `generate(prompt: str, system_instructions: str = "") -> str` that produces text
                using the loaded model and tokenizer.
        """
        tokenizer = self.load_hf_tokenizer(hugging_face_token, model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, token=hugging_face_token)
        model = model.to(device)

        def generate(prompt: str, system_instructions: str = system_instructions):
            date_time = f"[CURRENT DATE AND TIME: {datetime.datetime.now().strftime('%B %d, %Y %I:%M %p')}]\n"
            instructions_prefix = (
                f"System Instructions: {system_instructions}\n" if system_instructions else ""
            )
            inputs = tokenizer(f"{instructions_prefix}{date_time}{prompt}", return_tensors="pt")
            inputs = {k: v.to(device) for k, v in inputs.items()}
            input_len = inputs["input_ids"].shape[1]
            outputs = model.generate(**inputs, temperature=temperature)
            generated_tokens = outputs[0][input_len:]
            return tokenizer.decode(generated_tokens, skip_special_tokens=True)

        return generate
