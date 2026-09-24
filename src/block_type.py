from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith("> ") or line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.splitlines()):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(str(i) + ". ") for i, line in enumerate(block.splitlines(), start=1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH