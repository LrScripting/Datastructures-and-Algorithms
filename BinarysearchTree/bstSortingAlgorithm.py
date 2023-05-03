# Algorithm that sorts an array in acending or decending order!
# this algorithm converts the array into a sorted binary tree
# the binary tree is then recursively treversed to retrieve and return the sorted array.


# bst Node class
class BstNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

# bst base class
class Bst:
    def __init__(self):
        self.root = None
   
    
    def insert(self, data):
        if self.root:
            self.insertItem(data, self.root)
        else: 
            self.root = BstNode(data)
   
    def insertItem(self, data, node):
        if data >= node.data:
            if node.right is None:
                node.right = BstNode(data)
            else: 
                self.insertItem(data, node.right)
        if data < node.data:
            if node.left is None:
                node.left = BstNode(data)
            else:
                self.insertItem(data, node.left)
    def sortTree(self, node=None, sortedArray=[]):
        if node is None:
            node = self.root

        if node.left:
            self.sortTree(node.left)

        sortedArray.append(node.data)

        if node.right:
            self.sortTree(node.right)
        return sortedArray
    
    def revSortTree(self, node=None, sortedArray=[]):
        if node is None:
            node = self.root

        if node.right:
            self.revSortTree(node.right)
        sortedArray.append(node.data)

        if node.left:
            self.revSortTree(node.left)
        return sortedArray

    

    def convertArray(self, arr):
        newBst = Bst()
        for i in range(len(arr)):
            newBst.insert(arr[i])
        return newBst
    
binarySearchTree = Bst()


def bstSort(arr):
    bst = Bst()
    convertedArray = bst.convertArray(arr)
    return convertedArray.sortTree()

def bstReverseSort(arr):
    bst = Bst()
    convertedArray = bst.convertArray(arr)
    return convertedArray.revSortTree()    

arr = [2,1,4,8,2,8,3,1,7,4]
print(bstSort(arr))
print(bstReverseSort(arr))
