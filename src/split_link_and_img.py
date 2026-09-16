from textnode import TextNode, TextType
from extract_link_and_img import extract_markdown_images,extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        elif node.text_type == TextType.TEXT:
            images:list[tuple] = extract_markdown_images(node.text)
            for alt_text, url in images:
                sections = node.text.split(f"![{alt_text}]({url})", 1)
                if sections[0] != "":
                    new_list.append(TextNode(sections[0], TextType.TEXT))
                new_list.append(TextNode(alt_text,TextType.IMAGE,url))
                node.text = sections[1]
            if node.text != "":
                new_list.append(TextNode(node.text, TextType.TEXT))
    return new_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        elif node.text_type == TextType.TEXT:
            links:list[tuple] = extract_markdown_links(node.text)
            for cover_text, url in links:
                sections = node.text.split(f"[{cover_text}]({url})", 1)
                if sections[0] != "":
                    new_list.append(TextNode(sections[0], TextType.TEXT))
                new_list.append(TextNode(cover_text,TextType.LINK,url))
                node.text = sections[1]
            if node.text != "":
                new_list.append(TextNode(node.text, TextType.TEXT))
    return new_list
