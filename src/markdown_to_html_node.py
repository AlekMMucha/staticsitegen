from markdown_to_blocks import markdown_to_blocks
from block_type import BlockType,block_to_block_type
from htmlnode import HTMLNode,ParentNode
from text_to_textnode import text_to_textnode
from textnode import text_node_to_html_node,TextNode,TextType
import re

def text_to_children(text) -> list[HTMLNode]:
    text_nodes = text_to_textnode(text)
    new_list = []
    for node in text_nodes:
        new_list.append(text_node_to_html_node(node))
    return new_list

def markdown_to_html_node(markdown_text):
    list_of_converted_blocks =[]
    blocks = markdown_to_blocks(markdown_text)
    for block in blocks:
        block_type = block_to_block_type(block)
        ##Maybe practice by making use of helper functions in this block of ifs
        if block_type == BlockType.HEADING:
            start_of_block, rest_of_block = block.split(" ",1)
            tag = f"h{len(start_of_block)}"
            children:list[HTMLNode] = text_to_children(rest_of_block)
            new_block_node = ParentNode(tag,children,None)
        elif block_type == BlockType.QUOTE:
            splitlines_block = block.splitlines()
            clean_lines_list = [re.sub(r"^>\s?", "", line) for line in splitlines_block]
            clean_block = "\n".join(clean_lines_list)
            children = text_to_children(clean_block)
            new_block_node = ParentNode("blockquote",children,None)
        elif block_type == BlockType.CODE:
            content = re.sub(r"```\s*$", "",block.split("\n",1)[1])
            textnode = TextNode(content,TextType.CODE)
            new_block_node = ParentNode("pre",[text_node_to_html_node(textnode)],None)
        elif block_type == BlockType.UNORDERED_LIST:
            splitlines_block = block.splitlines()
            lines_without_symbol = [line.split(" ",1)[1] for line in splitlines_block]
            list_of_children = [ParentNode("li",text_to_children(line),None) for line in lines_without_symbol]
            new_block_node = ParentNode("ul",list_of_children,None)
        elif block_type == BlockType.ORDERED_LIST:
            splitlines_block = block.splitlines()
            lines_without_symbol = [line.split(" ",1)[1] for line in splitlines_block]
            list_of_children = [ParentNode("li",text_to_children(line),None) for line in lines_without_symbol]
            new_block_node = ParentNode("ol",list_of_children,None)
        elif block_type == BlockType.PARAGRAPH:
            split_block = block.split("\n")
            rejoined_block = " ".join(split_block)
            children = text_to_children(rejoined_block)
            new_block_node = ParentNode("p",children,None)
        else:
            raise Exception("error while parsing html node blocks")
        list_of_converted_blocks.append(new_block_node)
    div_node = ParentNode("div",list_of_converted_blocks,None)
    return div_node
