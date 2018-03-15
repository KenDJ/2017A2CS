#Task 27.04
import datetime
class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title,';',self.__Author__Artist,';',end='')
        print(self.__ItemID,',',self.__OnLoan,',', self.__DueDate)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return(self.__IsRequested)

    def SetIsRequested(self):
        self.__IsRequested = True

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested)

class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre = ""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self, g):
        self.__Genre = g

    def PrintDetails(self):
        print("CD Details")
        LibraryItem.PrintDetails(self)
        print(self.__Genre)

class Borrower:
    def __init__(self,a,b,c,d):
        self.__BorrowerName = a
        self.__EmailAddress = b
        self.__BorrowerID = c
        self.__ItemsOnLoan = 0

    def UpdateItems(self,a):
        self.__ItemsOnLoan = ++a

    def GetBorrowerName(self):
        return(self.__BorrowerName)

    def GetEmailAddress(self):
        return(self.__EmailAddress)

    def GetBorrowerID(self):
        return(self.__BorrowerID)

    def GetItemsOnLoan(self):
        return(self.__ItemsOnLoan)

    def PrintDetails(self):
        print(self.__BorrowerName,",",self.__EmailAddress,",",self.__BorrowerID,",",self.__ItemsOnLoan, end='')

    

def main():
    CarlBook = Book('Carl_Is_Dumb','Carl',2222)
    MJ = CD('Beat_It','MJ',1983) 
    CarlBook.PrintDetails()
    MJ.PrintDetails()
    Carl = Borrower('Carl','Carl@stupidity.com',2222,3)
    Carl.PrintDetails()

main()
