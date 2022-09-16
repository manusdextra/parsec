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

# block_level_patterns = {
#    r"\A(\s*[\-\*]\s*)(.*)$": "\n",
#    r"\A(>\s)(.*)$"         : "\n",
#    r"\A(.*)$"              : "[\-=]{3,}",
# }

single_line_patterns = {
    # headings
    r"^(#{6} )(.*)$"  : r"<h6>\2</h6>\n",
    r"^(#{5} )(.*)$"  : r"<h5>\2</h5>\n",
    r"^(#{4} )(.*)$"  : r"<h4>\2</h4>\n",
    r"^(#{3} )(.*)$"  : r"<h3>\2</h3>\n",
    r"^(#{2} )(.*)$"  : r"<h2>\2</h2>\n",
    r"^(# )(.*)$"     : r"<h1>\2</h1>\n",
}


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
    markdown = markdown.split('\n')
    html = ""
    """
    Procedure:
    - go through markdown line by line
    - if multiline pattern is detected, add line to holding space and read in next one
    - if any following line doesn't match the same pattern, process the holding space and
      clear it
    - Note: Would it be worth it using a manual for loop that can reset the index to an earlier line?

    TODO:
    - [ ] expand multiline_patterns to include flags?
          or a second regex to be applied to the entire holding space?
    """
    while markdown:
        buffer = ""
        line = markdown[0]
        for key, val in single_line_patterns.items():
            line = re.sub(key, val, line)
        buffer += line
        html += buffer
        del markdown[0]

    return html

if __name__ == "__main__":
    options = get_options()
    markdown = options.infile
    parse(markdown)
