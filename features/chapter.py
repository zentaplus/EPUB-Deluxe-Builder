# features/chapter.py

from pathlib import Path
import re


class ChapterProcessor:
    """
    Process and normalize book chapters.
    """


    def __init__(self, chapter_dir):

        self.chapter_dir = Path(
            chapter_dir
        )

        self.chapters = []



    def scan(self):

        """
        Find chapter files.
        """

        self.chapters.clear()


        for file in sorted(
            self.chapter_dir.glob("*.xhtml")
        ):

            self.chapters.append(file)


        return self.chapters



    def extract_title(self, file):

        """
        Extract chapter title.
        """

        content = file.read_text(
            encoding="utf-8"
        )


        title = re.search(

            r"<h1.*?>(.*?)</h1>",

            content,

            re.S | re.I

        )


        if title:

            return self.clean_text(
                title.group(1)
            )


        return file.stem



    def clean_text(self, text):

        """
        Remove HTML tags.
        """

        text = re.sub(

            r"<.*?>",

            "",

            text

        )


        return text.strip()



    def normalize(
        self,
        file,
        index
    ):

        """
        Convert chapter to EPUB standard XHTML.
        """


        title = self.extract_title(
            file
        )


        body = file.read_text(
            encoding="utf-8"
        )


        # remove old wrapper

        body = re.sub(

            r"<\?xml.*?\?>",

            "",

            body

        )


        xhtml = f"""<?xml version="1.0"
encoding="UTF-8"?>

<!DOCTYPE html>

<html
xmlns="http://www.w3.org/1999/xhtml">


<head>

<meta charset="UTF-8"/>

<title>
{title}
</title>


<link
rel="stylesheet"
type="text/css"
href="../css/style.css"/>


</head>


<body>


<section
epub:type="chapter">


<h1>
{title}
</h1>


{body}


</section>


</body>

</html>
"""


        file.write_text(

            xhtml,

            encoding="utf-8"

        )


        return file



    def process_all(self):

        """
        Process all chapters.
        """


        chapters = self.scan()


        result = []


        for index, chapter in enumerate(

            chapters,

            start=1

        ):


            result.append(

                self.normalize(
                    chapter,
                    index
                )

            )


        return result
