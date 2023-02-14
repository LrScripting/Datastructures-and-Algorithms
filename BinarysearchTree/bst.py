"""Binary Search Tree Implementation in python:
BST is a node based binary tree data structure with the folowing properties:
- the left subtree of a node contains only nodes with keys smaller than the nodes key
- the right subtree of a node contains only nodes with keys greater than the nodes key
- the left and right nodes are also BST's"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class binarySTree:
    def __init__(self) -> None:
        self.root = None

    def Insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.addToList(data, self.root)
    
    def addToList(self, data, node):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self.addToList(data, node.left)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self.addToList(data, node.right)
    
    def find(self, data):
        if self.root:
            return self.findItem(data, self.root)
        else:
            return None
    
    def findItem(self, data, node):
        if data == node.data:
            return node
       
        elif data < node.data and node.left:
            self.findItem(data, node.left)
        
        elif data > node.data and node.right:
            self.findItem(data, node.right)
    
    def print(self, data):
        if self.root:
            self.orderedPrint(data, self.root)
    
    def orderedPrint(self, data, node):
        if node.left:
            self.orderedPrint(node.left)

        print(node.data)

        if node.right:
            self.orderedPrint(node.right)

