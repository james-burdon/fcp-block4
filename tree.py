class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        if isinstance(child, Tree):
            self.children.append(child)
    def print_tree(self, depth=0):
        print(" " * depth + self.value)
        for child in self.children:
            child.print_tree(depth + 1)


root = Tree('root')
child1 = Tree('child1')
root.add_child(child1)
child2 = Tree('child2')
root.add_child(child2)
grandchild1 = Tree('grandchild1')
child1.add_child(grandchild1)
greatgrandchild1 = Tree('greatgrandchild1')
grandchild1.add_child(greatgrandchild1)
root.print_tree()
