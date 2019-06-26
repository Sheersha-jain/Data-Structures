# maximum depth or height of tree

class Tree():
    def __init__(self, value):
        self.left = None
        self.right =None
        self.data = value

def max_depth(root):
    if not root:
        return 0
    else :
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        print("left-depth", left_depth)
        print("right depth", right_depth)

        if(left_depth > right_depth):
            return left_depth + 1
        else:
            return right_depth +1


root = Tree(233)
root.left = Tree(7676)
root.right = Tree(3873287)
root.right.right = Tree(546)

max_depth(root)