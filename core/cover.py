"""
core.cover

Cover image processing.

Responsibilities

- Load cover
- Validate image
- Convert to RGB
- Resize if needed
- Optimize JPEG
- Return bytes for EbookLib
"""

from __future__ import annotations

import io
from pathlib import Path

from PIL import Image


# ---------------------------------------------------------
# Constants
# ---------------------------------------------------------

MAX_WIDTH = 1600
MAX_HEIGHT = 2560

JPEG_QUALITY = 92

SUPPORTED_EXTENSIONS = {

    ".jpg",
    ".jpeg",
    ".png",
    ".webp",

}


# ---------------------------------------------------------
# Exception
# ---------------------------------------------------------

class CoverError(Exception):
    """Raised when cover image is invalid."""


# ---------------------------------------------------------
# Cover Processor
# ---------------------------------------------------------

class CoverProcessor:

    def __init__(
        self,
        max_width: int = MAX_WIDTH,
        max_height: int = MAX_HEIGHT,
    ):

        self.max_width = max_width
        self.max_height = max_height

    # -----------------------------------------------------

    def validate(
        self,
        path: Path,
    ) -> None:

        if not path.exists():
            raise CoverError("Cover file does not exist.")

        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise CoverError(
                f"Unsupported image format: {path.suffix}"
            )

    # -----------------------------------------------------

    def load(
        self,
        path: Path,
    ) -> Image.Image:

        self.validate(path)

        return Image.open(path)

    # -----------------------------------------------------

    def convert_rgb(
        self,
        image: Image.Image,
    ) -> Image.Image:

        if image.mode != "RGB":
            image = image.convert("RGB")

        return image

    # -----------------------------------------------------

    def resize(
        self,
        image: Image.Image,
    ) -> Image.Image:

        width, height = image.size

        ratio = min(

            self.max_width / width,

            self.max_height / height,

            1.0,

        )

        if ratio == 1.0:
            return image

        new_size = (

            int(width * ratio),

            int(height * ratio),

        )

        return image.resize(

            new_size,

            Image.LANCZOS,

        )

    # -----------------------------------------------------

    def export(
        self,
        image: Image.Image,
    ) -> bytes:

        stream = io.BytesIO()

        image.save(

            stream,

            format="JPEG",

            quality=JPEG_QUALITY,

            optimize=True,

        )

        return stream.getvalue()

    # -----------------------------------------------------

    def process(
        self,
        path: str | Path,
    ) -> bytes:

        image = self.load(Path(path))

        image = self.convert_rgb(image)

        image = self.resize(image)

        return self.export(image)


# ---------------------------------------------------------
# Public API
# ---------------------------------------------------------

_processor = CoverProcessor()


def load_cover(path: str | Path) -> bytes:
    """
    Load and optimize cover image.

    Returns
    -------
    bytes
        JPEG bytes ready for EbookLib.
    """

    return _processor.process(path)
