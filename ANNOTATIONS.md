# ANNOTATION.md
JT PIPELINES — Execution Notes & Example Output
Updated: 2026-05-28

---

## Purpose
This document records the execution of the JT Pipelines program, including:
- Environment details
- Pipeline stages (CSV, XLSX, JSON, TXT)
- File outputs written to the `data/processed` directory
- Example terminal output for documentation and verification

---

## Pipeline Overview

### 1. CSV Pipeline
- Reads CSV source data
- Computes summary statistics
- Writes: `justice_score_stats.txt`

### 2. XLSX Pipeline
- Reads Excel workbook
- Extracts feedback text
- Counts words
- Writes: `jt_xlsx_word_count.txt`
- Displays feedback block in terminal

### 3. JSON Pipeline
- Reads JSON dataset
- Groups people by country
- Writes: `json_people_by_country.txt`

### 4. TXT Pipeline
- Reads text file
- Summarizes content
- Writes: `jt_text_summary.txt`

---

## Example Output (Formatted)

2026-05-28 03:01:49 | INFO | JT | === RUN START ===
2026-05-28 03:01:49 | INFO | JT | project=JT PIPELINES
2026-05-28 03:01:49 | INFO | JT | repo_dir=datafun-03-analytics
2026-05-28 03:01:49 | INFO | JT | python=3.14.5
2026-05-28 03:01:50 | INFO | JT | os=Windows 11
2026-05-28 03:01:50 | INFO | JT | shell=powershell
2026-05-28 03:01:50 | INFO | JT | cwd=.
2026-05-28 03:01:50 | INFO | JT | github_actions=False

2026-05-28 03:01:50 | INFO | JT | ========== START main() ==========
2026-05-28 03:01:50 | INFO | JT | ROOT_DIR = .
2026-05-28 03:01:50 | INFO | JT | PROCESSED_DIR = data\processed

2026-05-28 03:01:50 | INFO | JT | CSV PIPELINE: START
2026-05-28 03:01:50 | INFO | JT | CSV PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\justice_score_stats.txt
2026-05-28 03:01:50 | INFO | JT | CSV PIPELINE: END

2026-05-28 03:01:50 | INFO | JT | JT XLSX PIPELINE: START

=== FEEDBACK FROM EXCEL ===
Excellent work on the project!
The results were excellent and clear.
Needs improvement in documentation.
Excellent presentation and delivery.
Good effort overall.
=== END FEEDBACK ===

2026-05-28 03:01:50 | INFO | JT | JT XLSX PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\jt_xlsx_word_count.txt
2026-05-28 03:01:50 | INFO | JT | JT XLSX PIPELINE: END

2026-05-28 03:01:50 | INFO | JT | JSON PIPELINE: START
2026-05-28 03:01:50 | INFO | JT | JSON PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\json_people_by_country.txt
2026-05-28 03:01:50 | INFO | JT | JSON PIPELINE: END

2026-05-28 03:01:50 | INFO | JT | JT TXT PIPELINE: START
2026-05-28 03:01:50 | INFO | JT | JT TXT PIPELINE: wrote C:\Users\JTEFE\Repos\datafun-03-analytics\data\processed\jt_text_summary.txt
2026-05-28 03:01:50 | INFO | JT | JT TXT PIPELINE: END

2026-05-28 03:01:50 | INFO | JT | ========== Executed successfully! ==========

---

## Notes
- All pipelines executed without errors.
- Output files were successfully written to `data/processed`.
- Pre‑commit hooks enforce LF line endings, trailing whitespace cleanup, and formatting.
- Windows may display CRLF warnings, but the repository remains clean and consistent.

---

## Summary
The JT Pipelines program is functioning correctly and producing consistent, validated outputs across all stages. This annotation serves as a reference for future runs, debugging, and documentation updates.
