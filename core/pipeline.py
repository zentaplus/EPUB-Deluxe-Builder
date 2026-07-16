# core/pipeline.py

from pathlib import Path


from features.chapter import (
    ChapterProcessor
)

from features.cover import (
    CoverBuilder
)

from features.image_opt import (
    ImageOptimizer
)

from features.typography import (
    TypographyBuilder
)

from features.theme import (
    ThemeBuilder
)

from features.kindle import (
    KindleChecker
)


from core.builder import (
    EPUBBuilder
)

from core.validator import (
    EPUBValidator
)



class DeluxePipeline:
    """
    Complete EPUB Deluxe build pipeline.
    """



    def __init__(
        self,
        project_dir,
        output_file
    ):

        self.project_dir = Path(
            project_dir
        )


        self.output_file = Path(
            output_file
        )


        self.logs = []



    def log(self, message):

        self.logs.append(
            message
        )

        print(
            message
        )



    def process_chapters(self):

        self.log(
            "[1] Processing chapters..."
        )


        processor = ChapterProcessor(

            self.project_dir
            /
            "content/chapters"

        )


        processor.process_all()



    def process_cover(self):

        self.log(
            "[2] Building cover..."
        )


        cover = CoverBuilder(

            self.project_dir

        )


        cover.build()



    def optimize_images(self):

        self.log(
            "[3] Optimizing images..."
        )


        optimizer = ImageOptimizer(

            self.project_dir
            /
            "content/images"

        )


        optimizer.optimize_all()



    def build_typography(
        self
    ):

        self.log(
            "[4] Generating typography..."
        )


        typography = TypographyBuilder(

            self.project_dir

        )


        typography.save()



    def apply_theme(
        self,
        theme="classic"
    ):

        self.log(
            "[5] Applying theme..."
        )


        theme_builder = ThemeBuilder(

            self.project_dir

        )


        theme_builder.save(
            theme
        )



    def check_kindle(self):

        self.log(
            "[6] Checking Kindle compatibility..."
        )


        checker = KindleChecker(

            self.project_dir

        )


        result = checker.validate()


        if not result["compatible"]:

            raise Exception(

                result["errors"]

            )



    def build_epub(self):

        self.log(
            "[7] Building EPUB..."
        )


        builder = EPUBBuilder(

            self.project_dir,

            self.output_file

        )


        return builder.build()



    def validate(self):

        self.log(
            "[8] Validating EPUB..."
        )


        validator = EPUBValidator(

            self.project_dir

        )


        return validator.validate()



    def run(
        self,
        theme="classic"
    ):

        self.log(

            "=== EPUB Deluxe Pipeline ==="

        )


        self.process_chapters()

        self.process_cover()

        self.optimize_images()

        self.build_typography()

        self.apply_theme(
            theme
        )

        self.check_kindle()


        epub = self.build_epub()


        self.validate()



        self.log(

            "=== BUILD COMPLETE ==="

        )


        return epub
