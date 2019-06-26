class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kdistance(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
    else:
        kdistance(root.left, k-1)
        kdistance(root.right, k-1)