"""Tiny helper to build .ipynb files from a list of (cell_type, source) tuples.
Used by the build_notebook_*.py scripts -- not part of the taught curriculum."""

import json
import uuid


def make_notebook(cells):
    """cells: list of ("markdown"|"code", source_string)"""
    nb_cells = []
    for i, (cell_type, source) in enumerate(cells):
        cell = {
            "id": uuid.uuid4().hex[:8],
            "cell_type": cell_type,
            "metadata": {},
            "source": source.splitlines(keepends=True),
        }
        if cell_type == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
        nb_cells.append(cell)

    return {
        "cells": nb_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.13"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_notebook(path, cells):
    nb = make_notebook(cells)
    with open(path, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"Wrote {path} ({len(cells)} cells)")


def md(text):
    return ("markdown", text.strip() + "\n")


def code(text):
    return ("code", text.strip() + "\n")
