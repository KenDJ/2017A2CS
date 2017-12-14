#Ken Su Opt 3
#CodingBat recursion 1

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    return bunnyEars(bunnies-1)+2

def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibonacci(x-2)+fibonacci(x-1)

def bunnyEars2(bunnies):
    if bunnies == 0:
        return 0
    if bunnies%2 ==0:
        return bunnyEars2(bunnies-1)+3
    if bunnies%2 ==1:
        return bunnyEars2(bunnies-1)+2

def triangle(x):
    if x == 0:
        return 0
    return triangle(x-1)+x

def sumDigits(x):
    if x ==0:
        return 0
    return sumDigits(int(x/10)) + x%10

def count7(x):
    if x == 0:
        return 0 
    if x%10 == 7:
        return count7(int(x/10)) + 1
    if x%10 != 7:
        return count7(int(x/10))

def count8(x):
    if x == 0:
        return 0
    if x%10 == 8:
        return count8(int(x/10)) + 1
    if x%10 != 8:
        return count8(int(x/10))

def powerN(base, n):
    if n == 1:
        return base
    return base*powerN(base, n-1)


def countX(word):                                                      
    if len(word) == 0:
        return 0
    if word[0] == 'x':
        return 1 + countX(word[1:])
    return countX(word[1:])


def countHi(word):
    if len(word) == 0:
        return 0
    if (word[0] == 'h') and (word[1] == 'i'):
        return 1 + countHi(word[1:])
    return countHi(word[1:])

def changeXY(x):
    if x == '':
        return ''
    if x[-1:] == 'x':
        return changeXY(x[:-1])+'y'
    else:
        return changeXY(x[:-1])+x[-1:]

def changePi(x):
    if x == '':
        return ''
    if x[-2:] == 'pi':
        return changePi(x[:-2])+'3.14'
    else:
        return changePi(x[:-1])+x[-1:]

def noX(string):
    if string == "":
        return ""
    if string[-1:] == 'x':
        return noX(string[:-1])
    else:
        return noX(string[:-1])+string[-1:]

def array6(x,index):
    if index == len(x):
        return False
    if x[index] == 6:
        return True
    return array6(x, index+1)

def array11(arr, index):
    if index == len(arr):
        return 0
    if arr[index] == 11:
        return 1 + array11(arr, index + 1)
    return array11(arr, index + 1)

print(array11([1,2,3,11,5,11], 0))

def array220(nums, index):
    if index == len(nums) - 1:
        return 0
    if nums[index + 1] == nums[index]*10:
        return 1 + array220(nums, index + 1)
    return array220(nums, index + 1)

print(array220([1,2,20], 0))

def allStar(string):
    if string[:-1] == '':
        return string[-1:]
    else:
        return allStar(string[:-1])+'*'+string[-1:]

def pairStar(string):
    if string == "":
        return ""
    if string[-1:] == string[-2:-1]:
        return pairStar(string[:-1])+'*'+string[-1:]
    else:
        return pairStar(string[:-1])+string[-1:]

def endX(string):
    if len(string) == '':
        return ''
    if string[0] == 'x':
        return endX(string[1:] + 'x')
    return endX(string)

def countPairs(x):
    if x == '':
        return 0
    if x[-1:] == x[-3:-2]:
        return countPairs(x[:-1])+1
    else:
        return countPairs(x[:-1])

def countAbc(string):
    if len(string) < 3:
        return 0
    if (string[0] == 'a') and (string[1] == 'b'):
        if string[2] == 'c':
            return 1 + countAbc(string[1:])
        if string[2] == 'a':
            return 1 + countAbc(string[1:])
    return countAbc(string[1:])
print(countAbc('abcxxaba'))


def count11(x):
    if len(x) == 0:
        return 0
    if x[0] == '1' and x[1] == '1':
        return count11(x[2:])+1
    else:
        return count11(x[1:])

def stringClean(x):
    if x == '':
        return ''
    if x[-1] == x[-2:-1]:
        return stringClean(x[:-1])
    else:
        return stringClean(x[:-1])+x[-1:]
print(stringClean("aaabcdd"))

def countHi2(string):
    if len(string) < 2:
        return 0
    if len(string) == 0:
        return 0
    if (string[0] != 'x') and (string[1] == 'h') and (string[2] == 'i'):
        return 1 + countHi2(string[1:])
    return  countHi2(string[1:])

print(countHi2("ahixhi"))

def parenBit(string):
    if string[0] != '(':
        if string[len(string) - 1] != ')':
            return parenBit(string[1:-1])
        return parenBit(string[1:])
    if string[len(string) - 1] != ')':
        return parenBit(string[:len(string)-1])
    return string

def nestParen(string):
    if len(string) == 0:
        return True
    if (string[0] == '(') and (string[len(string) - 1] == ')'):
        return nestParen(string[1:len(string)-1])
    return False

def strCount(string, sub):
    if len(string) < len(sub):
        return 0
    if string[:len(sub)] == sub:
        return strCount(string[len(sub):], sub) + 1
    return strCount(string[len(sub):], sub)

print(strCount("catcowcat", "cat"))

def strCopies(string, sub, n):
    if n <= 0:
        return True
    if len(string) < len(sub):
        return False
    if string[:len(sub)] == sub:
        return strCopies(string[1:], sub, n - 1)
    return strCopies(string[1:], sub, n)

print(strCopies('catcowcat', 'cat', 2))

def strDist(string, sub):
    if len(string) == 0:
        return 0
    if string[:len(sub)] != sub:
        return strDist(string[1:], sub)
    if string[-len(sub):] != sub:
        return strDist(string[:-1], sub)
    return len(string)
print(strDist("ccccatcowcatttttt", "cat"))
        

