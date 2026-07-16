# pro/packaging.py

from pathlib import Path
import shutil
import hashlib
import json
from datetime import datetime



class ReleasePackager:
    """
    EPUB release packaging system.
    """



    def __init__(
        self,
        project_dir,
        output_dir="release"
    ):

        self.project_dir = Path(
            project_dir
        )


        self.output_dir = (

            self.project_dir
            /
            output_dir

        )


        self.output_dir.mkdir(

            parents=True,

            exist_ok=True

        )



    def sha256(
        self,
        file
    ):

        """
        Generate SHA256 checksum.
        """

        hash_sha = hashlib.sha256()


        with open(
            file,
            "rb"
        ) as f:


            for block in iter(

                lambda:
                f.read(4096),

                b""

            ):

                hash_sha.update(
                    block
                )


        return hash_sha.hexdigest()



    def copy_epub(
        self,
        epub_file
    ):

        """
        Copy final EPUB.
        """

        source = Path(
            epub_file
        )


        target = (

            self.output_dir
            /
            source.name

        )


        shutil.copy2(

            source,

            target

        )


        return target



    def create_manifest(
        self,
        epub_file
    ):

        """
        Create release information.
        """

        epub = Path(
            epub_file
        )


        info = {

            "file":

                epub.name,


            "size":

                epub.stat().st_size,


            "sha256":

                self.sha256(
                    epub
                ),


            "created":

                datetime.utcnow()
                .strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                )

        }


        output = (

            self.output_dir
            /
            "release.json"

        )


        output.write_text(

            json.dumps(

                info,

                indent=4,

                ensure_ascii=False

            ),

            encoding="utf-8"

        )


        return output



    def package(
        self,
        epub_file
    ):

        """
        Complete release package.
        """


        epub = self.copy_epub(
            epub_file
        )


        manifest = self.create_manifest(
            epub
        )


        return {

            "epub":

                epub,


            "manifest":

                manifest

        }
