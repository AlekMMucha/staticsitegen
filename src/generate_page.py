from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from htmlnode import HTMLNode
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page \nfrom: {from_path} \nto: {dest_path} \nusing: {template_path}")
    with open(from_path,'r') as file:
        from_file_contents = file.read()
    with open(template_path,'r') as file:
        template_file_contents = file.read()
    title = extract_title(from_file_contents)
    from_html_nodes:HTMLNode = markdown_to_html_node(from_file_contents)
    from_html = from_html_nodes.to_html()
    template_file_contents = template_file_contents.replace("{{ Title }}", title)
    template_file_contents = template_file_contents.replace("{{ Content }}", from_html)
    os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    with open(dest_path,'w') as file:
        file.write(template_file_contents)

def generate_page_recursive(dir_path_content,template_path,dest_path):
    print(f"Generating pages (recursively) \nfrom: {dir_path_content} \nto : {dest_path}.")
    list_of_dir = os.listdir(dir_path_content)
    for item in list_of_dir:
        if item.endswith(".md"):
            generate_page(os.path.join(dir_path_content,item),template_path, os.path.join(dest_path,item.replace(".md",".html")))
        if os.path.isdir(os.path.join(dir_path_content,item)):
            os.mkdir(os.path.join(dest_path,item))
            generate_page_recursive(os.path.join(dir_path_content,item),template_path,os.path.join(dest_path,item))