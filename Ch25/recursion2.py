#Codingbat Recursion 2
#Ken Su Opt 3

def groupSum(start,list1,target):
    if target == 0:
        return True
    if start == len(list1):
        return False
    return groupSum(start + 1, list1, target - list1[start]) or groupSum(start + 1, list1, target)



def groupSum6(start,list1,target):
    if start == len(list1):
        return (target == 0)
    if list1[start] == 6:
        return groupSum6(start+1,list1,target - list1[start])
    return groupSum6(start + 1, list1, target - list1[start]) or groupSum6(start + 1, list1, target)

print(groupSum6(0,[1,6,6,3],4))


def groupNoAdj(start,list1,target):
    if start == len(list1):
        return (target == 0)
    return groupNoAdji(start+2, list1, target - list1[start]) or groupNoAdji(start+1, list1,target)

def groupSum5(start, list1, target):
    if start == len(list1):
        return (target == 0)
    if list1[start] % 5 == 0:
        if list1[start+1] == 1:
            return groupSum5(start+2, list1, target - list1[start])
        if list1[start+1] != 1:
            return groupSum5(start +1, list1, target - list1[start])
    return groupSum5(start + 1, list1, target - list1[start]) or groupSum6(start + 1, list1, target)
 
def groupSumClump(start, list1, target):
    if start == len(list1):
        return (target == 0)
    for start in range(len[list1]-1):
        if list[start] == list[start + 1]:
            start = start + 1
    return groupSumClump(start + 1, list1, target - list1[start]) or groupSumClump(start + 1, list1, target)

def splitArrayhelper(list1, start, sum1, sum2):
    if (start >= len(list1)):
        return (sum1 == sum2)
    return splitArrayhelper(list1, start+1, sum1+list1[start], sum2) or splitArrayhelper(list1, start+1, sum1,sum2 + list1[start])

def splitArray(list1):
    return splitArrayhelper(list1, 0, 0, 0)

print(splitArray([1,2,3,4,4,5]))

def splitOdd10(list1, target=0, start=0):
    if target % 10 == 0 and (sum(list1)-target) % 2 == 1:
        return True
    if (start >= len(list1)):
        return False
    return splitOdd10(list1, target=target+array[start], start=start+1) or splitOdd10(list1, target=target, start=start + 1)

def split53(list1, target=0, start=0):
    if target == sum(list1)-target:
        return True
    if start >= len(list1):
        return False
    if list1[start] % 5 == 0:
        return split53(list1, target=target+array[start], start=start+1)
    if list1[start] % 3 == 0:
        return split53(list1, target=target, start=start+1)
    return split53(list1, target=target+array[start], start=start+1) or split53(list1, target=target, start=start+1)




