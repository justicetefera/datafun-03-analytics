"""
app_jt.py - Justice's master pipeline runner.

This script mirrors the instructor's app_case.py but calls MY custom pipelines:
    - justice_csv_pipeline
    - jaso_pipeline
    - jt_text_pipeline
    - jt_xlsx_pipeline

Running this file executes ALL my ETVL pipelines and writes results to:
    data/processed/

Run from project root:

    uv run python -m cintel.app_jt
"""

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path

# === IMPORT MY CUSTOM PIPELINES ===
from datafun.jt_csv_pipeline import run_csv_pipeline
from datafun.jt_json_pipeline import run_json_pipeline
from datafun.jt_text_pipeline import run_text_pipeline
from datafun.jt_xlsx_pipeline import run_xlsx_pipeline

# === LOGGER ===
LOG: logging.Logger = get_logger("JT", level="DEBUG")

# === PATHS ===
ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
RAW_DIR: Final[Path] = DATA_DIR / "raw"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed"


def main() -> None:
    """Run all four of Justice's custom ETVL pipelines."""
    log_header(LOG, "JT PIPELINES")

    LOG.info("========== START main() ==========")
    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "PROCESSED_DIR", PROCESSED_DIR)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # === RUN ALL MY PIPELINES ===
    run_csv_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)
    run_xlsx_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)
    run_json_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)
    run_text_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)

    LOG.info("========== Executed successfully! ==========")


if __name__ == "__main__":
    main()
