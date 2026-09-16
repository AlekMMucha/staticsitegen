import unittest
from extract_link_and_img import extract_markdown_images, extract_markdown_links

class TestLinkAndImageExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "BLAHBLLAHBLAH yes this is a link [link text](https://example.com) and this is an image ![alt text](https://example.com/image.png) and another image ![another alt](https://example.com/another_image.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "https://example.com/image.png"), ("another alt", "https://example.com/another_image.jpg")])

        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        text = "BLAHBLAHBLAH yes this is a link [link text](https://example.com) and this is an image ![alt text](https://example.com/image.png) and another link [another link](https://example.com/another_page)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link text", "https://example.com"), ("another link", "https://example.com/another_page")])

if __name__ == "__main__":
    unittest.main()