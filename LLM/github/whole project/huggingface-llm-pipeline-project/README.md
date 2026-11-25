# GPT-2 Text Generation CLI

A small Python project for exploring causal language generation with Hugging Face Transformers and PyTorch. It accepts a Hub model ID or a local model directory, tokenizes a prompt, and returns an autoregressive continuation.

## Quick start

Requires Python 3.10+. Use an activated virtual environment. On a CPU-only machine, the [PyTorch installer](https://pytorch.org/get-started/locally/) lets you choose a CPU wheel before installing the remaining requirements.

```bash
python -m pip install -r requirements.txt
python main.py "The best way to learn a new programming language is" --max-new-tokens 18
```

The default is [OpenAI GPT-2 on Hugging Face](https://huggingface.co/openai-community/gpt2). The first run downloads and caches the model. A greedy run returned the following text.

> The best way to learn a new programming language is to learn it from a beginner.
>
> The best way to learn a new programming language

The token limit can cut the continuation mid-sentence. GPT-2 is a base text-prediction model, and its output can be repetitive or incorrect.

## Options

```bash
python main.py "The archive contained" --model distilgpt2 --max-new-tokens 24 --sample --seed 42
python main.py "The telescope found" --model ./my-model --local-files-only --completion-only --max-new-tokens 24
```

| Option | Behavior |
| --- | --- |
| `--max-new-tokens` | Budget for generated tokens |
| `--max-length` or `--max_length` | Total budget including the prompt. With neither length option, the total budget is 50 |
| `--sample` and `--seed` | Enable sampling and set its seed |
| `--revision` | Select a specific Hub revision |
| `--local-files-only` | Resolve files from disk or the local cache |
| `--completion-only` | Print only the continuation |

Greedy decoding is the default. The CLI validates the prompt's token budget, checks a declared context limit, and reports model-loading errors on stderr.

See [LICENSE](LICENSE) for the project's license and the [model card](https://huggingface.co/openai-community/gpt2) for GPT-2's details.

CI checks installation, dependency compatibility, unit tests and CLI examples on Python 3.12 for each push and pull request. You can also run it from the Actions tab.
