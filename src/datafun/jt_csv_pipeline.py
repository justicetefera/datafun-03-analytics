"""
justice_csv_pipeline.py - Custom CSV ETVL pipeline.

Author: Justice Tefera
Date: 2026-05

This file is my custom version of the instructor's CSV pipeline.
It practices key Python skills:

    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading CSV files using the csv module
    - keyword-only function arguments
    - error handling with raise
    - calculating statistics with the statistics module
    - writing results to a text file

My custom modifications include:
    - Using my own CSV file: justice_test_scores.csv
    - Adding a new statistic: range
    - Adding a custom verification rule (scores must be 0–100)
    - Writing a custom report header

Run from project root:

    uv run python -m jt_csv_pipeline
"""

import csv
import statistics
from pathlib import Path
from typing import Any

# === E: EXTRACT ===


def extract_csv_scores(*, file_path: Path, column_name: str) -> list[float]:
    """Extract numeric values from a CSV column."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    scores: list[float] = []

    with file_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None or column_name not in reader.fieldnames:
            raise KeyError(
                f"CSV missing expected column '{column_name}'. "
                f"Found columns: {reader.fieldnames}"
            )

        for row in reader:
            raw_value = (row.get(column_name) or "").strip()
            if not raw_value:
                continue
            try:
                scores.append(float(raw_value))
            except ValueError:
                continue

    return scores


# === T: TRANSFORM ===


def transform_scores_to_stats(*, scores: list[float]) -> dict[str, float]:
    """Calculate statistics from a list of floats."""
    if not scores:
        raise ValueError("No numeric values found for analysis.")

    return {
        "count": float(len(scores)),
        "min": min(scores),
        "max": max(scores),
        "mean": statistics.mean(scores),
        "stdev": statistics.stdev(scores) if len(scores) > 1 else 0.0,
        "range": max(scores) - min(scores),
    }


# === V: VERIFY ===


def verify_stats(*, stats: dict[str, float]) -> None:
    """Verify that the statistics dictionary is valid."""
    required = {"count", "min", "max", "mean", "stdev", "range"}
    missing = required - set(stats.keys())

    if missing:
        raise KeyError(f"Missing required stats keys: {sorted(missing)}")

    if stats["count"] <= 0:
        raise ValueError("Count must be positive.")

    if stats["min"] > stats["max"]:
        raise ValueError("Minimum cannot exceed maximum.")

    # Custom rule: scores must be between 0 and 100
    if stats["min"] < 0 or stats["max"] > 100:
        raise ValueError("Scores must be between 0 and 100.")


# === L: LOAD ===


def load_stats_report(*, stats: dict[str, float], out_path: Path) -> None:
    """Write statistics to a text file."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Justice's Custom Score Statistics Report\n")
        f.write("Analyzed student performance data.\n\n")
        f.write(f"Count: {int(stats['count'])}\n")
        f.write(f"Minimum: {stats['min']:.2f}\n")
        f.write(f"Maximum: {stats['max']:.2f}\n")
        f.write(f"Mean: {stats['mean']:.2f}\n")
        f.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
        f.write(f"Range: {stats['range']:.2f}\n")


# === FULL PIPELINE ===


def run_csv_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline."""
    logger.info("CSV PIPELINE: START")

    input_file = raw_dir / "justice_test_scores.csv"
    output_file = processed_dir / "justice_score_stats.txt"

    scores = extract_csv_scores(file_path=input_file, column_name="score")
    stats = transform_scores_to_stats(scores=scores)
    verify_stats(stats=stats)
    load_stats_report(stats=stats, out_path=output_file)

    logger.info("CSV PIPELINE: wrote %s", output_file)
    logger.info("CSV PIPELINE: END")
