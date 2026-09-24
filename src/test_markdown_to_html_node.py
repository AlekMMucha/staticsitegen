import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    def test_ordered_list(self):
        md = "1. This is a **ORDERED LIST**\n2. testing if all _child_ HTML Nodes also known as **LeafNodes**\n3. `this should all be **unformatted** and _untouched_ `\n4. I am really hoping that this works :)"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.maxDiff = None
        self.assertEqual(
            html,
            "<div><ol><li>This is a <b>ORDERED LIST</b></li><li>testing if all <i>child</i> HTML Nodes also known as <b>LeafNodes</b></li><li><code>this should all be **unformatted** and _untouched_ </code></li><li>I am really hoping that this works :)</li></ol></div>"
        )
    def test_unordered_list(self):
        md = "- hello word **BOLDBOLDBOLD**.\n- _italic italic italic italic_.\n- thirdddddddd\n- cant forget newline\n- last one\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><ul><li>hello word <b>BOLDBOLDBOLD</b>.</li><li><i>italic italic italic italic</i>.</li><li>thirdddddddd</li><li>cant forget newline</li><li>last one</li></ul></div>")
    def test_heading(self):
        md = "### This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><h3>This is a heading</h3></div>")

        md2 = "###### **this heading is all bold**"
        node2 = markdown_to_html_node(md2)
        html2 = node2.to_html()
        self.assertEqual(html2,"<div><h6><b>this heading is all bold</b></h6></div>")
    def test_quote(self):
        md = ">hello\n> this is a quote block\n>BOOOYAHHH.\n>i can have children :) **bold** and _italic_."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><blockquote>hello\nthis is a quote block\nBOOOYAHHH.\ni can have children :) <b>bold</b> and <i>italic</i>.</blockquote></div>")