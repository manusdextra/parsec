#!/usr/bin/env python3

""" Markdown parser.

I wrote this initially to practice Python, and then found out I could
actually use it for other projects, so I decided to flesh it out.
The goal (for now) is to implement the "Basic Syntax" according to
markdownguide.org, and follow the best practice described there.

In the short term, I will focus on:
    - [ ] headings
    - [ ] text styles
    - [ ] paragraphs
    - [ ] lists
"""

import argparse
import pathlib
import re

def get_options():
    parser = argparse.ArgumentParser(
            description="Parse markdown file and output HTML"
    )
    parser.add_argument(
            "infile",
            type=pathlib.Path,
            help="Path to Markdown formatted file to be converted to HTML"
    )
    return parser.parse_args()

def parse(markdown):
    """ main loop """
    inline_patterns = {
        # headings
        r"\A(# )(.*)"     : r"<h1>\2</h1>",
        r"\A(#{2} )(.*)"  : r"<h2>\2</h2>",
        r"\A(#{3} )(.*)"  : r"<h3>\2</h3>",
        r"\A(#{4} )(.*)"  : r"<h4>\2</h4>",
        r"\A(#{5} )(.*)"  : r"<h5>\2</h5>",
        r"\A(#{6} )(.*)"  : r"<h6>\2</h6>",
    }

    for pattern in inline_patterns:
        markdown = re.sub(pattern, inline_patterns[pattern], markdown)
    return markdown

if __name__ == "__main__":
    options = get_options()
    markdown = options.infile
    parse(markdown)
