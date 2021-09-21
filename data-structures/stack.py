def create_stack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item, "pushed into stack")

def pop(stack):
    if isEmpty(stack):
        print("Stack is empty")
        return None
    print(stack[-1], "is popped")
    stack.pop(-1)
    return None

def display(stack):
    if isEmpty(stack):
        print("Stack is empty")
        return None
    print(stack)

stack = create_stack()
if isEmpty(stack):
    print("Stack is empty")
else:
    print("stack is not empty")
push(stack, 1)
pop(stack)
push(stack,2)
push(stack,3)
display(stack)
pop(stack)
pop(stack)
pop(stack)
display(stack)

