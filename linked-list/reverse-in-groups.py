class Node:
    def __init__(self, data):
        self.data = data
        self.next= None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertlist(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverseGroups(self, head, k):
        current = head
        next = None
        previous = None
        count = 0

        while(current is not None and count< k):
            next = current.next
            current.next = previous
            previous = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverseGroups(next, k)
        return previous

    def printlist(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next


llist = Linkedlist()
llist.insertlist(9)
llist.insertlist(8)
llist.insertlist(7)
llist.insertlist(6)
llist.insertlist(5)
llist.insertlist(4)
llist.insertlist(3)
llist.insertlist(2)
llist.insertlist(1)

llist.printlist()
llist.head = llist.reverseGroups(llist.head, 3)

llist.printlist()

