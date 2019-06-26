# preorder traversal of tree
# sequence of preorder traversal Root-Left-Right

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

root = Tree(39)
root.left = Tree(78)
root.right = Tree(100)

preorder(root)