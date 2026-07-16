#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
====================================================

EPUB Deluxe Builder Pro

Entry Point

====================================================
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent

OUTPUT_DIR = PROJECT_ROOT / "output"

RESOURCES_DIR = PROJECT_ROOT / "resources"

CORE_DIR = PROJECT_ROOT / "core"

GUI_DIR = PROJECT_ROOT / "gui"


def ensure_directories() -> None:
    """
    Create required directories if missing.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    RESOURCES_DIR.mkdir(exist_ok=True)

    CORE_DIR.mkdir(exist_ok=True)

    GUI_DIR.mkdir(exist_ok=True)


def print_banner() -> None:

    print()

    print("=" * 60)

    print("EPUB Deluxe Builder Pro")

    print("Version : 0.1.0")

    print("=" * 60)

    print()


def check_dependencies() -> None:

    missing = []

    try:
        import ebooklib
    except ImportError:
        missing.append("ebooklib")

    try:
        import PIL
    except ImportError:
        missing.append("Pillow")

    try:
        import bs4
    except ImportError:
        missing.append("beautifulsoup4")

    if missing:

        print()

        print("Missing packages:")

        for pkg in missing:
            print(" -", pkg)

        print()

        print("Install with:")

        print()

        print("pip install -r requirements.txt")

        print()

        sys.exit(1)


def main():

    print_banner()

    ensure_directories()

    check_dependencies()

    print("Environment OK.")

    print()

    print("Next step:")

    print("Implement GUI.")

    print()

    print("Project root :")

    print(PROJECT_ROOT)

    print()

    print("Output folder :")

    print(OUTPUT_DIR)

    print()

    print("Ready.")


if __name__ == "__main__":
    main()
