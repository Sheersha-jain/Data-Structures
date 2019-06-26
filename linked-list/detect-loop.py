# Implementation of Floyd’s Cycle-Finding Algorithm
# to find loop in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def insertNode(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

    def detectLoop(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                print("detect found in the loop")
                return
        else:
            print("Loop free list")

llist = Linkedlist()
llist.insertNode(20)
llist.insertNode(4)
llist.insertNode(15)
llist.insertNode(10)

llist.head.next.next.next.next = llist.head
llist.detectLoop()