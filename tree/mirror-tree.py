class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def mirror(node):
    if node is None:
        return 0
    else:
        temp = node
        mirror(node.left)
        mirror(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

def inorderNode(node):
    if node is None:
        return 0
    else :
        inorderNode(node.left)
        print(node.data, end=" ")
        inorderNode(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Inorder traversal")
inorderNode(root)


mirror(root)

print("\nInorder traversal of",
      "the mirror tree is ")
inorderNode(root)