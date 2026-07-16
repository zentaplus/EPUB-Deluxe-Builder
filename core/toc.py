"""
core.toc

Build EPUB3 navigation.

Responsibilities

- Navigation document
- NCX
- Table of contents
- Spine helper
"""

from __future__ import annotations

from ebooklib import epub

from .chapter_parser import Chapter


# ---------------------------------------------------------
# TOC Builder
# ---------------------------------------------------------

class TOCBuilder:

    """
    Build EPUB navigation.
    """

    def __init__(self):

        self.pages: list[epub.EpubHtml] = []

    # -----------------------------------------------------

    def create_chapter_pages(

        self,

        chapters: list[Chapter],

    ) -> list[epub.EpubHtml]:

        result = []

        for index, chapter in enumerate(chapters, start=1):

            page = epub.EpubHtml(

                uid=f"chapter_{index}",

                file_name=f"text/chapter_{index:04d}.xhtml",

                title=chapter.title,

                lang="vi",

            )

            page.content = f"""
<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<title>{chapter.title}</title>

<link rel="stylesheet"

href="../styles/style.css"/>

</head>

<body>

<h1>{chapter.title}</h1>

{self._paragraphs(chapter.content)}

</body>

</html>
"""

            result.append(page)

        self.pages = result

        return result

    # -----------------------------------------------------

    @staticmethod
    def _paragraphs(text: str) -> str:

        html = []

        for line in text.split("\n"):

            line = line.strip()

            if not line:

                continue

            html.append(

                f"<p>{line}</p>"

            )

        return "\n".join(html)

    # -----------------------------------------------------

    def apply(

        self,

        book: epub.EpubBook,

        title_page: epub.EpubHtml,

        info_page: epub.EpubHtml,

    ) -> None:

        toc = [

            epub.Link(

                title_page.file_name,

                "Trang tiêu đề",

                "title",

            ),

            epub.Link(

                info_page.file_name,

                "Thông tin",

                "info",

            ),

        ]

        toc.extend(self.pages)

        book.toc = tuple(toc)

    # -----------------------------------------------------

    def build_spine(

        self,

        title_page: epub.EpubHtml,

        info_page: epub.EpubHtml,

    ):

        spine = [

            "nav",

            title_page,

            info_page,

        ]

        spine.extend(self.pages)

        return spine

    # -----------------------------------------------------

    @staticmethod
    def add_navigation(

        book: epub.EpubBook,

    ):

        book.add_item(

            epub.EpubNav()

        )

        book.add_item(

            epub.EpubNcx()

        )


# ---------------------------------------------------------
# Public API
# ---------------------------------------------------------

_builder = TOCBuilder()


def build_pages(

    chapters: list[Chapter],

) -> list[epub.EpubHtml]:

    return _builder.create_chapter_pages(

        chapters

    )


def apply_toc(

    book: epub.EpubBook,

    title_page: epub.EpubHtml,

    info_page: epub.EpubHtml,

):

    _builder.apply(

        book,

        title_page,

        info_page,

    )


def build_spine(

    title_page: epub.EpubHtml,

    info_page: epub.EpubHtml,

):

    return _builder.build_spine(

        title_page,

        info_page,

    )


def add_navigation(

    book: epub.EpubBook,

):

    _builder.add_navigation(book)
