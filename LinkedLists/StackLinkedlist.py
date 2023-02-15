class stacknode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return True if self.root == None else False
    def push(self, data):
        newnode = stacknode(data)
        newnode.next = self.root
        self.root = newnode
        print(newnode.data + " pushed to stack")
    def pop(self):
        if(self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        return temp.data
    def peek(self):
        print("the top of the stack is: " + self.root.data)
        return self.root.data
