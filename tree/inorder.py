# Inorder traversal of tree
# sequence of inorder is (Left-Root-Right)

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(4)

inorder(root)


