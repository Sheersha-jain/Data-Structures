current_pointer = -1
stack = []
stack_size = 0

def createStack(size):
    global stack_size
    stack_size = size
    for i in range(stack_size):
        stack.append(0)
    print(stack)


def isFull():
    if current_pointer == stack_size -1:
        return True
    return False

def isEmpty():
    if current_pointer == -1:
        return True

    return False

def push(new_element):
    if isFull():
        print("Stack is full")
        return

    global current_pointer
    stack[current_pointer+1] = new_element

    current_pointer = current_pointer+1
    print(stack)

def pop():
    if isEmpty():
        print("stack is empty")
        return

    global current_pointer
    stack[current_pointer]=0
    current_pointer = current_pointer -1
    print(stack)


createStack(5)
push(3)
push(4)
push(6)
push(-1)
push(7)
push(10)
pop()
pop()
pop()
pop()
pop()
pop()