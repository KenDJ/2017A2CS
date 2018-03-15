#Task 27.07
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

    def Returning(self, a,b):
        self.__OnLoan = False
        b.UpdateItemsOnLoan(-1)

    def GetTitle(self):
        return(self.__Title)

    def GetAuthor_Artist(self):
        return(self.__Author_Artist)

    def GetItemID(self):
        return(self.__ItemID)

    def GetOnLoan(self):
        return(self.__OnLoan)

    def GetBorrowerID(self):
        return(self.__BorrowerID)

    def GetDueDate(self):
        return(self.__DueDate)
        
    def PrintDetails(self):
        print(self.__Title,';',self.__Author__Artist,';',end='')
        print(self.__ItemID,',',self.__OnLoan,',', self.__DueDate, end= '')
        print(self.__BorrowerID)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return(self.__IsRequested)

    def GetRequestedBy(self):
        return(self.__RequestedBy)

    def RequestedBook(self,a,b):
        self.__IsRequested = True
        self.__RequestedBy = b.GetBorrowerID()

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        if self.__IsRequested:
            print('Requested By', self.__RequestedBy)
        else:
            print('It is still there')

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

def DisplayMenu():
    print('1 - Add a new borrower')
    print('2 - Add a new book')
    print('3 - Add a new CD')
    print('4 - Borrow book')
    print('5 - Return book')
    print('6 - Borrow CD')
    print('7 - Return CD')
    print('8 - Request book')
    print('9 - Print all details')
    print('99 - Exit program')
    print('                           ')
    print('Enter your menu choice')


def main():
    Terminate = False
    NextBorrowerID = 1
    NextBookID = 1
    NextCDID = 1

    while Terminate == False:
        DisplayMenu()
        MenuChoice = int(input())
        if MenuChoice == 1:
            BorrowerName = str(input("Name: "))
            Email = str(input("Email: "))
            BorrowerID = NextBorrowerID
            NextBorrowerID = NextBorrowerID + 1
            NewBorrower = Borrower(BorrowerName, Email, BorrowerID)
        elif MenuChoice == 2:
            Title = input("Title: ")
            Author = input("Author: ")
            ItemID = NextBookID
            NextBookID = NextBookID + 1
            NewBook = TBook(Title, Author, ItemID)
        elif MenuChoice == 3: 
            Title = input("Title: ")
            Artist = input("Artist: ")
            ItemID = NextCDID
            NextCDID = NextCDID + 1
            NewCD = CD(Title, Artist, ItemID)
        elif MenuChoice == 4: 
            BorrowerID = input("Borrower ID: ")
            ItemID = input("Book ID: ")
            Book.Borrowing(ItemID, Borrower)
        elif MenuChoice == 5: 
            BorrowerID = input("Borrower ID: ")
            ItemID = intput("Book ID: ")
            Book.Returning(ItemID, Borrower)
        elif MenuChoice == 6: 
            BorrowerID = input("Borrower ID: ")
            ItemID = input("CD ID: ")
            CD.Borrowing(ItemID, Borrower)
        elif MenuChoice == 7:
            BorrowerID = input("Borrower ID: ") 
            ItemID = input("CD ID: ")
            CD.Returning(ItemID, Borrower)
        elif MenuChoice == 8: 
            BorrowerID = input("Borrower ID: ")
            ItemID = input("Book ID: ")
            Book.RequestedBook(ItemID, Borrower)
        elif MenuChoice == 9: 
            print("Borrower Details")
            Borrower.PrintDetails()
            print("Book Details")
            Book.PrintDetails()
            print("CD Details")
            CD.PrintDetails()
        elif MenuChoice == 99: 
            Finish = True
        else:
            print("wrong input")
main()

