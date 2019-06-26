class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def push_on_node(self, new_data, prev_node):
        if prev_node is None:
            print("given previous node must present in linkedlist")
            return

        new_node = Node(new_data)
        print(type(new_node))
        print(type(prev_node))
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head= self.head.next

llist = Linklist()
llist.head = Node(2)
llist.head.next = Node(4)
llist.head.next.next = Node(66)
llist.push_on_node(llist.head.next, 8)
llist.printList()
