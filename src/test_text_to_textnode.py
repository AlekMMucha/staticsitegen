import unittest
from text_to_textnode import text_to_textnode
from textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnode(text)
        expected_result = [    TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),]

        self.assertEqual(result, expected_result)

        text2 = "This text has no special formatting, just plain text."
        result2 = text_to_textnode(text2)
        expected_result2 = [TextNode("This text has no special formatting, just plain text.", TextType.TEXT)]

        self.assertEqual(result2, expected_result2)

        text3="this text has a formatting error with an unbalanced **bold delimiter"
        self.assertRaises(Exception, text_to_textnode, text3)

        text4="this text has a formatting error with an unbalanced _italic delimiter"
        self.assertRaises(Exception, text_to_textnode, text4)

        text5="this text has a formatting error with an unbalanced `code delimiter"
        self.assertRaises(Exception, text_to_textnode, text5)

        text6="this text has a formatting error with an unbalanced **bold** and _italic delimiter"
        self.assertRaises(Exception, text_to_textnode, text6)

if __name__ == "__main__":
    unittest.main()