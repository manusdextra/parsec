from parsec import parse

class TestHeadings():
    def test_h1(self):
        assert parse("# Hello") == "<h1>Hello</h1>"
    def test_h2(self):
        assert parse("## Hello") == "<h2>Hello</h2>"
    def test_h3(self):
        assert parse("### Hello") == "<h3>Hello</h3>"
    def test_h4(self):
        assert parse("#### Hello") == "<h4>Hello</h4>"
    def test_h5(self):
        assert parse("##### Hello") == "<h5>Hello</h5>"
    def test_h6(self):
        assert parse("###### Hello") == "<h6>Hello</h6>"
