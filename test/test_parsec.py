import unittest
from ddt import ddt, data, unpack
from parsec import parse


@ddt
class TestHeadings(unittest.TestCase):
    @unpack
    @data(
        ("# Hello", "<h1>Hello</h1>\n\n"),
        ("## Hello", "<h2>Hello</h2>\n\n"),
        ("### Hello", "<h3>Hello</h3>\n\n"),
        ("#### Hello", "<h4>Hello</h4>\n\n"),
        ("##### Hello", "<h5>Hello</h5>\n\n"),
        ("###### Hello", "<h6>Hello</h6>\n\n"),
    )
    def test_headings(self, inputs, expected):
        self.assertEqual(parse(inputs), expected)


@ddt
class TestLists(unittest.TestCase):
    @unpack
    @data(
        ("* this is a list item", "<ul>\n<li>this is a list item</li>\n</ul>\n\n"),
        ("*this is not", "*this is not"),
        ("- this is a list item", "<ul>\n<li>this is a list item</li>\n</ul>\n\n"),
        ("-this is not", "-this is not"),
    )
    def test_list_items(self, inputs, expected):
        self.assertEqual(parse(inputs), expected)

    # @unpack
    # @data(
    #     (
    #         "- one\n- list\n",
    #         "<ul>\n<li>one</li>\n<li>list</li>\n</ul>\n\n",
    #     ),
    #     (
    #         "# one\nhello\n",
    #         "<h1>one</h1>\n\nhello",
    #     ),
    #     # (
    #     #     "# one\n- this\n- is\n# two\n- two\n- lists\n",
    #     #     "<h1>one</h1>\n<ul><li>this</li>\n<li>is</li>\n</ul>\n<h1>two</h1>\n<ul><li>two</li>\n<li>lists</li></ul>\n",
    #     # ),
    # )
    # def test_complete_lists(self, inputs, expected):
    #     self.assertEqual(parse(inputs), expected)
