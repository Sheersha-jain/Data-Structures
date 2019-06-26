# inserting node in link list in the front of list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = Linklist()
llist.head = Node(1)
llist.push_front(2)
llist.push_front(4)
llist.printList()


