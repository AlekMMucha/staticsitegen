import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        n3 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, n3)

        n4 = TextNode("this is a node", TextType.CODE)
        self.assertNotEqual(node, n4)

        n5 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node, n5)

        n6 = TextNode("this is a node",TextType.CODE, "https://exampleurl.com")
        n7 = TextNode("this is a node",TextType.CODE, "https://exampleurl.com")
        self.assertNotEqual(n4, n6)
        self.assertEqual(n6, n7)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_repr = "TextNode(This is a text node, bold, None)"
        self.assertEqual(repr(node), expected_repr)

        node2 = TextNode("This is a link", TextType.LINK, "https://example.com")
        expected_repr2 = "TextNode(This is a link, link, https://example.com)"
        self.assertEqual(repr(node2), expected_repr2)

    def test_text_node_to_html_node(self):
        text_node = TextNode("this is plain text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is plain text")
        text_node2 = TextNode("this is Code", TextType.CODE)
        html_node2 = text_node_to_html_node(text_node2)
        self.assertEqual(html_node2.tag, "code")
        self.assertEqual(html_node2.value, "this is Code")
        text_node3 = TextNode("this is a link", TextType.LINK, "https://example.com")
        html_node3 = text_node_to_html_node(text_node3)
        self.assertEqual(html_node3.tag, "a")
        self.assertEqual(html_node3.value, "this is a link")
        self.assertEqual(html_node3.props, {"href": "https://example.com"})
        text_node4 = TextNode("this is an image", TextType.IMAGE, "https://example.com/image.png")
        html_node4 = text_node_to_html_node(text_node4)
        self.assertEqual(html_node4.tag, "img")
        self.assertEqual(html_node4.value, None)
        self.assertEqual(html_node4.props, {"src": "https://example.com/image.png", "alt": "this is an image"})

if __name__ == "__main__":
    unittest.main()