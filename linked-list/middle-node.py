class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertlist(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def middleNode(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            print(slow_ptr.data)

list1 = Linkedlist()
list1.insertlist(5)
list1.insertlist(4)
list1.insertlist(2)
list1.insertlist(3)
list1.insertlist(1)
list1.middleNode()