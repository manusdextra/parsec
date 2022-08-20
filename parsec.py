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

def wrap(section, brackets):
    """ wrap section in brackets """
    return f"<{brackets}>{section}</{brackets}>"

def parse(markdown):
    """ main loop """
    regex_collection = {
        r"\A(# )(.*)"     : "h1",
        r"\A(#{2} )(.*)"  : "h2",
        r"\A(#{3} )(.*)"  : "h3",
        r"\A(#{4} )(.*)"  : "h4",
        r"\A(#{5} )(.*)"  : "h5",
        r"\A(#{6} )(.*)"  : "h6",
    }

    for pattern in regex_collection:
        match = re.search(pattern, markdown)
        if match:
            return wrap(match.group(2), regex_collection[pattern])

if __name__ == "__main__":
    options = get_options()
    markdown = options.infile
    parse(markdown)
