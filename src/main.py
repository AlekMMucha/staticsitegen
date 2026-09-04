def main():
    from textnode import TextNode, TextType
    text_node1 = TextNode("Hello, World!", TextType.TEXT)
    print(repr(text_node1))  # Output: TextNode(Hello, World!,text,None)
    text_node2 = TextNode("this is bold", TextType.BOLD, "https://example.com")
    print(repr(text_node2))  # Output: TextNode(this is bold,bold,https://example.com)

main()