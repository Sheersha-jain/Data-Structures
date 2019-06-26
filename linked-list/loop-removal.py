class Node:
    def __init__(self, data):
        self.data = data
        self.next =None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertElement(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detectandRemoval(self):
        if self.head is None:
            return
        if self.head.next is None:
            return

        slow_pointer = self.head
        fast_pointer = self.head

        while(slow_pointer and fast_pointer and fast_pointer.next):
            if fast_pointer.next is None:
                break
            if slow_pointer == fast_pointer:
                break
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            slow_pointer = self.head
            while(slow_pointer!=fast_pointer):
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
            fast_pointer.next = None

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

llist = Linkedlist()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
llist.head.next.next.next.next.next =  llist.head.next.next
llist.detectandRemoval()
llist.printList()
