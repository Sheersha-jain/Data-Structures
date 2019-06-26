class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            new_node.next = None

        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        new_node.next = None

    def prinList(self):
        while(self.head):
            print(self.head.data)
            self.head=self.head.next

llist = Linkedlist()
llist.head = Node(1)
llist.head.next = Node(23)
llist.head.next.next = Node(44)
llist.push_end(6)
llist.prinList()