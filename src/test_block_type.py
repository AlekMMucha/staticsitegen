import unittest
from block_type import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\nCode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### this is not a heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1. This is not an ordered list\n- This is not an unordered list"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("```\nThis is not a code block"), BlockType.PARAGRAPH)
        self.assertNotEqual(block_to_block_type("This is a paragraph."), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("1. Ordered list item"), BlockType.UNORDERED_LIST)
        self.assertNotEqual(block_to_block_type("##this is not a heading"), BlockType.HEADING)

if __name__ == '__main__':
    unittest.main()
