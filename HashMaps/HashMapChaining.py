#hashmap with basic collision algorithm that uses a linked list for chaining in the even of collisions.

class CashList:
    # initialize linked list with head set to None
    def __init__(self,head=None):
        self.head = head
        
    # insert a new item into the linked list 
    def insertNode(self, node):
        if self.head == None:
            self.head = node
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node
    
    #print the linked list to debugging 
    def printList(self):
        temp =self.head
        while(temp.next != None):
            if temp.next != None:
                print(temp.data[1]+"\n")
                temp = temp.next
        else:
            print("no items in list")
    
#define thecashNode to be added to linked list
class CashNode:
    def __init__(self,data):
        self.data = data
        self.next =None

class CashMap:
    # initialize hashmap to size specified by user
    def __init__(self,size):
        self.size = size
        self.arrayMap = self.createMap(size)
        self.itemsInserted = 0
    
    # define Hash function to determine item index
    def hashFn(self,item):
        return sum([int(ord(y)) for y in list(item[0])]) % len(self.arrayMap)
    
    #create and initialize empty hash map   
    def createMap(self, size):
        return [[] for x in range(0, self.size)]
    


    #insert an item into the hash map, using chaining to prevent collisions
    def insertItem(self, item):
        targetIndx = self.hashFn(item)
        if self.arrayMap[targetIndx] == []:
            newNode = CashNode(item)
            newList = CashList()
            newList.insertNode(newNode)
            self.arrayMap[targetIndx] = newList
        else:
            itemList = self.arrayMap[targetIndx]
            newNode = CashNode(item)
            itemList.insertNode(newNode)
        self.itemsInserted += 1
        
    def deleteItem(self, item):
        indx = self.hashFn(item)
        currItem = self.arrayMap[indx].head
        prevItem = None
        while currItem:
            if currItem.data == item:
                if prevItem:
                    prevItem.next = currItem.next
                else:
                    self.arrayMap[indx].head = currItem.next
                return "Item Deleted Successfully! "
            prevItem = currItem
            currItem = currItem.next
            
    #prints all items in associated with the hash map
    def __str__(self):
        
        for i in range(self.size):
            temp = self.arrayMap[i].head
            
            while temp:
                print(temp.data)
                temp = temp.next
    
        print("\nBase layer: \n")
        for j in range(myCashMap.size):
            if myCashMap.arrayMap[j] == []:
                print([])
            else:

                print(myCashMap.arrayMap[j].head.data)
        
        return " "
            
    
                        


myCashMap = CashMap(3)
myCashMap.insertItem(("mega", "kek"))
myCashMap.insertItem(("Halla", "lulia"))
myCashMap.insertItem(("absa", "lutely"))
myCashMap.insertItem(("kke", "meg"))
myCashMap.insertItem(("apple", "dupa"))
myCashMap.insertItem(("cyka", "blyat"))
myCashMap.insertItem(("holye", "grail"))
myCashMap.insertItem(("trillionare", "cosmo"))
myCashMap.insertItem(("cyber", "terrorist"))
myCashMap.insertItem(("sinarcTan", "accupc"))
myCashMap.insertItem(("cosmoNoght", "cyberNought"))
myCashMap.insertItem(("iter", "ation"))
myCashMap.insertItem(("naught", "atro"))
myCashMap.insertItem(("triple", "dhs"))
myCashMap.insertItem(("idi", "nahoi"))
myCashMap.updateItemValue(('naught','atro'), 'cosmo')
myCashMap.deleteItem(('mega', 'kek'))

print(myCashMap)

print(myCashMap.arrayMap)

