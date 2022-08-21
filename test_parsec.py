import unittest
from ddt import ddt, data, unpack
from parsec import parse

@ddt
class TestHeadings(unittest.TestCase):

    @unpack
    @data(
        ("# Hello",        "<h1>Hello</h1>"),
        ("## Hello",       "<h2>Hello</h2>"),
        ("### Hello",      "<h3>Hello</h3>"),
        ("#### Hello",     "<h4>Hello</h4>"),
        ("##### Hello",    "<h5>Hello</h5>"),
        ("###### Hello",   "<h6>Hello</h6>"),
    )
    def test_headings(self, inputs, expected):
        self.assertEqual(parse(inputs), expected)

@ddt
class TestLists(unittest.TestCase):

    @unpack
    @data(
            ("* this is a list item",       "<li>this is a list item</li>"),
            ("*this is not",                "*this is not"),
            ("- this is a list item",       "<li>this is a list item</li>"),
            ("-this is not",                "*this is not"),
            ("- this\n- is\n- one\n- list", "<ul><li>this</li><li>is</li><li>one</li><li>list</li></ul>"),
            ("# one\n- this\n- is\n# two\n- two\n- lists", "<h1>one</h1><ul><li>this</li><li>is</li></ul><h1>two</h1><ul><li>two</li><li>lists</li></ul>"),
    )
    def test_lists(self, inputs, expected):
        self.assertEqual(parse(inputs), expected)
