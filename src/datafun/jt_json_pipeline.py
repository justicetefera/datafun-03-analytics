"""
jaso_pipeline.py - Custom JSON ETVL pipeline.

Author: Justice Tefera
Date: 2026-05

This file is my custom version of the instructor's JSON pipeline.
It practices key Python skills:

    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading JSON files using the json module
    - walking JSON: dictionaries, lists, and nested structures
    - keyword-only function arguments
    - defensive programming for untrusted input
    - runtime type checking with isinstance()
    - writing results to a text file

My custom modifications include:
    - Using my own JSON file: jaso_people.json
    - Adding a new transformation: count people by country
    - Adding a custom verification rule (country names must be valid strings)
    - Writing a custom report header

Run from project root:

    uv run python -m jt.jaso_pipeline
"""

import json
from pathlib import Path
from typing import Any

# === E: EXTRACT ===


def extract_people_list(
    *, file_path: Path, list_key: str = "people"
) -> list[dict[str, Any]]:
    """Extract a list of dictionaries from a JSON file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        data: Any = json.load(f)

    if not isinstance(data, dict):
        raise TypeError("Expected JSON top-level object to be a dictionary.")

    value: Any = data.get(list_key, [])

    if not isinstance(value, list):
        raise TypeError(f"Expected {list_key!r} to be a list.")

    people_list: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            people_list.append(item)

    return people_list


# === T: TRANSFORM ===


def transform_count_by_country(
    *, people_list: list[dict[str, Any]], country_key: str = "country"
) -> dict[str, int]:
    """Count people by country."""
    counts: dict[str, int] = {}

    for person in people_list:
        country: Any = person.get(country_key, "Unknown")

        if not isinstance(country, str) or not country.strip():
            country = "Unknown"

        counts[country] = counts.get(country, 0) + 1

    return counts


# === V: VERIFY ===


def verify_country_counts(*, counts: dict[str, int]) -> None:
    """Verify that country counts are valid."""
    for country, count in counts.items():
        if not isinstance(country, str) or not country.strip():
            raise ValueError(f"Invalid country name: {country!r}")
        if count < 0:
            raise ValueError(f"Invalid count for country {country!r}: {count}")


# === L: LOAD ===


def load_country_report(*, counts: dict[str, int], out_path: Path) -> None:
    """Write country counts to a text file."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Justice's Custom JSON Country Report\n")
        f.write("Analyzed people grouped by country.\n\n")

        for country in sorted(counts):
            f.write(f"{country}: {counts[country]}\n")


# === FULL PIPELINE ===


def run_json_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline."""
    logger.info("JSON PIPELINE: START")

    input_file = raw_dir / "jaso_people.json"
    output_file = processed_dir / "json_people_by_country.txt"

    people_list = extract_people_list(file_path=input_file, list_key="people")
    country_counts = transform_count_by_country(
        people_list=people_list, country_key="country"
    )
    verify_country_counts(counts=country_counts)
    load_country_report(counts=country_counts, out_path=output_file)

    logger.info("JSON PIPELINE: wrote %s", output_file)
    logger.info("JSON PIPELINE: END")
