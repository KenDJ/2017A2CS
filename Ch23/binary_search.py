#insertionSort
#Ken Opt3
#Accordance to sudo code p327 electronic copy

def insertionSort(alist):
    for i in range(2,len(alist)):
        itemInserted = alist[i]
        currentItem = i - 1
        while (alist[currentItem] > itemInserted) and (currentItem > 0):
            alist[currentItem + 1] = alist[currentItem]
            currentItem = currentItem - 1
        alist[currentItem + 1] = itemInserted

alist = [1,2,3,5,6,7,3,4,5]
insertionSort(alist)
print(alist)
            
