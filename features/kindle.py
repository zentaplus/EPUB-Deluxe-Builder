# features/kindle.py

from pathlib import Path


class KindleChecker:
    """
    Kindle compatibility checker.
    """


    def __init__(
        self,
        project_dir
    ):

        self.project_dir = Path(
            project_dir
        )


        self.content = (
            self.project_dir
            /
            "content"
        )


        self.errors = []

        self.warnings = []



    def check_cover(self):

        """
        Check cover image.
        """

        images = (

            self.content
            /
            "images"

        )


        found = False


        if images.exists():

            for file in images.iterdir():

                if file.name.lower() in [

                    "cover.jpg",
                    "cover.jpeg",
                    "cover.png"

                ]:

                    found = True


        if not found:

            self.warnings.append(

                "Missing cover image"

            )



    def check_fonts(self):

        """
        Check embedded fonts.
        """

        fonts = (

            self.content
            /
            "fonts"

        )


        if not fonts.exists():

            return


        for font in fonts.iterdir():

            if font.suffix.lower() not in [

                ".ttf",
                ".otf",
                ".woff",
                ".woff2"

            ]:

                self.warnings.append(

                    f"Unsupported font: {font.name}"

                )



    def check_xhtml(self):

        """
        Check XHTML files.
        """

        chapters = (

            self.content
            /
            "chapters"

        )


        if not chapters.exists():

            return


        for file in chapters.glob(
            "*.xhtml"
        ):


            text = file.read_text(

                encoding="utf-8"

            )


            if "<h1" not in text:

                self.warnings.append(

                    f"No chapter title: {file.name}"

                )



    def check_metadata(self):

        """
        Check book metadata.
        """

        config = (

            self.project_dir
            /
            "book.json"

        )


        if not config.exists():

            self.errors.append(

                "Missing book.json metadata"

            )



    def validate(self):

        self.errors.clear()

        self.warnings.clear()


        self.check_cover()

        self.check_fonts()

        self.check_xhtml()

        self.check_metadata()


        return {

            "compatible":
                len(self.errors) == 0,

            "errors":
                self.errors,

            "warnings":
                self.warnings

        }



    def report(self):

        result = self.validate()


        print(
            "Kindle Compatibility Report"
        )

        print(
            "-" * 35
        )


        if result["compatible"]:

            print(
                "READY FOR KINDLE"
            )

        else:

            print(
                "NOT READY"
            )


        for error in self.errors:

            print(
                "[ERROR]",
                error
            )


        for warning in self.warnings:

            print(
                "[WARNING]",
                warning
            )
