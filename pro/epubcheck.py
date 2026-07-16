# pro/epubcheck.py

from pathlib import Path
import re


class EPUBCheckPro:
    """
    Professional EPUB quality checker.
    """


    def __init__(
        self,
        epub_dir
    ):

        self.epub_dir = Path(
            epub_dir
        )


        self.errors = []

        self.warnings = []



    def check_mimetype(self):

        file = (
            self.epub_dir
            /
            "mimetype"
        )


        if not file.exists():

            self.errors.append(

                "Missing mimetype"

            )

            return



        content = file.read_text(

            encoding="utf-8"

        ).strip()



        if content != (
            "application/epub+zip"
        ):

            self.errors.append(

                "Invalid mimetype"

            )



    def check_container(self):

        container = (

            self.epub_dir

            /

            "META-INF/container.xml"

        )


        if not container.exists():

            self.errors.append(

                "Missing container.xml"

            )

            return



        text = container.read_text(

            encoding="utf-8"

        )


        if "package.opf" not in text:

            self.errors.append(

                "Invalid container reference"

            )



    def check_opf_structure(self):

        opf_files = list(

            self.epub_dir.rglob(

                "*.opf"

            )

        )


        if not opf_files:

            self.errors.append(

                "OPF not found"

            )

            return



        opf = opf_files[0]


        text = opf.read_text(

            encoding="utf-8"

        )


        required = [

            "<metadata",

            "<manifest",

            "<spine"

        ]


        for item in required:


            if item not in text:

                self.errors.append(

                    f"OPF missing {item}"

                )



    def check_xhtml(self):

        files = list(

            self.epub_dir.rglob(

                "*.xhtml"

            )

        )


        for file in files:


            text = file.read_text(

                encoding="utf-8"

            )


            if not re.search(

                r"<html.*?>",

                text,

                re.I

            ):

                self.errors.append(

                    f"Invalid XHTML: {file.name}"

                )



            if "</body>" not in text:

                self.errors.append(

                    f"Missing body: {file.name}"

                )



    def check_resources(self):

        """

        Detect empty resource folders.
        """

        folders = [

            "images",

            "fonts",

            "css"

        ]


        for folder in folders:


            path = (

                self.epub_dir
                /
                folder

            )


            if path.exists():

                if not any(path.iterdir()):

                    self.warnings.append(

                        f"Empty folder: {folder}"

                    )



    def run(self):

        self.errors.clear()

        self.warnings.clear()


        self.check_mimetype()

        self.check_container()

        self.check_opf_structure()

        self.check_xhtml()

        self.check_resources()



        return {

            "status":

                len(self.errors) == 0,


            "errors":

                self.errors,


            "warnings":

                self.warnings

        }



    def report(self):

        result = self.run()


        print(
            "EPUB Professional Check"
        )

        print(
            "=" * 35
        )


        if result["status"]:

            print(
                "PASS"
            )

        else:

            print(
                "FAILED"
            )


        for e in self.errors:

            print(
                "[ERROR]",
                e
            )


        for w in self.warnings:

            print(
                "[WARN]",
                w
            )
