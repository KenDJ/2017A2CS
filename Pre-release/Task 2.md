#Ken Su

#Task 2

##2.1 & arrows of 2.2

###

|Toy                  |
| ------------------- |
|Name      :  STRING  |
|ID        : STRING   |
|Price     : CURRENCY |
|Minimum age : INTEGER|
|---------------------|
|Constructor()        |
|GetName()            |
|GetID()              |  
|GetPrice()           |			    			
|GetMinimum_age()     |                     
|SetName()            |                     
|SetID()              |                     
|SetPrice()           |                     
|SetMinimum_age()     |                     
|PrintDetails()       |                     
                                            
                                            
|Computer Game        |                     
|---------------------|                     
|Category : STRING    |                     
|Console : STRING     |                    
|---------------------|            
|Constructor()        |                    
|GetCategory()        |                    
|SetCategory()        |                    
|SetConsole()         |                    
|GetConsole()         |                    
                                   	   
                                   
|Vehicle              |            
|---------------------|            
|Type         : STRING|            
|Height      : INTEGER|            
|Length     : INTEGER |            
|Weight     :  FLOAT  |            
|---------------------|            
|Constructor()        |    
|Set/GetType()        |
|Set/GetHeight()      |
|Set/GetLength()      |
|Set/GetWeight()      |

##2.2

###
If one class's attributes and functions are passed directly down to its subclasses,then the relationship between it and its subclasses is called inheritance.

In the example above, computer game and vehicle are both subclasses of toy, and they inherit all attributes and functions of toy.

##2.3

###

```python
class toy:
    def __init__(self, n, i, p, m):
        self.__name = n
        self.__id = i
        self.__price = p
        self.__minimum_age = m

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name = name

    def getID(self):
        return self.__id

    def setID(self, ID):
        self.__id = ID

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setminimumage(self, age):
        self.__minimum_age = age

    def getminimumage(self):
        return self.__minimum_age
```

##2.4

###
```python
class vehicle(toy):
    
	def __init__(self,n,i,p,m,t,h,l,w):
        				toy.__init__(self,n,i,p,m):
        				self.__type=t
       
		self.__height=h

	        self.__weight=w
 
	        self.__length=l

class ComputerGame(toy):
	def __init__(self,n,i,p,m,cat,con):
		toy.__init__(self,n,i,p,m):
		self.__category = cat
		self.__console = con
```
##2.5

###
```python
try:
    
	if age>0 and age<18:
        
		self.age=age
    
	else:
       
		age=input('Age out of range')
```

##2.6

###



    


