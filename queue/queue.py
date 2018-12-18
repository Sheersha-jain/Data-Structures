queue = []
front_pointer = 0
tail_pointer = -1
size = 0
capacity = 0

def createQueue(queue_capacity):
    global capacity
    capacity = queue_capacity
    for i in range(capacity):
        queue.append(0)
    print(queue)

def isEmpty():
    if size == 0:
        return True
    return False

def isFull():
    if size == capacity:
        return True
    return False

def push(new_element):
    if isFull():
        print("queue is full cannot insert element")
        return

    global tail_pointer
    global size
    global capacity

    queue[(tail_pointer+1)%capacity] = new_element
    tail_pointer = (tail_pointer +1)%capacity
    size =size +1
    print(queue)

def pop():
    if isEmpty():
        print("queue is empty cannot pop")
        return
    global front_pointer
    global size

    queue[front_pointer] =0
    front_pointer = (front_pointer +1)%capacity
    size =size-1
    print(queue)

createQueue(3)
push(5)
push(4)
push(2)
push(1)
pop()
pop()
push(6)
pop()
pop()
pop()