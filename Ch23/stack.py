#Stack
#Ken Su Opt 3
#Push(): insert item at the top of the stack / Pop(): returns the item of the top
#The whole point of ordered list is to rank dataitems in arthimatic order!!!
#Very IMPORTANT !!!: always use 'self.attribute' format when using an attribute  
nullPointer = -1

class Node:
    def __init__(self):
        self.Data = ""
        self.nextPointer = nullPointer

class linkedList:
    def __init__(self):
        self.startPointer = nullPointer      #shoud there be nullpointer?
        self.freePointer = 0
        self.record = []
        newNode = None
        
        for i in range(10):
            newNode = Node()
            newNode.nextPointer = i + 1
            self.record.append(newNode)
        newNode.nextPointer = nullPointer        #what the hell

    def outputNode(self):
        currentPointer = self.startPointer
        while currentPointer != nullPointer:
            print(self.record[currentPointer].Data, end = ",")
            currentPointer = self.record[currentPointer].nextPointer

    def printList(self):
        for i in range(10):
            print(self.record[i].Data,':', self.record[i].nextPointer)

    def insertNode(self,newItem):
        if self.freePointer != nullPointer:
            newPointer = self.freePointer
            self.record[newPointer].Data = newItem
            self.freePointer = self.record[self.freePointer].nextPointer
            previousPointer = nullPointer                        #correction
            currentPointer = self.startPointer
            while (currentPointer != nullPointer) and (self.record[currentPointer].Data < newItem):    #second part ???
                previousPointer = currentPointer
                currentPointer = self.record[currentPointer].nextPointer
            if previousPointer == nullPointer:                  #correction
                self.record[newPointer].nextPointer = self.startPointer
                self.startPointer = newPointer
            else:
                self.record[newPointer].nextPointer = self.record[previousPointer].nextPointer
                self.record[previousPointer].nextPointer = newPointer

        def deleteNode(self, dataItem):
            currentPointer = self.startPointer
            while (currentPointer != nullPointer) and (self.record[currentPoitner].Data != dataItem):
                previousPointer = currentPointer
                currentPointer = self.record[currentPointer].nextPointer
            if (currentPointer != nullPointer):
                if currentPointer !=self.startPointer:
                    self.startPointer = self.record[startPointer].nextPointer
                else:
                    self.record[previousPointer].nextPointer = self.record[currentPointer].nextPointer       #
                self.record[currentPointer].nextPointer = self.freePointer
                self.freePointer = currentPointer

        def findNode(self, dataItem):
            currentPointer = self.startPointer
            while (currentPointer != nullPointer) and (self.record[currentPointer].Data != dataItem):
                currentPointer = self.record[currentPointer].nextPointer
            return currentPointer

        def push(self):
            self.record.append(newNode)
            newNode.nextPointer = nullPointer
            

        def pop(self):
            for i in range (10):
                if self.record[i].nextPointer == nullPointer:
                    return self.record[i].Data
                    deleteNode(self.record[i].Data)
            
                    
l = linkedList()
l.insertNode(5)
l.insertNode(25)
l.insertNode(15)
l.insertNode(35)
l.printList()                         
            
