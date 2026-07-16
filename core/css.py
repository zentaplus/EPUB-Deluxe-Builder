"""
core.css

Generate professional CSS stylesheet for EPUB 3.

Compatible with:

- Apple Books
- Kobo
- Google Play Books
- Moon+ Reader
- ReadEra
"""

from __future__ import annotations


DEFAULT_CSS = """
/* ==========================================================
   EPUB Deluxe Builder
   ========================================================== */

html{
    margin:0;
    padding:0;
}

body{

    margin-top:5%;

    margin-bottom:5%;

    margin-left:6%;

    margin-right:6%;

    line-height:1.75;

    text-align:justify;

    font-family:serif;

    widows:2;

    orphans:2;

    -epub-hyphens:auto;

}

h1{

    text-align:center;

    font-size:1.8em;

    margin-top:2em;

    margin-bottom:1.5em;

    page-break-before:always;

    font-weight:bold;

}

h2{

    text-align:center;

    margin-top:1.5em;

    margin-bottom:1em;

}

p{

    margin-top:0;

    margin-bottom:0.7em;

    text-indent:2em;

}

.cover{

    margin:0;

    padding:0;

    text-align:center;

}

.cover img{

    display:block;

    width:100%;

    height:auto;

}

.title-page{

    text-align:center;

    margin-top:25%;

}

.title-page h1{

    page-break-before:auto;

    font-size:2em;

}

.title-page h2{

    font-weight:normal;

}

.info{

    margin-top:2em;

}

.info table{

    width:100%;

    border-collapse:collapse;

}

.info td{

    padding:0.4em;

    vertical-align:top;

}

blockquote{

    margin-left:2em;

    margin-right:2em;

    font-style:italic;

}

hr{

    border:none;

    border-top:1px solid #999;

    margin:2em 0;

}

img{

    max-width:100%;

    height:auto;

}

code{

    font-family:monospace;

}

pre{

    white-space:pre-wrap;

}

.small{

    font-size:0.9em;

}

.center{

    text-align:center;

}

.right{

    text-align:right;

}

.left{

    text-align:left;

}
"""


# ---------------------------------------------------------
# Public API
# ---------------------------------------------------------

def get_css() -> str:
    """
    Return default stylesheet.
    """
    return DEFAULT_CSS


def get_css_bytes() -> bytes:
    """
    Return UTF-8 encoded stylesheet.
    """
    return DEFAULT_CSS.encode("utf-8")
