# features/cover.py

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


class CoverBuilder:
    """
    EPUB cover generator.
    """


    def __init__(
        self,
        project_dir
    ):

        self.project_dir = Path(
            project_dir
        )


        self.image_dir = (
            self.project_dir
            /
            "content/images"
        )


        self.output_dir = (
            self.project_dir
            /
            "content"
        )


        self.cover_file = None



    def find_cover(self):

        """
        Search existing cover image.
        """

        if not self.image_dir.exists():

            return None


        names = [

            "cover.jpg",
            "cover.jpeg",
            "cover.png",
            "Cover.jpg",
            "Cover.png"

        ]


        for name in names:

            file = (
                self.image_dir
                /
                name
            )


            if file.exists():

                self.cover_file = file

                return file


        return None



    def create_placeholder(
        self,
        title="Untitled Book"
    ):

        """
        Create simple cover.
        """

        self.image_dir.mkdir(
            parents=True,
            exist_ok=True
        )


        output = (
            self.image_dir
            /
            "cover.png"
        )


        img = Image.new(

            "RGB",

            (
                1600,
                2560
            ),

            "white"

        )


        draw = ImageDraw.Draw(
            img
        )


        try:

            font = ImageFont.truetype(
                "DejaVuSans.ttf",
                120
            )

        except:

            font = None



        draw.text(

            (
                200,
                1100
            ),

            title,

            font=font

        )


        img.save(
            output
        )


        self.cover_file = output


        return output



    def validate_image(self):

        """
        Check cover image.
        """

        if not self.cover_file:

            return False


        try:

            img = Image.open(
                self.cover_file
            )


            img.verify()


            return True


        except Exception:

            return False



    def generate_xhtml(self):

        """
        Generate EPUB cover page.
        """

        xhtml = f"""<?xml version="1.0"
encoding="UTF-8"?>


<!DOCTYPE html>


<html
xmlns="http://www.w3.org/1999/xhtml">


<head>

<title>
Cover
</title>


</head>


<body>


<div
style="text-align:center">


<img

src="images/{self.cover_file.name}"

alt="Cover"

style="max-width:100%;height:auto;"/>


</div>


</body>


</html>
"""


        output = (
            self.output_dir
            /
            "cover.xhtml"
        )


        output.write_text(

            xhtml,

            encoding="utf-8"

        )


        return output



    def build(
        self,
        title="Untitled Book"
    ):

        cover = self.find_cover()


        if not cover:

            cover = self.create_placeholder(
                title
            )


        if not self.validate_image():

            raise Exception(
                "Invalid cover image"
            )


        return self.generate_xhtml()
