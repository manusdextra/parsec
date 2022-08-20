from parsec import parse

def test_headings():
    assert parse("# Hello") == "<h1>Hello</h1>"
