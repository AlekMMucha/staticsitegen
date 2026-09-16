import unittest
from split_link_and_img import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class testSplittingImgAndLink(unittest.TestCase):
    def test_split_nodes_image(self):
        old_nodes1 = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes1 = split_nodes_image([old_nodes1])
        expected_nodes1 = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(new_nodes1, expected_nodes1)

        new_nodes2 = split_nodes_image([TextNode("This is text with no images", TextType.TEXT),
                                        TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
                                        TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
                                        TextNode("this is bold text", TextType.BOLD),
                                        TextNode("this is italic text", TextType.ITALIC),
                                        TextNode("this is code text", TextType.CODE),])
        expected_nodes2 = [
            TextNode("This is text with no images", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode("this is bold text", TextType.BOLD),
            TextNode("this is italic text", TextType.ITALIC),
            TextNode("this is code text", TextType.CODE),]
        self.assertEqual(new_nodes2, expected_nodes2)

    def test_split_nodes_link(self):
        old_nodes1 = TextNode("This is text with a [link](https://example.com) and another [second link](https://example.com/second)",
        TextType.TEXT,
        )
        new_nodes1 = split_nodes_link([old_nodes1])
        expected_nodes1 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.com/second"),
        ]
        self.assertEqual(new_nodes1, expected_nodes1)

        new_nodes2 = split_nodes_link([TextNode("This is text with no links", TextType.TEXT),
                                        TextNode("This is text with a [link](https://example.com)", TextType.TEXT),
                                        TextNode("This is text with a [link](https://example.com) and another [second link](https://example.com/second)", TextType.TEXT),
                                        TextNode("this is bold text", TextType.BOLD),
                                        TextNode("this is italic text", TextType.ITALIC),
                                        TextNode("this is code text", TextType.CODE),])
        expected_nodes2 = [
            TextNode("This is text with no links", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.com/second"),
            TextNode("this is bold text", TextType.BOLD),
            TextNode("this is italic text", TextType.ITALIC),
            TextNode("this is code text", TextType.CODE),]
        self.assertEqual(new_nodes2, expected_nodes2)
if __name__ == "__main__":
    unittest.main()