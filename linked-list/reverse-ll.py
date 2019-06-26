class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertList(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        previous = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head =self.head.next

llist = Linkedlist()
llist.insertList(20)
llist.insertList(4)
llist.insertList(15)
llist.insertList(85)


llist.printList()
llist.reverse()
llist.printList()