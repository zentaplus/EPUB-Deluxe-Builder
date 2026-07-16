# core/manifest.py

from pathlib import Path
import mimetypes
import re


class ManifestBuilder:
    """
    Generate EPUB manifest items.
    """


    def __init__(self, epub_dir):

        self.epub_dir = Path(epub_dir)

        self.items = []


    def _detect_media_type(self, file):

        ext = file.suffix.lower()


        mapping = {

            ".xhtml":
                "application/xhtml+xml",

            ".html":
                "text/html",

            ".css":
                "text/css",

            ".jpg":
                "image/jpeg",

            ".jpeg":
                "image/jpeg",

            ".png":
                "image/png",

            ".svg":
                "image/svg+xml",

            ".woff":
                "font/woff",

            ".woff2":
                "font/woff2",

            ".ttf":
                "font/ttf",

            ".otf":
                "font/otf",

            ".ncx":
                "application/x-dtbncx+xml"

        }


        if ext in mapping:

            return mapping[ext]


        mime, _ = mimetypes.guess_type(
            str(file)
        )

        return mime or "application/octet-stream"



    def _create_id(self, path):

        name = str(path)

        name = re.sub(
            r"[^a-zA-Z0-9]",
            "_",
            name
        )

        return name.lower()



    def scan(self):

        self.items.clear()


        for file in self.epub_dir.rglob("*"):


            if not file.is_file():
                continue


            relative = file.relative_to(
                self.epub_dir
            )


            # bỏ package.opf
            if relative.name == "package.opf":
                continue


            item = {

                "id":
                    self._create_id(relative),

                "href":
                    str(relative)
                    .replace("\\", "/"),

                "media-type":
                    self._detect_media_type(file)

            }


            self.items.append(item)


        return self.items



    def build_xml(self):

        self.scan()


        result = [
            "<manifest>"
        ]


        for item in self.items:

            result.append(

                f"""
<item
 id="{item['id']}"
 href="{item['href']}"
 media-type="{item['media-type']}"/>
"""
            )


        result.append(
            "</manifest>"
        )


        return "\n".join(result)



    def update(self, opf_file):

        content = opf_file.read_text(
            encoding="utf-8"
        )


        manifest_xml = self.build_xml()


        content = re.sub(

            r"<manifest>.*?</manifest>",

            manifest_xml,

            content,

            flags=re.S

        )


        opf_file.write_text(

            content,

            encoding="utf-8"

        )
