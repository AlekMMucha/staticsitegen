import unittest
from htmlnode import HTMLNode,LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_value(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        expected_html = ' class="container" id="main"'
        node2 = HTMLNode(tag="span", props={"style": "color: red;"})
        self.assertEqual(node.props_to_html(), expected_html)
        self.assertNotEqual(node2.props_to_html(), expected_html)
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode(tag="div", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello, World!", props={"class": "text"})
        node2 = HTMLNode(tag="p", value="Hello, World!", props={"class": "text"})
        self.assertEqual(repr(node), repr(node2))
        expected_repr = "HTMLNode(tag=p, value=Hello, World!, children=None, props={'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)

    def test_Leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("span", "this is a span", {"class": "highlight"})
        node3 = LeafNode("span", "this is a span", {"href": "https://example.com"})
        self.assertEqual(node2.to_html(), '<span class="highlight">this is a span</span>')
        self.assertNotEqual(node2.to_html(), node3.to_html())
        self.assertEqual(node3.to_html(), '<span href="https://example.com">this is a span</span>')

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")

def test_to_html_with_grandchildren_and_props(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node], {"class": "highlight"})
    parent_node = ParentNode("div", [child_node], {"id": "container"})
    self.assertEqual(parent_node.to_html(),'<div id="container"><span class="highlight"><b>grandchild</b></span></div>')

def test_to_html_with_multiple_children(self):
    child_node1 = LeafNode("span", "child1")
    child_node2 = LeafNode("p", "child2")
    parent_node = ParentNode("div", [child_node1, child_node2])
    self.assertEqual(parent_node.to_html(), '<div><span>child1</span><p>child2</p></div>')

def test_to_html_with_multiple_children_and_props(self):
    child_node1 = LeafNode("span", "child1", {"class": "highlight"})
    child_node2 = LeafNode("p", "child2", {"id": "paragraph"})
    parent_node = ParentNode("div", [child_node1, child_node2], {"style": "color: red;"})
    self.assertEqual(parent_node.to_html(), '<div style="color: red;"><span class="highlight">child1</span><p id="paragraph">child2</p></div>')

if __name__ == "__main__":
    unittest.main()