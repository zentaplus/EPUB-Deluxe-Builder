"""
core.metadata

EPUB metadata manager.

Responsibilities

- Title
- Author
- Language
- Identifier
- Publisher
- Description
- Subject
- Rights
- Creator
- Modified Date

Compatible with EPUB3.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ebooklib import epub

from .utils import generate_uuid


# ---------------------------------------------------------
# Data Model
# ---------------------------------------------------------

@dataclass(slots=True)
class Metadata:

    title: str

    author: str

    language: str = "vi"

    publisher: str = ""

    description: str = ""

    subject: str = ""

    rights: str = ""

    contributor: str = "EPUB Deluxe Builder"

    identifier: str | None = None


# ---------------------------------------------------------
# Metadata Builder
# ---------------------------------------------------------

class MetadataBuilder:

    def __init__(self, metadata: Metadata):

        self.metadata = metadata

        if self.metadata.identifier is None:

            self.metadata.identifier = generate_uuid()

    # -----------------------------------------------------

    @staticmethod
    def modified_date() -> str:

        return datetime.utcnow().strftime(

            "%Y-%m-%dT%H:%M:%SZ"

        )

    # -----------------------------------------------------

    def apply(self, book: epub.EpubBook) -> None:

        data = self.metadata

        book.set_identifier(

            data.identifier

        )

        book.set_title(

            data.title

        )

        book.set_language(

            data.language

        )

        book.add_author(

            data.author

        )

        # ---------------------------------------------

        if data.publisher:

            book.add_metadata(

                "DC",

                "publisher",

                data.publisher,

            )

        if data.description:

            book.add_metadata(

                "DC",

                "description",

                data.description,

            )

        if data.subject:

            book.add_metadata(

                "DC",

                "subject",

                data.subject,

            )

        if data.rights:

            book.add_metadata(

                "DC",

                "rights",

                data.rights,

            )

        # ---------------------------------------------

        book.add_metadata(

            "DC",

            "creator",

            data.author,

        )

        book.add_metadata(

            "DC",

            "contributor",

            data.contributor,

        )

        # EPUB3 modified timestamp

        book.add_metadata(

            None,

            "meta",

            "",

            {

                "property": "dcterms:modified",

                "content": self.modified_date(),

            },

        )

        # Generator

        book.add_metadata(

            None,

            "meta",

            "EPUB Deluxe Builder",

            {

                "name": "generator",

                "content": "EPUB Deluxe Builder",

            },

        )


# ---------------------------------------------------------
# Public API
# ---------------------------------------------------------

def apply_metadata(

    book: epub.EpubBook,

    metadata: Metadata,

) -> None:

    """
    Apply metadata to an EPUB book.
    """

    MetadataBuilder(

        metadata

    ).apply(

        book

    )
