



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
        # Check to see if the current node has the value we are looking for.
        if self.value == value:
            return True

        # If value is less than current node's value, search the left sub-tree
        if value < self.value:
            # If there's a left child, we need to search it. If not, the value doesn't exist in the tree.
            if self.left:
                return self.left.search(value)
            return False
        else:
            # Same process as for the right child.
            if self.right:
                return self.right.search(value)
            return False

    def pretty_print(self, indent=0):
        if self.right:
            self.right.pretty_print(indent + 4)
            print(" " * indent + str(self.value))
        if self.left:
            self.left.pretty_print(indent + 4)

def test_search():
    #Values to store in the binary search tree
    values_to_add = [5, 8, 2, 4, 6, 7, 3]

    #Create a root node with the first element of the list
    root = BinarySearchTree(values_to_add[0])

    #Add remaining elements to the tree
    for val in values_to_add[1:]:
        root.insert(val)

    print("Running tests")
    assert(root.search(5)==True), "Test 1"
    assert(root.search(8)==True), "Test 2"
    assert(root.search(2)==True), "Test 3"
    assert(root.search(4)==True), "Test 4"
    assert(root.search(6)==True), "Test 5"
    assert(root.search(7)==True), "Test 6"
    assert(root.search(3)==True), "Test 7"
    assert(root.search(10)==False) , "Test 8"
    print("Tests finished")

if __name__ == "__main__":
    test_search()