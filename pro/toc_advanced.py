# pro/toc_advanced.py

from pathlib import Path
import re


class AdvancedTOCBuilder:
    """
    Advanced EPUB 3 navigation generator.
    """


    def __init__(
        self,
        chapter_dir
    ):

        self.chapter_dir = Path(
            chapter_dir
        )


        self.structure = []



    def scan(self):

        """
        Scan XHTML headings.
        """


        self.structure.clear()


        files = sorted(

            self.chapter_dir.glob(
                "*.xhtml"
            )

        )


        for file in files:


            chapter = {

                "file":
                    file.name,

                "title":
                    file.stem,

                "sections":
                    []

            }


            content = file.read_text(

                encoding="utf-8"

            )


            headings = re.findall(

                r"<h([1-3])[^>]*>(.*?)</h\1>",

                content,

                re.I | re.S

            )


            for level, title in headings:


                title = re.sub(

                    "<.*?>",

                    "",

                    title

                ).strip()



                chapter["sections"].append({

                    "level":
                        int(level),

                    "title":
                        title

                })


            self.structure.append(
                chapter
            )


        return self.structure



    def build_list(
        self,
        chapters=None
    ):


        if chapters is None:

            chapters = self.scan()



        html = []


        html.append(

            "<ol>"

        )


        for chapter in chapters:


            html.append(

f"""
<li>

<a href="chapters/{chapter['file']}">

{chapter['title']}

</a>

"""

            )


            sections = chapter["sections"]


            if sections:


                html.append(

                    "<ol>"

                )


                for section in sections:


                    html.append(

f"""
<li>
<span>
{section['title']}
</span>
</li>
"""

                    )


                html.append(

                    "</ol>"

                )



            html.append(

                "</li>"

            )


        html.append(

            "</ol>"

        )


        return "\n".join(html)



    def generate_nav(self):


        toc = self.build_list()



        return f"""<?xml version="1.0"
encoding="UTF-8"?>


<html

xmlns="http://www.w3.org/1999/xhtml"

xmlns:epub="http://www.idpf.org/2007/ops">


<head>

<title>
Table of Contents
</title>

</head>


<body>


<nav epub:type="toc">


<h1>
Contents
</h1>


{toc}


</nav>


</body>


</html>
"""



    def save(
        self,
        output_file
    ):


        output_file = Path(
            output_file
        )


        output_file.write_text(

            self.generate_nav(),

            encoding="utf-8"

        )


        return output_file
