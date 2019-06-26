class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None





llist = Linklist()
llist.head = Node(1)
llist.head.next = Node(2)
llist.head.next.next = Node(3)


