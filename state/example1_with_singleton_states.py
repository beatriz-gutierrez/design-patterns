import os 

class Node:

    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        else:
            return self.tag_name

# Available states: OpenTag, CloseTag, TextNode and ChildNode
class OpenTag:

    def process(self, remaining_string, parser):

        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
       
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        node = Node(tag_name, parser.current_node)
        
        parser.current_node.children.append(node)
        parser.current_node = node
        print("Change to ChildNode state")
        parser.state = child_node

        return remaining_string[i_end_tag + 1 :]


class CloseTag:

    def process(self, remaining_string, parser):
       
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
       
        assert remaining_string[i_start_tag + 1] == "/"
        tag_name = remaining_string[i_start_tag + 2 : i_end_tag]
        assert tag_name == parser.current_node.tag_name
        
        parser.current_node = parser.current_node.parent
        print("Change to ChildNode state")
        parser.state = child_node
       
        return remaining_string[i_end_tag + 1 :].strip()


class TextNode:

    def process(self, remaining_string, parser):
       
        i_start_tag = remaining_string.find("<")
        text = remaining_string[:i_start_tag]
       
        parser.current_node.text = text
        print("Change to ChildNode state")
        parser.state = child_node
        
        return remaining_string[i_start_tag:]


class ChildNode:

    def process(self, remaining_string, parser):
       
        stripped = remaining_string.strip()
        if stripped.startswith("</"):
            print("Change to CloseTag state")
            parser.state = close_tag
        elif stripped.startswith("<"):
            print("Change to OpenTag state")
            parser.state = open_tag
        else:
            print("Change to TextNode state")
            parser.state = text_node
        
        return stripped


class FirstTag:

    def process(self, remaining_string, parser):

        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")

        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        root = Node(tag_name)

        parser.root = parser.current_node = root
        print("Change to ChildNode state")
        parser.state = child_node

        return remaining_string[i_end_tag + 1 :]

# module-level variables (mimicked singleton objects)
first_tag = FirstTag()
open_tag = OpenTag()
close_tag = CloseTag()
child_node = ChildNode()
text_node = TextNode()


class Parser:

    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None

        print("Start at FirstTag state")
        self.state = first_tag

    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    def start(self):
        self.process(self.parse_string)


if __name__ == "__main__":
    
    with open(os.path.join("state", "simplified.xml")) as file:
        
        contents = file.read()
        p = Parser(contents)
        p.start()

        nodes = [p.root]
        while nodes:
            node = nodes.pop(0)
            print(node)
            nodes = node.children + nodes
