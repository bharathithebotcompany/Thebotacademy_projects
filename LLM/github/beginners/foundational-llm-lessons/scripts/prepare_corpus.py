"""Downloads and cleans 'Electricity for Boys' by J.S. Zerbe (Project Gutenberg #22766,
public domain) into a plain-text corpus for tokenization/pretraining notebooks.

Run once: `python scripts/prepare_corpus.py`
"""

import re
import urllib.request
from pathlib import Path

GUTENBERG_URL = "https://www.gutenberg.org/cache/epub/22766/pg22766.txt"
OUT_PATH = Path(__file__).resolve().parent.parent / "data" / "electricity_for_boys.txt"

START_MARKER = "*** START OF THE PROJECT GUTENBERG EBOOK ELECTRICITY FOR BOYS ***"
END_MARKER = "*** END OF THE PROJECT GUTENBERG EBOOK ELECTRICITY FOR BOYS ***"
CHAPTER_START = "CHAPTER I"
TRANSCRIBER_NOTE = "Transcriber's Note."


def download(url: str = GUTENBERG_URL) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")


def clean(raw_text: str) -> str:
    # Strip the Project Gutenberg license header/footer.
    start = raw_text.find(START_MARKER)
    end = raw_text.find(END_MARKER)
    body = raw_text[start + len(START_MARKER) : end]

    # Drop front matter (title page, table of contents, illustration list) --
    # the real narrative starts at "CHAPTER I".
    chapter_start = body.find(CHAPTER_START)
    body = body[chapter_start:]

    # Drop the transcriber's note box that trails the actual text.
    note_start = body.find(TRANSCRIBER_NOTE)
    if note_start != -1:
        box_start = body.rfind("+--", 0, note_start)
        body = body[: box_start if box_start != -1 else note_start]

    # Remove [Illustration: ...] captions -- they're not prose.
    body = re.sub(r"\[Illustration[^\]]*\]", "", body)

    # Collapse hyphenated line-wraps like "some-\nthing" -> "something".
    body = re.sub(r"-\n", "", body)

    # Collapse runs of 3+ blank lines down to 2 (paragraph break).
    body = re.sub(r"\n{3,}", "\n\n", body)

    return body.strip() + "\n"


def main():
    print(f"Downloading from {GUTENBERG_URL} ...")
    raw = download()
    text = clean(raw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text):,} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
