class HTMLNode:
    def __init__(self, tag:str|None = None, value:str|None = None, children:list[HTMLNode]|None = None, props:dict|None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML.")

    def props_to_html(self):
        if not self.props:
            return ""
        return " "+" ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict|None = None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None and (self.tag is not "img" and self.tag is not "a"):
            raise ValueError("All Leaf nodes must have a value.")
        elif self.tag is None:
            return self.value
        if self.props:
            props_str = self.props_to_html()
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list[HTMLNode], props:dict|None = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All Parent nodes must have a tag.")
        if not self.children:
            raise ValueError("All Parent nodes must have children.")
        return f"<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
