"""
jt_text_pipeline.py - Custom Text ETVL pipeline.

Author: Justice Tefera
Date: 2026-05

    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading text files line by line
    - counting lines, words, characters, and custom metrics
    - keyword-only function arguments
    - error handling with raise
    - writing results to a text file

My custom modifications include:
    - Using my own text file: jt_sample_text.txt
    - Adding a new metric: average words per line
    - Adding a custom verification rule (line count must be > 0)
    - Writing a custom report header

Run from project root:

    uv run python -m jt_text_pipeline
"""

from pathlib import Path
from typing import Any

# === E: EXTRACT ===


def extract_lines(*, file_path: Path) -> list[str]:
    """Extract lines from a text file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        return f.readlines()


# === T: TRANSFORM ===


def transform_line_word_char_counts(*, lines: list[str]) -> dict[str, float]:
    """Calculate line, word, char counts + custom metric."""
    if not isinstance(lines, list):
        raise TypeError("Expected a list of strings for 'lines'.")

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        char_count += len(line)
        word_count += len(line.split())

    # Custom metric: average words per line
    avg_words = word_count / line_count if line_count > 0 else 0.0

    return {
        "lines": line_count,
        "words": word_count,
        "chars": char_count,
        "avg_words": avg_words,
    }


# === V: VERIFY ===


def verify_summary(*, summary: dict[str, float]) -> None:
    """Verify summary dictionary is valid."""
    required = ("lines", "words", "chars", "avg_words")

    for key in required:
        if key not in summary:
            raise KeyError(f"Missing summary key: {key}")

        if summary[key] < 0:
            raise ValueError(f"Invalid {key} count: {summary[key]}")

    # Custom rule: must have at least 1 line
    if summary["lines"] == 0:
        raise ValueError("Text file must contain at least one line.")


# === L: LOAD ===


def load_summary_report(*, summary: dict[str, float], out_path: Path) -> None:
    """Write summary to a text file."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Justice's Custom Text Summary Report\n")
        f.write("Analyzed text file statistics.\n\n")
        f.write(f"Lines: {summary['lines']}\n")
        f.write(f"Words: {summary['words']}\n")
        f.write(f"Characters: {summary['chars']}\n")
        f.write(f"Average Words per Line: {summary['avg_words']:.2f}\n")


# === FULL PIPELINE ===


def run_text_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline."""
    logger.info("JT TXT PIPELINE: START")

    input_file = raw_dir / "jt_sample_text.txt"
    output_file = processed_dir / "jt_text_summary.txt"

    lines = extract_lines(file_path=input_file)
    summary = transform_line_word_char_counts(lines=lines)
    verify_summary(summary=summary)
    load_summary_report(summary=summary, out_path=output_file)

    logger.info("JT TXT PIPELINE: wrote %s", output_file)
    logger.info("JT TXT PIPELINE: END")
