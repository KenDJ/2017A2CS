#Hash algorithm
#Opt 3 Ken

hashTable = [0]*10
Max = 10


def key(newItem):
    key = newItem % 10
    return key
        
        
def insert(newItem):
    index = key(newItem)
    while hashTable[index] != None:
        index = index + 1
        if index > Max:
            index = 1
    hashTable[index] = newItem

def findRecord(searchNumber):
    index = key(searchNumber)
    while (hashTable[index] != searchNumber) and (hashTable[index] != None):
        index = index + 1
        if index > Max:
            index = 0
    if hashTable[index] != None:
        print(index)

insert(25)
insert(30)
insert(26)
insert(11)
findRecord(26)
        
    
    
    
        
