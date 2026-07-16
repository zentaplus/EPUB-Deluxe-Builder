# features/typography.py

from pathlib import Path


class TypographyBuilder:
    """
    EPUB typography and CSS generator.
    """


    def __init__(
        self,
        project_dir
    ):

        self.project_dir = Path(
            project_dir
        )


        self.content_dir = (
            self.project_dir
            /
            "content"
        )


        self.css_dir = (
            self.content_dir
            /
            "css"
        )


        self.font_dir = (
            self.content_dir
            /
            "fonts"
        )


        self.fonts = []



    def scan_fonts(self):

        """
        Find embedded fonts.
        """

        self.fonts.clear()


        if not self.font_dir.exists():

            return []


        supported = [

            ".ttf",
            ".otf",
            ".woff",
            ".woff2"

        ]


        for file in self.font_dir.iterdir():

            if file.suffix.lower() in supported:

                self.fonts.append(file)


        return self.fonts



    def generate_font_face(self):

        """
        Generate @font-face CSS.
        """

        css = []


        for font in self.scan_fonts():

            name = font.stem


            css.append(

f"""
@font-face {{

font-family: '{name}';

src:
url('../fonts/{font.name}');

}}

"""

            )


        return "\n".join(css)



    def generate_css(
        self,
        theme="classic"
    ):

        """
        Create reading stylesheet.
        """


        font_css = (
            self.generate_font_face()
        )


        if theme == "modern":

            body_font = "Arial, sans-serif"


        else:

            body_font = (
                "Georgia, "
                "serif"
            )



        css = f"""
{font_css}


body {{

font-family:
{body_font};

font-size:
1em;

line-height:
1.6;

margin:

0
5%;

text-align:
justify;

}}



h1 {{

font-size:
1.8em;

text-align:
center;

margin-bottom:
1em;

}}



p {{

text-indent:
1.5em;

margin:
0.6em 0;

}}



img {{

max-width:
100%;

height:
auto;

}}



.chapter {{

page-break-before:
always;

}}

"""


        return css



    def save(
        self,
        theme="classic"
    ):

        """
        Save style.css.
        """


        self.css_dir.mkdir(

            parents=True,

            exist_ok=True

        )


        css_file = (

            self.css_dir
            /
            "style.css"

        )


        css_file.write_text(

            self.generate_css(theme),

            encoding="utf-8"

        )


        return css_file
