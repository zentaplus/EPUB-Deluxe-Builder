# pro/metadata_ai.py

from pathlib import Path
import json
import uuid
from datetime import datetime



class MetadataAI:
    """
    Advanced EPUB metadata generator.
    """



    def __init__(
        self,
        project_dir
    ):

        self.project_dir = Path(
            project_dir
        )


        self.config = {}

        self.load()



    def load(self):

        file = (

            self.project_dir
            /
            "book.json"

        )


        if file.exists():

            self.config = json.loads(

                file.read_text(

                    encoding="utf-8"

                )

            )



    def get(
        self,
        key,
        default=""
    ):

        return self.config.get(

            key,

            default

        )



    def generate_identifier(self):

        return (

            "urn:uuid:"

            +

            str(
                uuid.uuid4()
            )

        )



    def generate(self):

        """
        Create advanced metadata object.
        """


        metadata = {


            "identifier":

                self.generate_identifier(),



            "title":

                self.get(
                    "title",
                    "Untitled Book"
                ),



            "creator":

                self.get(
                    "author",
                    "Unknown"
                ),



            "publisher":

                self.get(
                    "publisher",
                    "EPUB Deluxe Publishing"
                ),



            "language":

                self.get(
                    "language",
                    "vi"
                ),



            "description":

                self.get(
                    "description",
                    ""
                ),



            "subject":

                self.get(
                    "subject",
                    []
                ),



            "keywords":

                self.get(
                    "keywords",
                    []
                ),



            "series":

                self.get(
                    "series",
                    ""
                ),



            "isbn":

                self.get(
                    "isbn",
                    ""
                ),



            "modified":

                datetime.utcnow()
                .strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                )

        }


        return metadata



    def save(
        self,
        output="metadata.json"
    ):


        data = self.generate()


        file = (

            self.project_dir
            /
            output

        )


        file.write_text(

            json.dumps(

                data,

                ensure_ascii=False,

                indent=4

            ),

            encoding="utf-8"

        )


        return file
