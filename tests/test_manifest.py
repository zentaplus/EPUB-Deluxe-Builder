# tests/test_manifest.py

from pathlib import Path

from core.manifest import (
    ManifestBuilder
)



def test_manifest_scan(tmp_path):

    epub = tmp_path / "EPUB"

    epub.mkdir()


    file = (

        epub
        /
        "chapter.xhtml"

    )


    file.write_text(

        "<html></html>",

        encoding="utf-8"

    )


    manifest = ManifestBuilder(

        epub

    )


    items = manifest.scan()


    assert len(items) == 1

    assert (
        items[0]["media-type"]
        ==
        "application/xhtml+xml"
    )
