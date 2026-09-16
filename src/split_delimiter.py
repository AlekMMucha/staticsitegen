from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        elif node.text_type == TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text)>1:
                if len(split_text)%2 == 0 :
                    raise Exception("The number of split parts is even, which means the delimiter is not balanced.")
                for i, text in enumerate(split_text):
                    if split_text[i] == "":
                        continue
                    if i %2 != 0:
                        new_list.append(TextNode(text, text_type))
                    else:
                        new_list.append(TextNode(text, TextType.TEXT))
            else:
                new_list.append(node)
    return new_list