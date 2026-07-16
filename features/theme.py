# features/theme.py

from pathlib import Path


class ThemeBuilder:
    """
    EPUB reading theme generator.
    """


    THEMES = {

        "classic": {

            "background": "#ffffff",

            "text":
            "#222222",

            "font":
            "Georgia, serif",

            "line":
            "1.7"

        },


        "modern": {

            "background":
            "#ffffff",

            "text":
            "#333333",

            "font":
            "Arial, sans-serif",

            "line":
            "1.6"

        },


        "dark": {

            "background":
            "#111111",

            "text":
            "#eeeeee",

            "font":
            "Arial, sans-serif",

            "line":
            "1.7"

        },


        "sepia": {

            "background":
            "#f4ecd8",

            "text":
            "#5b4636",

            "font":
            "Georgia, serif",

            "line":
            "1.8"

        },


        "manga": {

            "background":
            "#ffffff",

            "text":
            "#000000",

            "font":
            "sans-serif",

            "line":
            "1.4"

        }

    }



    def __init__(
        self,
        project_dir
    ):

        self.project_dir = Path(
            project_dir
        )


        self.css_dir = (

            self.project_dir
            /
            "content/css"

        )



    def generate(
        self,
        theme="classic"
    ):

        if theme not in self.THEMES:

            raise ValueError(

                f"Unknown theme: {theme}"

            )


        config = self.THEMES[theme]


        css = f"""

/*
 EPUB Deluxe Theme:
 {theme}
*/


body {{

background-color:
{config['background']};

color:
{config['text']};

font-family:
{config['font']};

line-height:
{config['line']};

margin:
5%;

}}



h1 {{

text-align:
center;

font-weight:
bold;

}}



p {{

text-indent:
1.5em;

margin-bottom:
0.8em;

}}



img {{

max-width:
100%;

height:
auto;

}}



"""


        return css



    def save(
        self,
        theme="classic"
    ):


        self.css_dir.mkdir(

            parents=True,

            exist_ok=True

        )


        output = (

            self.css_dir
            /
            f"{theme}.css"

        )


        output.write_text(

            self.generate(theme),

            encoding="utf-8"

        )


        return output



    def available_themes(self):

        return list(
            self.THEMES.keys()
        )
