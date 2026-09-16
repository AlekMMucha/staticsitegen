import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter(self):
        old_nodes = [
            TextNode("this is *bold* text", TextType.TEXT),
            TextNode("this is _italic_ text", TextType.TEXT),
            TextNode("this is `code` text", TextType.TEXT), 
            TextNode("*bold* text *bold*", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        expected_nodes = [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("this is _italic_ text", TextType.TEXT),
            TextNode("this is `code` text", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected_nodes)

        old_nodes2 = [
            TextNode("this is *bold* text", TextType.TEXT),
            TextNode("this is _italic_ text", TextType.TEXT),
            TextNode("this is `code` text", TextType.TEXT), 
            TextNode("*bold* text *bold*", TextType.TEXT)
        ]
        new_nodes2 = split_nodes_delimiter(old_nodes2, "_", TextType.ITALIC)
        expected_nodes2 = [
            TextNode("this is *bold* text", TextType.TEXT),
            TextNode("this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            TextNode("this is `code` text", TextType.TEXT),
            TextNode("*bold* text *bold*", TextType.TEXT)
        ]
        self.assertEqual(new_nodes2, expected_nodes2)

        old_nodes3 = [
            TextNode("this is *bold* text*", TextType.TEXT),
            TextNode("this is _italic_ text", TextType.TEXT),
            TextNode("this is `code` text", TextType.TEXT), 
            TextNode("*bold* text *bold*", TextType.TEXT)
        ]
        self.assertRaises(Exception, split_nodes_delimiter, old_nodes3, "*", TextType.BOLD)
        ##checking to see if the exception is raised when the number of split parts is even, which means the delimiter is not balanced.

if __name__ == "__main__":
    unittest.main()