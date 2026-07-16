"""
core.builder

Main EPUB building pipeline.

Pipeline:

TXT
 |
Cleaner
 |
Chapter Parser
 |
EPUB Book
 |
Metadata
 |
Cover
 |
CSS
 |
TOC
 |
EPUB Output

"""

from __future__ import annotations


from pathlib import Path

from ebooklib import epub


from .cleaner import clean_text

from .chapter_parser import split_chapters

from .cover import load_cover

from .css import get_css_bytes

from .metadata import (
    Metadata,
    apply_metadata,
)

from .toc import (
    build_pages,
    apply_toc,
    build_spine,
    add_navigation,
)

from .utils import (
    log,
    safe_filename,
    ensure_directory,
)


# =========================================================
# Constants
# =========================================================

DEFAULT_LANGUAGE = "vi"


# =========================================================
# Builder Exception
# =========================================================

class EPUBBuilderError(Exception):
    """
    General EPUB builder error.
    """



# =========================================================
# EPUB Builder
# =========================================================

class EPUBBuilder:

    """
    Main EPUB creation engine.
    """


    def __init__(
        self,
        output_dir: str | Path = "output",
    ):

        self.output_dir = Path(output_dir)

        ensure_directory(
            self.output_dir
        )


    # -----------------------------------------------------

    def read_text(
        self,
        path: str | Path,
    ) -> str:

        """
        Read TXT file.

        UTF-8 first,
        fallback UTF-16.
        """

        path = Path(path)

        if not path.exists():

            raise EPUBBuilderError(
                "Input file not found"
            )


        encodings = [

            "utf-8",

            "utf-8-sig",

            "utf-16",

            "gb18030",

            "cp1258",

        ]


        for encoding in encodings:

            try:

                return path.read_text(
                    encoding=encoding
                )

            except UnicodeDecodeError:

                continue


        raise EPUBBuilderError(
            "Cannot decode text file"
        )


    # -----------------------------------------------------

    def create_book(
        self,
        title: str,
        author: str,
    ) -> epub.EpubBook:


        book = epub.EpubBook()


        metadata = Metadata(

            title=title,

            author=author,

            language=DEFAULT_LANGUAGE,

        )


        apply_metadata(

            book,

            metadata,

        )


        return book


    # -----------------------------------------------------

    def add_stylesheet(
        self,
        book: epub.EpubBook,
    ):

        style = epub.EpubItem(

            uid="style",

            file_name="styles/style.css",

            media_type="text/css",

            content=get_css_bytes(),

        )


        book.add_item(style)


        return style

  # core/builder.py

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED
import shutil
import tempfile

from .manifest import ManifestBuilder
from .metadata import MetadataBuilder
from .toc import TocBuilder


class EPUBBuilder:
    """
    Main EPUB build engine.
    """

    def __init__(self, project_dir, output_file):
        self.project_dir = Path(project_dir)
        self.output_file = Path(output_file)

        self.temp_dir = None

        self.oebps_dir = None
        self.meta_inf_dir = None

    def build(self):
        """
        Build complete EPUB package.
        """

        self._create_workspace()

        self._prepare_structure()

        self._copy_resources()

        self._generate_metadata()

        self._generate_manifest()

        self._generate_toc()

        self._package_epub()

        self._cleanup()

        return self.output_file


    def _create_workspace(self):

        self.temp_dir = Path(
            tempfile.mkdtemp(prefix="epub_build_")
        )


    def _prepare_structure(self):

        root = self.temp_dir

        self.meta_inf_dir = root / "META-INF"
        self.oebps_dir = root / "EPUB"

        self.meta_inf_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.oebps_dir.mkdir(
            parents=True,
            exist_ok=True
        )


        # Required EPUB mimetype
        mimetype = root / "mimetype"

        mimetype.write_text(
            "application/epub+zip",
            encoding="utf-8"
        )


        container = self.meta_inf_dir / "container.xml"

        container.write_text(
            """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0"
 xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
 <rootfiles>
  <rootfile full-path="EPUB/package.opf"
   media-type="application/oebps-package+xml"/>
 </rootfiles>
</container>
""",
            encoding="utf-8"
        )


    def _copy_resources(self):

        source = self.project_dir / "content"

        if not source.exists():
            return

        for item in source.iterdir():

            target = self.oebps_dir / item.name

            if item.is_dir():

                shutil.copytree(
                    item,
                    target,
                    dirs_exist_ok=True
                )

            else:

                shutil.copy2(
                    item,
                    target
                )


    def _generate_metadata(self):

        metadata = MetadataBuilder(
            self.project_dir
        )

        metadata.save(
            self.oebps_dir / "package.opf"
        )


    def _generate_manifest(self):

        manifest = ManifestBuilder(
            self.oebps_dir
        )

        manifest.update(
            self.oebps_dir / "package.opf"
        )


    def _generate_toc(self):

        toc = TocBuilder(
            self.project_dir
        )

        toc.save(
            self.oebps_dir / "toc.xhtml"
        )


    def _package_epub(self):

        if self.output_file.exists():
            self.output_file.unlink()


        with ZipFile(
            self.output_file,
            "w"
        ) as epub:

            # EPUB requirement:
            # mimetype must be first and uncompressed

            epub.write(
                self.temp_dir / "mimetype",
                "mimetype",
                compress_type=ZIP_STORED
            )


            for file in self.temp_dir.rglob("*"):

                if file.name == "mimetype":
                    continue

                epub.write(
                    file,
                    file.relative_to(
                        self.temp_dir
                    ),
                    compress_type=ZIP_DEFLATED
                )


    def _cleanup(self):

        if self.temp_dir and self.temp_dir.exists():

            shutil.rmtree(
                self.temp_dir,
                ignore_errors=True
            )



