



class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            print("Error- value is also in Tree")

    def search(self, value):
        return False

    def pretty_print(self, indent=0):
        if self.right:
            self.right.pretty_print(indent + 4)
            print(" " * indent + str(self.value))
        if self.left:
            self.left.pretty_print(indent + 4)