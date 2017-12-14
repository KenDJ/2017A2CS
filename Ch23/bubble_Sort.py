#Bubble sort version 2
#Ken

def bubbleSort(alist):
    for i in range(len(alist),0,-1):
        for a in range(i):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            

alist = [1,3,4,5,2,23,342,3434,22,3,5,2]
bubbleSort(alist)
print(alist)
