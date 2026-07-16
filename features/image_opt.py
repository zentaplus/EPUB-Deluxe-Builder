# features/image_opt.py

from pathlib import Path
from PIL import Image


class ImageOptimizer:
    """
    Optimize images for EPUB.
    """


    def __init__(
        self,
        image_dir
    ):

        self.image_dir = Path(
            image_dir
        )


        self.supported = [

            ".jpg",
            ".jpeg",
            ".png",
            ".webp"

        ]


        self.processed = []



    def scan(self):

        """
        Find all images.
        """

        images = []


        if not self.image_dir.exists():

            return images


        for file in self.image_dir.rglob("*"):

            if (

                file.is_file()

                and

                file.suffix.lower()
                in self.supported

            ):

                images.append(file)


        return images



    def resize(
        self,
        image,
        max_width=1600
    ):

        """
        Resize large images.
        """

        img = Image.open(
            image
        )


        width, height = img.size


        if width <= max_width:

            return False



        ratio = (
            max_width
            /
            width
        )


        new_size = (

            max_width,

            int(
                height * ratio
            )

        )


        img = img.resize(

            new_size,

            Image.LANCZOS

        )


        img.save(
            image
        )


        return True



    def compress_jpeg(
        self,
        image,
        quality=85
    ):

        """
        Compress JPEG images.
        """

        if image.suffix.lower() not in [

            ".jpg",
            ".jpeg"

        ]:

            return False



        img = Image.open(
            image
        )


        img.save(

            image,

            optimize=True,

            quality=quality

        )


        return True



    def compress_png(
        self,
        image
    ):

        """
        Optimize PNG.
        """

        if image.suffix.lower() != ".png":

            return False


        img = Image.open(
            image
        )


        img.save(

            image,

            optimize=True

        )


        return True



    def create_thumbnail(
        self,
        image,
        size=(300,400)
    ):

        """
        Create preview image.
        """


        img = Image.open(
            image
        )


        img.thumbnail(
            size
        )


        output = (

            image.parent

            /

            (
                image.stem
                +
                "_thumb"
                +
                image.suffix

            )

        )


        img.save(
            output
        )


        return output



    def optimize_all(self):

        """
        Run optimization pipeline.
        """

        images = self.scan()


        for image in images:


            self.resize(
                image
            )


            if image.suffix.lower() in [

                ".jpg",
                ".jpeg"

            ]:

                self.compress_jpeg(
                    image
                )


            elif image.suffix.lower() == ".png":

                self.compress_png(
                    image
                )


            self.processed.append(
                image
            )


        return self.processed
