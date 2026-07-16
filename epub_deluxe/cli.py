# epub_deluxe/cli.py

import argparse

from pathlib import Path


from core.pipeline import (
    DeluxePipeline
)


from .version import VERSION



def main():


    parser = argparse.ArgumentParser(

        prog="epub-deluxe",

        description=
        "Professional EPUB Builder"

    )


    parser.add_argument(

        "command",

        choices=[

            "build",

            "version"

        ]

    )


    parser.add_argument(

        "project",

        nargs="?"

    )


    parser.add_argument(

        "-o",

        "--output",

        default="book.epub"

    )


    parser.add_argument(

        "--theme",

        default="classic"

    )


    args = parser.parse_args()



    if args.command == "version":

        print(

            VERSION

        )

        return



    if args.command == "build":


        if not args.project:

            print(
                "Missing project folder"
            )

            return



        pipeline = DeluxePipeline(

            Path(args.project),

            Path(args.output)

        )


        pipeline.run(

            theme=args.theme

        )
