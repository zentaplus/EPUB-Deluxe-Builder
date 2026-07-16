"""
core.chapter_parser

Split novel text into chapters.

Supports:

- Chương 1
- Chương 100
- Chương Một
- 第1章
- 第001章
- 第三十五章
- Chapter 1
- Volume 1
- Quyển 1
- Thứ 73 chương
"""

from __future__ import annotations

import re
from dataclasses import dataclass


# ---------------------------------------------------------
# Data
# ---------------------------------------------------------

@dataclass(slots=True)
class Chapter:

    title: str

    content: str


# ---------------------------------------------------------
# Regex
# ---------------------------------------------------------

CHAPTER_PATTERNS = [

    # Chương 1
    r"^Chương\s+\d+.*$",

    # Chương Một
    r"^Chương\s+[A-Za-zÀ-ỹ]+.*$",

    # Thứ 73 chương
    r"^Thứ\s+\d+\s+chương.*$",

    # Chapter 1
    r"^Chapter\s+\d+.*$",

    # Volume 1
    r"^Volume\s+\d+.*$",

    # Quyển 1
    r"^Quyển\s+\d+.*$",

    # 第1章
    r"^第\s*\d+\s*[章节卷].*$",

    # 第三十五章
    r"^第[一二三四五六七八九十百千万零〇两]+[章节卷].*$",

]

CHAPTER_REGEX = re.compile(

    "|".join(f"(?:{p})" for p in CHAPTER_PATTERNS),

    re.IGNORECASE,

)


# ---------------------------------------------------------
# Parser
# ---------------------------------------------------------

class ChapterParser:

    """
    Split TXT into chapters.
    """

    def is_chapter(self, line: str) -> bool:

        return bool(

            CHAPTER_REGEX.match(

                line.strip()

            )

        )

    def split(self, text: str) -> list[Chapter]:

        chapters: list[Chapter] = []

        title = "Giới thiệu"

        buffer: list[str] = []

        for raw in text.split("\n"):

            line = raw.strip()

            if self.is_chapter(line):

                if buffer:

                    chapters.append(

                        Chapter(

                            title=title,

                            content="\n".join(buffer).strip(),

                        )

                    )

                title = line

                buffer = []

                continue

            buffer.append(raw)

        if buffer:

            chapters.append(

                Chapter(

                    title=title,

                    content="\n".join(buffer).strip(),

                )

            )

        return chapters


# ---------------------------------------------------------
# API
# ---------------------------------------------------------

_parser = ChapterParser()


def split_chapters(text: str) -> list[Chapter]:

    """
    Split novel into chapters.
    """

    return _parser.split(text)
