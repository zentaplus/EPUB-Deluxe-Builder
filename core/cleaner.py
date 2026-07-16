"""
core.cleaner

Text cleaning pipeline for EPUB Deluxe Builder.

Responsibilities:
- Normalize newlines
- Remove advertisements
- Remove watermarks
- Remove duplicated blank lines
- Normalize spaces
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .utils import (
    collapse_blank_lines,
    normalize_newlines,
    normalize_spaces,
)

# ------------------------------------------------------------
# Remove patterns
# ------------------------------------------------------------

DEFAULT_PATTERNS = [

    r"^@Bạn đang đọc.*$",

    r"^Nguồn:.*$",

    r"^Website:.*$",

    r"^https?://.*$",

    r"^www\..*$",

    r"^={3,}$",

    r"^-{3,}$",

    r"^_{3,}$",

    r"^Quảng\s*cáo.*$",

    r"^Advertisement.*$",

    r"^PS[:：].*$",

    r"^QQ群.*$",

    r"^收藏本站.*$",

    r"^最新网址.*$",

    r"^手机用户.*$",

    r"^本章完.*$",

]


# ------------------------------------------------------------
# Config
# ------------------------------------------------------------

@dataclass(slots=True)
class CleanerConfig:

    remove_patterns: list[str] | None = None

    remove_empty_lines: bool = False


# ------------------------------------------------------------
# Cleaner
# ------------------------------------------------------------

class TextCleaner:

    def __init__(self, config: CleanerConfig | None = None):

        self.config = config or CleanerConfig()

        self.patterns = [

            re.compile(p, re.IGNORECASE)

            for p in (

                self.config.remove_patterns

                or DEFAULT_PATTERNS

            )

        ]


    def remove_ads(self, text: str) -> str:

        result = []

        for line in text.split("\n"):

            skip = False

            stripped = line.strip()

            for pattern in self.patterns:

                if pattern.match(stripped):

                    skip = True

                    break

            if not skip:

                result.append(line)

        return "\n".join(result)


    def normalize(self, text: str) -> str:

        text = normalize_newlines(text)

        text = normalize_spaces(text)

        text = collapse_blank_lines(text)

        return text.strip()


    def clean(self, text: str) -> str:

        text = self.normalize(text)

        text = self.remove_ads(text)

        text = collapse_blank_lines(text)

        return text.strip()


# ------------------------------------------------------------
# Convenience API
# ------------------------------------------------------------

_default_cleaner = TextCleaner()


def clean_text(text: str) -> str:
    """
    Clean novel text.

    Parameters
    ----------
    text:
        Raw TXT content.

    Returns
    -------
    str
        Cleaned content.
    """

    return _default_cleaner.clean(text)
