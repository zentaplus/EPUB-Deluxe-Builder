"""
core/utils.py

Utility functions used across the project.
"""

from __future__ import annotations

import html
import re
import uuid
from datetime import datetime
from pathlib import Path


# ============================================================
# UUID
# ============================================================

def generate_uuid() -> str:
    """
    Generate a random UUID string.

    Returns
    -------
    str
        UUID v4 string.
    """
    return str(uuid.uuid4())


# ============================================================
# DATE
# ============================================================

def utc_timestamp() -> str:
    """
    Return UTC timestamp in EPUB format.

    Example:
        2026-07-17T02:30:45Z
    """
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def local_date() -> str:
    """
    Return local date.

    Example:
        2026-07-17
    """
    return datetime.now().strftime("%Y-%m-%d")


# ============================================================
# HTML
# ============================================================

def escape_html(text: str) -> str:
    """
    Escape HTML entities.
    """
    return html.escape(text, quote=True)


# ============================================================
# FILENAME
# ============================================================

_INVALID_FILENAME = re.compile(r'[<>:"/\\|?*\x00-\x1F]')


def safe_filename(name: str) -> str:
    """
    Convert string to a safe filename.
    """
    name = _INVALID_FILENAME.sub("_", name)
    name = re.sub(r"\s+", " ", name).strip()

    if not name:
        return "untitled"

    return name


# ============================================================
# PATH
# ============================================================

def ensure_directory(path: Path) -> None:
    """
    Create directory if it does not exist.
    """
    path.mkdir(parents=True, exist_ok=True)


# ============================================================
# TEXT
# ============================================================

def normalize_newlines(text: str) -> str:
    """
    Normalize CRLF / CR to LF.
    """
    return (
        text
        .replace("\r\n", "\n")
        .replace("\r", "\n")
    )


def collapse_blank_lines(text: str) -> str:
    """
    Remove excessive blank lines.
    """
    return re.sub(r"\n{3,}", "\n\n", text)


def normalize_spaces(text: str) -> str:
    """
    Remove trailing spaces.
    """
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines)


# ============================================================
# FILE
# ============================================================

def file_size_mb(path: Path) -> float:
    """
    File size in MB.
    """
    return path.stat().st_size / (1024 * 1024)


# ============================================================
# LOG
# ============================================================

def log(message: str) -> None:
    """
    Console logger.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {message}")
