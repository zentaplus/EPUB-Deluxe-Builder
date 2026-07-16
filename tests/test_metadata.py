# tests/test_metadata.py

from pathlib import Path

from core.metadata import (
    MetadataBuilder
)



def test_metadata_creation(tmp_path):

    project = tmp_path / "book"

    project.mkdir()


    builder = MetadataBuilder(
        project
    )


    output = (
        project
        /
        "package.opf"
    )


    builder.save(
        output
    )


    assert output.exists()


    content = output.read_text(

        encoding="utf-8"

    )


    assert "<dc:title>" in content
