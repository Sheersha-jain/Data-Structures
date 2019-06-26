class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data= value

    def bfs(root):
        queue =[]
        if root is None:
            return
        queue.append(root)

        while len(queue)>0:
            print(queue[0])
            queue.pop(0)

            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)





