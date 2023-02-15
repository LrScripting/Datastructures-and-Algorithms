def createstack():
    stack = []
    return stack
def isEmpty(stack):
    return (len(stack) < 1)

def popstack(stack):
    if isEmpty(stack):
        return "Stack Empty"
    print(str(stack.pop()) + " popped from stack")
    return stack.pop()

def peek(stack):
    print(str(stack[len(stack) -1 ]) + " Is at the top of the stack")
    return stack[len(stack) -1]

def push(stack, item):
    stack.append(item)
    print(str(item) + " Added to stack")

def reverseStack(stacklen):
    if stacklen <= 0:
        return 
    print("kek")
    revstack.append(stack[stacklen -1])
    reverseStack(stacklen - 1)

stack = createstack()
push(stack, 11)
push(stack, 23)
push(stack, 33)
peek(stack)
print(stack)
leny = len(stack) - 1
revstack = []
reverseStack(len(stack))
print(revstack)
peek(revstack)
push(revstack, 12)
peek(revstack)
