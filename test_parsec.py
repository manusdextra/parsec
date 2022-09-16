import unittest
from ddt import ddt, data, unpack
from parsec import parse

@ddt
class TestHeadings(unittest.TestCase):

    @unpack
    @data(
        ("# Hello\n",        "<h1>Hello</h1>\n"),
        ("## Hello\n",       "<h2>Hello</h2>\n"),
        ("### Hello\n",      "<h3>Hello</h3>\n"),
        ("#### Hello\n",     "<h4>Hello</h4>\n"),
        ("##### Hello\n",    "<h5>Hello</h5>\n"),
        ("###### Hello\n",   "<h6>Hello</h6>\n"),
    )
    def test_headings(self, inputs, expected):
        self.assertEqual(parse(inputs), expected)

@ddt
class TestLists(unittest.TestCase):

    @unpack
    @data(
            ("* this is a list item\n",       "<li>this is a list item</li>\n"),
            ("*this is not\n",                "*this is not\n"),
            ("- this is a list item\n",       "<li>this is a list item</li>\n"),
            ("-this is not\n",                "-this is not\n"),
    )
    def test_list_items(self, inputs, expected):
        self.assertEqual(parse(inputs), expected)

    @unpack
    @data(
            ("- this\n- is\n- one\n- list", "<ul><li>this</li><li>is</li><li>one</li><li>list</li></ul>"),
            ("# one\n- this\n- is\n# two\n- two\n- lists", "<h1>one</h1><ul><li>this</li><li>is</li></ul><h1>two</h1><ul><li>two</li><li>lists</li></ul>"),
    )
    def test_complete_lists(self, inputs, expected):
        self.assertEqual(parse(inputs), expected)
