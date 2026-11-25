"""Run a Hugging Face causal language model from the command line."""

from __future__ import annotations

import argparse
import sys

DEFAULT_MODEL = "openai-community/gpt2"


def positive_int(text: str) -> int:
    value = int(text)
    if value <= 0:
        raise argparse.ArgumentTypeError("expected a positive integer")
    return value


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", help="Text for the model to continue")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Hugging Face model ID or local model directory")
    length = parser.add_mutually_exclusive_group()
    length.add_argument("--max-new-tokens", type=positive_int, help="Budget for the continuation alone")
    length.add_argument("--max-length", "--max_length", type=positive_int, help="Total tokens including the prompt")
    parser.add_argument("--sample", action="store_true", help="Sample tokens instead of using greedy decoding")
    parser.add_argument("--seed", type=int, help="Random seed for sampling")
    parser.add_argument("--local-files-only", action="store_true", help="Use local or cached files")
    parser.add_argument("--revision", help="Optional Hugging Face branch, tag or commit")
    parser.add_argument("--completion-only", action="store_true", help="Print only the new text")
    args = parser.parse_args(argv)
    if not args.prompt.strip():
        parser.error("the prompt must contain text")
    if args.seed is not None and not 0 <= args.seed < 2**32:
        parser.error("--seed must be between 0 and 4294967295")
    return args


def continuation_budget(prompt_tokens: int, max_length: int, max_new_tokens: int | None) -> int:
    budget = max_new_tokens if max_new_tokens is not None else max_length - prompt_tokens
    if budget < 1:
        raise ValueError(
            f"The prompt occupies {prompt_tokens} tokens. Use --max-new-tokens or a larger --max-length."
        )
    return budget


def generate_text(
    prompt: str,
    model_name: str = DEFAULT_MODEL,
    max_length: int = 50,
    *,
    max_new_tokens: int | None = None,
    sample: bool = False,
    seed: int | None = None,
    local_files_only: bool = False,
    revision: str | None = None,
    completion_only: bool = False,
) -> str:
    """Continue a prompt using the model's native tokenizer and PyTorch generation."""
    if not prompt.strip():
        raise ValueError("The prompt must contain text")

    import torch
    from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, set_seed

    load_options = {"local_files_only": local_files_only, "trust_remote_code": False}
    if revision is not None:
        load_options["revision"] = revision
    tokenizer = AutoTokenizer.from_pretrained(model_name, **load_options)
    inputs = tokenizer(prompt, return_tensors="pt", padding=False, truncation=False, verbose=False)
    prompt_tokens = inputs["input_ids"].shape[1]
    if not prompt_tokens:
        raise ValueError("The tokenizer produced no input tokens")
    budget = continuation_budget(prompt_tokens, max_length, max_new_tokens)
    config = AutoConfig.from_pretrained(model_name, **load_options)
    if config.is_encoder_decoder:
        raise ValueError("Use a decoder-only causal language model")
    limit = getattr(config, "max_position_embeddings", None)
    if isinstance(limit, int) and prompt_tokens + budget > limit:
        raise ValueError(f"Prompt and continuation exceed the model's {limit}-token context window")

    model = AutoModelForCausalLM.from_pretrained(model_name, config=config, **load_options).eval()
    if seed is not None:
        set_seed(seed)
    padding = tokenizer.pad_token_id
    if padding is None:
        padding = tokenizer.eos_token_id
    with torch.inference_mode():
        sequences = model.generate(
            **inputs, max_new_tokens=budget, do_sample=sample, num_beams=1,
            num_return_sequences=1, return_dict_in_generate=False, pad_token_id=padding,
        )
    completion = tokenizer.decode(sequences[0, prompt_tokens:], skip_special_tokens=True)
    return completion if completion_only else prompt + completion


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        result = generate_text(
            args.prompt, args.model, args.max_length if args.max_length is not None else 50,
            max_new_tokens=args.max_new_tokens, sample=args.sample, seed=args.seed,
            local_files_only=args.local_files_only, revision=args.revision, completion_only=args.completion_only,
        )
    except (ImportError, OSError, RuntimeError, TypeError, ValueError) as exc:
        print(f"Could not generate text: {exc}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
