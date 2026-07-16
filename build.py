# build.py

#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path


from core.pipeline import (
    DeluxePipeline
)



# Use package VERSION as single source of truth
try:
    from epub_deluxe import VERSION
except Exception:
    VERSION = "0.0.0"



def banner():

    print(
r"""
====================================

        EPUB DELUXE BUILDER

              v%s

====================================
""" % VERSION
    )



def run_build(args):


    project = Path(
        args.project
    )


    if not project.exists():

        print(

            "ERROR: Project folder not found"

        )

        sys.exit(1)



    pipeline = DeluxePipeline(

        project,

        args.output

    )


    try:

        result = pipeline.run(

            theme=args.theme

        )


        print()

        print(
            "SUCCESS:"
        )

        print(
            result
        )



    except Exception as error:


        print()

        print(
            "BUILD FAILED"
        )


        print(
            error
        )


        sys.exit(2)





def main():


    banner()



    parser = argparse.ArgumentParser(

        description=
        "EPUB Deluxe Builder"

    )



    parser.add_argument(

        "project",

        help=
        "Book project directory"

    )



    parser.add_argument(

        "-o",

        "--output",

        default=
        "deluxe_book.epub",

        help=
        "Output EPUB file"

    )



    parser.add_argument(

        "--theme",

        default=
        "classic",

        choices=[

            "classic",

            "modern",

            "dark",

            "sepia",

            "manga"

        ],

        help=
        "Reading theme"

    )



    parser.add_argument(

        "--version",

        action=
        "version",

        version=
        VERSION

    )



    args = parser.parse_args()



    run_build(args)





if __name__ == "__main__":

    main()
