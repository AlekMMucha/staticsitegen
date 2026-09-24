from markdown_to_html_node import markdown_to_html_node
from main import extract_title
from htmlnode import HTMLNode
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page \nfrom: {from_path} \nto: {dest_path} \nusing: {template_path}")
    with open(from_path,'r') as file:
        from_file_contents = file.read()
    with open(template_path,'r') as file:
        template_file_contents = file.read()
    title = extract_title(from_file_contents)
    from_html_nodes = markdown_to_html_node(from_file_contents)
    from_html = from_html_nodes.to_html()
    template_file_contents.replace("{{ Title }}", title)
    template_file_contents.replace("{{ Content }}", from_html)
    if "public" in os.listdir("./"):
        os.makedirs(os.path.dirname(dest_path))
        with open(dest_path,'w') as file:
            file.write(template_file_contents)

            
    