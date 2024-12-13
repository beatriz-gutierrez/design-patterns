from abc import ABC, abstractmethod


class Component(ABC):

    def __init__(self, name: str):
        self.name = name
        self.parent = None

    @staticmethod
    def _get_path(path: str):
        names = path.split("/")[1:]
        node = root
        for name in names:
            node = node.children[name]
        return node

    def move(self, new_path: str):
        new_folder = Component._get_path(new_path)

        del self.parent.children[self.name]
        new_folder.children[self.name] = self

        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]

    @abstractmethod
    def copy(self, new_path: str):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()


class File(Component): # Leaf object

    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path: str):
        # TODO
        print(f"Coping {self.name} file to {new_path} path")

    def __str__(self):
        return f"{self.name} file"

class Folder(Component): # Composite object

    def __init__(self, name: str):
        super().__init__(name)
        self.children: dict[str, "Component"] = {} # {name:Component}

    def add_child(self, child: "Component"):
        child.parent = self
        self.children[child.name] = child

    def copy(self, new_path: str):
        # TODO
        print(f"Coping {self.name} folder to {new_path} path")

    def __str__(self):
        result = f"{self.name} folder\n"
        for component in self.children.values():
            result += f" {component.__str__()}\n"
        return result

if __name__ == "__main__":

    root = Folder("root")

    folder1 = Folder('folder1')
    folder2 = Folder('folder2')
    root.add_child(folder1)
    root.add_child(folder2)

    folder11 = Folder('folder11')
    folder1.add_child(folder11)

    file111 = File('file111', 'contents')
    folder11.add_child(file111)

    file21 = File('file21', 'other contents')
    folder2.add_child(file21)

    print(root.children)
   


    folder2.move('/folder1/folder11')
    print(folder11.children)
    file21.move('/folder1')
    print(folder1.children)


    print(root)
