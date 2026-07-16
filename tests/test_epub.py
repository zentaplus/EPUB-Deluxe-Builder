# tests/test_epub.py

from zipfile import ZipFile



def test_epub_structure(epub_file):


    with ZipFile(
        epub_file
    ) as epub:


        files = epub.namelist()


        assert (
            "mimetype"
            in files
        )


        assert (

            "META-INF/container.xml"

            in files

        )
