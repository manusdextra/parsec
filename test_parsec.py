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

