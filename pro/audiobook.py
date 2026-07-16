# pro/audiobook.py

from pathlib import Path
import re


class AudioBookBuilder:
    """
    EPUB 3 Media Overlay generator.
    """


    def __init__(
        self,
        project_dir
    ):

        self.project_dir = Path(
            project_dir
        )


        self.audio_dir = (

            self.project_dir
            /
            "content/audio"

        )


        self.chapter_dir = (

            self.project_dir
            /
            "content/chapters"

        )


        self.overlay_dir = (

            self.project_dir
            /
            "content/overlays"

        )



    def scan_audio(self):

        """
        Find audio files.
        """

        if not self.audio_dir.exists():

            return []


        return list(

            self.audio_dir.glob(
                "*.mp3"
            )

        )



    def extract_paragraphs(
        self,
        chapter
    ):

        """
        Extract text blocks.
        """

        text = chapter.read_text(

            encoding="utf-8"

        )


        paragraphs = re.findall(

            r"<p.*?>(.*?)</p>",

            text,

            re.S | re.I

        )


        return paragraphs



    def create_smil(
        self,
        chapter,
        audio
    ):

        """
        Generate SMIL synchronization file.
        """

        self.overlay_dir.mkdir(

            parents=True,

            exist_ok=True

        )


        name = chapter.stem


        paragraphs = self.extract_paragraphs(

            chapter

        )


        seq = []


        for index, paragraph in enumerate(

            paragraphs

        ):


            seq.append(

f"""
<par>

<text src="../chapters/{chapter.name}#p{index+1}"/>


<audio

src="../audio/{audio.name}"

clipBegin="{index*5}s"

clipEnd="{(index+1)*5}s"

/>


</par>
"""

            )



        smil = f"""<?xml version="1.0"
encoding="UTF-8"?>


<smil

xmlns="http://www.w3.org/ns/SMIL">


<body>


<seq>

{''.join(seq)}

</seq>


</body>


</smil>
"""


        output = (

            self.overlay_dir
            /
            f"{name}.smil"

        )


        output.write_text(

            smil,

            encoding="utf-8"

        )


        return output



    def build(self):

        """
        Generate all SMIL files.
        """

        audio_files = self.scan_audio()


        chapters = sorted(

            self.chapter_dir.glob(
                "*.xhtml"
            )

        )


        results = []


        for chapter, audio in zip(

            chapters,

            audio_files

        ):

            results.append(

                self.create_smil(

                    chapter,

                    audio

                )

            )


        return results
