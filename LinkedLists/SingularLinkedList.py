class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insertatStart(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode 
    
    def insertAfter(self, prev, data):
        if prev.data == None:
            print("Previous node you provided isnt in list")
            return
        newnode = node(data)
        newnode.next = prev.next 
        prev.next = newnode

    def insertaAtEnd(self, data):
  
        newnode = node(data)
        last = self.head
        
        #if linked list is empty set head as newnode
        if (last is None):
            self.head = newnode
        
        while(last.next):
            last = last.next
        last.next = newnode

