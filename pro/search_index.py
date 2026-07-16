# pro/search_index.py

from pathlib import Path
import re
import json



class SearchIndexer:
    """
    EPUB content search index generator.
    """



    def __init__(
        self,
        chapter_dir
    ):

        self.chapter_dir = Path(
            chapter_dir
        )


        self.index = {}



    def clean_text(
        self,
        text
    ):

        """
        Remove HTML tags.
        """

        text = re.sub(

            r"<.*?>",

            " ",

            text

        )


        text = re.sub(

            r"\s+",

            " ",

            text

        )


        return text.strip()



    def tokenize(
        self,
        text
    ):

        """
        Convert text into keywords.
        """

        words = re.findall(

            r"\b[\wÀ-ỹ]+\b",

            text.lower()

        )


        return words



    def scan(self):

        """
        Scan all chapters.
        """

        self.index.clear()


        files = sorted(

            self.chapter_dir.glob(
                "*.xhtml"
            )

        )


        for file in files:


            content = file.read_text(

                encoding="utf-8"

            )


            text = self.clean_text(

                content

            )


            words = self.tokenize(

                text

            )


            for position, word in enumerate(words):


                if word not in self.index:

                    self.index[word] = []


                self.index[word].append({

                    "file":

                        file.name,


                    "position":

                        position

                })


        return self.index



    def search(
        self,
        keyword
    ):


        keyword = keyword.lower()


        return self.index.get(

            keyword,

            []

        )



    def save(
        self,
        output_file
    ):


        output_file = Path(
            output_file
        )


        output_file.write_text(

            json.dumps(

                self.index,

                ensure_ascii=False,

                indent=4

            ),

            encoding="utf-8"

        )


        return output_file
