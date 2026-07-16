# core/validator.py

from pathlib import Path
import re


class EPUBValidator:
    """
    Validate EPUB project structure.
    """


    def __init__(self, epub_dir):

        self.epub_dir = Path(epub_dir)

        self.errors = []

        self.warnings = []



    def validate(self):

        self.errors.clear()
        self.warnings.clear()


        self._check_structure()

        self._check_container()

        self._check_opf()

        self._check_xhtml()


        return {

            "valid":
                len(self.errors) == 0,

            "errors":
                self.errors,

            "warnings":
                self.warnings

        }



    def _check_structure(self):

        required = [

            "mimetype",

            "META-INF/container.xml",

            "EPUB"

        ]


        for item in required:

            path = (
                self.epub_dir / item
            )

            if not path.exists():

                self.errors.append(

                    f"Missing required file: {item}"

                )



    def _check_container(self):

        file = (
            self.epub_dir
            /
            "META-INF/container.xml"
        )


        if not file.exists():

            return


        text = file.read_text(
            encoding="utf-8"
        )


        if "package.opf" not in text:

            self.errors.append(

                "container.xml does not point to package.opf"

            )



    def _check_opf(self):

        opf = list(

            self.epub_dir.glob(
                "EPUB/*.opf"
            )

        )


        if not opf:

            self.errors.append(

                "Missing OPF package file"

            )

            return



        text = opf[0].read_text(
            encoding="utf-8"
        )


        required_tags = [

            "<metadata",

            "<manifest",

            "<spine"

        ]


        for tag in required_tags:

            if tag not in text:

                self.errors.append(

                    f"Missing OPF section: {tag}"

                )



    def _check_xhtml(self):


        files = list(

            self.epub_dir.rglob(
                "*.xhtml"
            )

        )


        for file in files:


            text = file.read_text(

                encoding="utf-8"

            )


            if "<html" not in text:

                self.errors.append(

                    f"Invalid XHTML: {file.name}"

                )


            if "</html>" not in text:

                self.errors.append(

                    f"Broken XHTML closing tag: {file.name}"

                )



    def report(self):

        result = self.validate()


        print(
            "EPUB Validation Report"
        )

        print(
            "-" * 30
        )


        if result["valid"]:

            print(
                "PASS: EPUB structure OK"
            )

        else:

            print(
                "FAILED"
            )


        if self.errors:

            print("\nErrors:")

            for error in self.errors:

                print(
                    " -",
                    error
                )


        if self.warnings:

            print("\nWarnings:")

            for warning in self.warnings:

                print(
                    " -",
                    warning
                )
