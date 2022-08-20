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

if __name__ == "__main__":
    options = get_options()
    markdown = options.infile

