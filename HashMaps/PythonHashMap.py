#asscosiative array abstract datatype
# everything is stored in key value pairs 
# you're mapping a name to a value, string to variable, ect
class HashTable:
    #create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hashTable = self.createBuckets()
        
    #creates an array of buckets, buckets are empty slots/arrays, the number of buckets is the length of the hashtable
    def createBuckets(self):
        return [[] for _ in range(self.size)]
        
    #inserting value into the hasmap
    def setVal(self, key, val):
    
        # get the index from the key
        # using hash     function
        
        hashKey = hash(key) % self.size
        # get the bucket corresponding the in dex 
        bucket = self.hashTable[hashKey]
        foundKey = False
        for i, r in enumerate(bucket):
            rKey, rVal = record
            # check if the bucket has the same key as the key to be to be inserted
            if rKey == key:
                foundKey = True
                break
        if foundKey:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
    #returned searched value with a specific key
        
    def getVal(self, key):
        hashKey = hash(key) % self.size
        bucket = self.hashTable[hashKey]
        
        foundKey = False
        for i, r in enumerate(bucket):
            rkey, rVal = r
            if rkey == key:
                foundKey = True
                break
            
        if foundKey:
            return rVal
        else: return "Table doesnt contain desired record"
    
    def deleteVal(self, key):
        hashKey = hash(key) % self.size
        bucket = self.hashTable[hashKey]
        foundKey = False
        for i, r in enumerate(bucket):
            rkey, rVal = r
            if rKey == key:
                self.hashTable.pop(i)
            else: return "no value to be deleted"
    def __str__(self):
        return "".join(str(item) for item in self.hashTable)

hashTable = HashTable(50)

#insert some values
hashTable.setVal("lmao@gmail.com", 'megakek')
print(hashTable)

hashTable.setVal("myemail@gmail.com", "password") 
print(hashTable)
print(hashTable.getVal("myemail@gmail.com")) 
