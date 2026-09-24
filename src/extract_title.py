import re
def extract_title(markdown):
    matches = re.findall(r"^#\s+(.+)", markdown, re.MULTILINE)
    if len(matches)==0:
        raise Exception("no header 1 (h1) to extract title from")
    else:
        return matches[0]