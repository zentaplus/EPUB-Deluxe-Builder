# build.py

#!/usr/bin/env python3

from pathlib import Path
import argparse
import sys


from core.builder import EPUBBuilder
from core.validator import EPUBValidator



VERSION = "1.0.0"



def print_banner():

    print(
r"""
=================================
     EPUB Deluxe Builder
          v1.0.0
=================================
"""
    )



def build_epub(
    project,
    output,
    validate=True
):


    project = Path(project)

    output = Path(output)


    if not project.exists():

        print(
            f"ERROR: Project not found: {project}"
        )

        sys.exit(1)



    print(
        "[1/3] Building EPUB..."
    )


    builder = EPUBBuilder(

        project,

        output

    )


    result = builder.build()


    print(

        f"Created: {result}"

    )



    if validate:


        print(
            "[2/3] Validating..."
        )


        validator = EPUBValidator(

            builder.temp_dir

        )


        report = validator.validate()



        if not report["valid"]:


            print(
                "Validation FAILED"
            )


            for error in report["errors"]:

                print(
                    " -",
                    error
                )


            sys.exit(2)



        else:

            print(
                "Validation PASSED"
            )



    print(

        "[3/3] Done."

    )



def main():

    print_banner()


    parser = argparse.ArgumentParser(

        description=
        "EPUB Deluxe Builder"

    )


    parser.add_argument(

        "project",

        help=
        "EPUB project folder"

    )


    parser.add_argument(

        "-o",

        "--output",

        default=
        "output.epub",

        help=
        "Output EPUB filename"

    )


    parser.add_argument(

        "--no-validate",

        action=
        "store_true",

        help=
        "Disable validation"

    )


    parser.add_argument(

        "--version",

        action=
        "version",

        version=
        VERSION

    )


    args = parser.parse_args()



    build_epub(

        args.project,

        args.output,

        not args.no_validate

    )



if __name__ == "__main__":

    main()
