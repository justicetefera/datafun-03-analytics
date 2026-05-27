# Analytics

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

Python 3.14+ • MIT License

A professional Python analytics project demonstrating multi-format ETL (Extract–Transform–Load) pipelines.


This project processes real data files, generates structured outputs, and follows the conventions of modern Python development.

---

## Project Overview

Data analytics requires durable, real‑world skills that go far beyond simply running code. Analysts must be able to set up and maintain a clean development environment, read and interpret existing codebases, execute multi‑step pipelines, analyze and validate outputs, and confidently push their work to a shared repository where others can review, reproduce, and build upon it. These abilities form the foundation of professional analytical practice. This project is designed to strengthen those capabilities through hands‑on experience with a fully structured Python codebase, giving learners the opportunity to work with real data, troubleshoot issues, and develop the habits and workflows used by modern analytics teams.

In the age of generative AI, the most valuable skills remain grounded in **real work**:
- Setting up and activating a virtual environment
- Running Python modules with `python -m`
- Understanding ETL logic
- Processing multiple data formats
- Logging results
- Using Git and GitHub professionally

Each phase of this project mirrors the workflow of a real analytics team.

---

## This Project

This project illustrates a complete ETL pipeline system that processes raw data in four formats:

- **CSV** — numeric datasets and descriptive statistics
- **JSON** — hierarchical structured data
- **Text** — unstructured natural-language content
- **Excel (XLSX)** — spreadsheet data using `openpyxl`

The working example demonstrates a full, end-to-end pipeline.
Use it as a model to build your own custom pipelines.

## Clone the Repository
git clone https://github.com/username/datafun-03-analytics
cd datafun-03-analytics
code .

## Environment Setup
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
uvx pre-commit install

## Run Pre‑Commit
git add -A
uvx pre-commit run --all-files
git add -A
uvx pre-commit run --all-files

## Save Progress
git add -A
git commit -m "update"
git push -u origin main



---

## Choosing Your Data

Think about the raw data you want to process:

- What format is it? (CSV, JSON, TXT, XLSX)
- Is it static? (Use files stored in your project, not live streams)

Being able to read and process a wide variety of data files is essential in professional analytics.
Python is widely used because it makes building these pipelines clean, modular, and repeatable.

---

## Project-Specific Design Choices

### PyRight Type Checking Adjustments
Some PyRight checks are disabled for this project.

**Why:**
When working with raw data, types are often unknown until after reading the file.
See the `[tool.pyright]` section in `pyproject.toml` for details.

---

### Keyword-Only Function Arguments
ETL functions use **keyword-only parameters**.

You’ll see a `*,` in the function definitions.
Everything after the asterisk must be passed using named keyword arguments.

**Why this matters:**
- Prevents argument-order mistakes
- Makes function calls self-documenting
- Improves clarity in multi-step pipelines

This is a common pattern in production analytics code.

---

## Large Project File Notice

This repository includes a **2.2 MB Excel file**.
The pre-commit configuration has been adjusted to allow this file size.

### Debug Tips
- If you see “import block is unsorted”:
  Use VS Code → hover → lightbulb → **Organize Imports**.
- If you see “Type of run_csv_pipeline is unknown”:
  Ensure your `.venv` is active and selected in VS Code.
  Command Palette → **Python: Select Interpreter** → choose the `.venv`.
  Then reload the window.

---

## Working Files

You will work primarily in:

- `docs/` — project narrative and documentation
- `src/datafun/` — all pipeline logic
- `pyproject.toml` — authorship, metadata, dependencies
- `zensical.toml` — authorship and project links

---

## Instructions

Follow the workflow guide to complete:

1. Phase 1 — Start & Run
2. Phase 2 — Change Authorship
3. Phase 3 — Read & Understand
4. Phase 4 — Modify
5. Phase 5 — Apply

Each phase builds on the previous one.

---

## Challenges

Challenges are expected.
Different operating systems behave differently, and part of learning professional analytics is troubleshooting:

- Share screenshots
- Include error messages
- Describe what you tried

Working through issues is part of the process.

---

## Success

After completing **Phase 1**, you will have:

- A working GitHub repository
- A functioning local environment
- A complete analytics pipeline

Running the example prints:


```shell
========== Executed successfully! ==========
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.


### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

## Clone the Repository
git clone https://github.com/username/datafun-03-analytics
cd datafun-03-analytics
code .

## Environment Setup
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
uvx pre-commit install

## Run Pre‑Commit
git add -A
uvx pre-commit run --all-files
git add -A
uvx pre-commit run --all-files

## Run the Example Module
uv run python -m datafun.app_jt

## Save Progress
git add -A
git commit -m "update"
git push -u origin main

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Example Output

```text
2026-05-27 16:16:06 | INFO | JT | === RUN START ===
2026-05-27 16:16:06 | INFO | JT | project=JT PIPELINES
2026-05-27 16:16:06 | INFO | JT | repo_dir=datafun-03-analytics
2026-05-27 16:16:06 | INFO | JT | python=3.14.5
2026-05-27 16:16:06 | INFO | JT | os=Windows 11
2026-05-27 16:16:06 | INFO | JT | shell=powershell
2026-05-27 16:16:06 | INFO | JT | cwd=.
2026-05-27 16:16:06 | INFO | JT | github_actions=False
2026-05-27 16:16:06 | INFO | JT | ========== START main() ==========
2026-05-27 16:16:06 | INFO | JT | ROOT_DIR = .
2026-05-27 16:16:06 | INFO | JT | PROCESSED_DIR = data\processed
2026-05-27 16:16:06 | INFO | JT | CSV PIPELINE: START
2026-05-27 16:16:06 | INFO | JT | CSV PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\justice_score_stats.txt
2026-05-27 16:16:06 | INFO | JT | CSV PIPELINE: END
2026-05-27 16:16:06 | INFO | JT | JT XLSX PIPELINE: START

=== FEEDBACK FROM EXCEL ===
Excellent work on the project!
The results were excellent and clear.
Needs improvement in documentation.
Excellent presentation and delivery.
Good effort overall.
=== END FEEDBACK ===

2026-05-27 16:16:06 | INFO | JT | JT XLSX PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\jt_xlsx_word_count.txt
2026-05-27 16:16:06 | INFO | JT | JT XLSX PIPELINE: END
2026-05-27 16:16:06 | INFO | JT | JSON PIPELINE: START
2026-05-27 16:16:06 | INFO | JT | JSON PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\json_people_by_country.txt
2026-05-27 16:16:06 | INFO | JT | JSON PIPELINE: END
2026-05-27 16:16:06 | INFO | JT | JT TXT PIPELINE: START
2026-05-27 16:16:06 | INFO | JT | JT TXT PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\jt_text_summary.txt
2026-05-27 16:16:06 | INFO | JT | JT TXT PIPELINE: END
2026-05-27 16:16:06 | INFO | JT | ========== Executed successfully! ==========
