# postorder traversal of tree
# sequence of postorder traversal (Left-Right-Root)

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self. value = data

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
