def markdown_to_blocks(markdown_text):
    split_markdown = markdown_text.split("\n\n")
    split_markdown_final = []
    for block in split_markdown:
        if block.strip("\n") == "":
            continue
        split_markdown_final.append(block.strip())
    return split_markdown_final