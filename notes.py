import random

#Even or odd

def evenOrOdd(num):
    if num % 2 == 0:
        return ('even')
    else:
        return('odd')

#Reverse a string

def reverse(thisString):
    reverseString = ""
    length = len(thisString) - 1
    for i in thisString:
        reverseString += thisString[length]
        length -= 1
    return(reverseString)

#Prime num checker

def prime(num):
    amountDiv = 0
    divisor = num
    wholeNum = 0
    for i in range(num):
        wholeNum = num / divisor
        if  wholeNum == round(wholeNum):
            amountDiv += 1
        divisor -= 1

    if amountDiv == 2:
        return("This number is a prime")
    else:
        return("This number is not a prime")

#Palidrome

def palidrome(thisString):
    if len(thisString) % 2 == 0:
        x = slice(len(thisString) // 2)
        y = slice((len(thisString) // 2), len(thisString))
        firstHalf = thisString[x]
        secondHalf = thisString[y]

        if reverse(firstHalf) == secondHalf:
            return("This string is a palidrome")
        else:
            return("This string is not a palidorme")
    else:
        x = slice(len(thisString) // 2)
        y = slice((len(thisString) // 2) + 1, len(thisString))
        firstHalf = thisString[x]
        secondHalf = thisString[y]

        if reverse(firstHalf) == secondHalf:
            return("This string is a palidrome")
        else:
            return("This string is not a palidorme")

#Pangram

def pangram(thisString):
    amountInAlphabet = 0
    stringUpper = thisString.upper()
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if i in stringUpper:
            amountInAlphabet += 1

    if amountInAlphabet == 26:
        return('This string is a pangram')
    else:
        return('This string is not a pangram')

#Minimum

def minimum(arg1, arg2, arg3, arg4, arg5):
    numList = [arg1, arg2, arg3, arg4, arg5]
    minNum = numList[0]
    for y in numList:
        if (y < minNum):
            minNum = y

    return(minNum)

#In range

def in_range(x, hi, lo):
    if lo < x < hi:
        return('in range')
    else:
        return('out of range')

#Greatest Common Denomiator

def gcd(x, y):
    divisor = 0
    if x > y:
        divisor = x
    else:
        divisor = y

    divX = x / divisor
    divY = y / divisor

    keepLoop = True

    while keepLoop == True:
        if (divX == round(divX)) and (divY == round(divY)):
            keepLoop = False
        else:
            divisor -= 1
            divX = y / divisor
            divY = x / divisor

    return (divisor)

#Dice rool mini-project

def diceRolls(numOfRolls):
    landsOf1s = 0
    landsOf2s = 0
    landsOf3s = 0
    landsOf4s = 0
    landsOf5s = 0
    landsOf6s = 0

    for roll in range(numOfRolls):
        randomNum = random.randint(1, 6)

        if randomNum == 1:
            landsOf1s += 1
        elif randomNum == 2:
            landsOf2s += 1
        elif randomNum == 3:
            landsOf3s += 1
        elif randomNum == 4:
            landsOf4s += 1
        elif randomNum == 5:
            landsOf5s += 1
        else:
            landsOf6s += 1

    numList = [landsOf1s, landsOf2s, landsOf3s, landsOf4s, landsOf5s, landsOf6s]

    print('1:', landsOf1s, '2:', landsOf2s, '3:', landsOf3s, '4:', landsOf4s, '5:', landsOf5s, '6:', landsOf6s)
    print('The percentage of 1s is:', landsOf1s / numOfRolls, 'The percentage of 2s is:', landsOf2s / numOfRolls, 'The percentage of 3s is:', landsOf3s / numOfRolls, 'The percentage of 4s is:', landsOf4s / numOfRolls, 'The percentage of 5s is:', landsOf5s / numOfRolls, 'The percentage of 6s is:', landsOf6s / numOfRolls)

    maxNum = 0

    for x in numList:
        if (x > maxNum):
            maxNum = x


    if maxNum == landsOf1s:
        print("The face that showed up the most was 1")
    if maxNum == landsOf2s:
        print("The face that showed up the most was 2")
    if maxNum == landsOf3s:
        print("The face that showed up the most was 3")
    if maxNum == landsOf4s:
        print("The face that showed up the most was 4")
    if maxNum == landsOf5s:
        print("The face that showed up the most was 5")
    if maxNum == landsOf6s:
        print("The face that showed up the most was 6")

diceRolls(10)
diceRolls(10000)
diceRolls(1000000)

#Print natural numbers
def printUpTo(x):
    for i in range(x):
        print(i)

#Prime number recursion

def prime(num):
    amountDiv = 0
    divisor = num
    wholeNum = 0
    for i in range(num):
        wholeNum = num / divisor
        if  wholeNum == round(wholeNum):
            amountDiv += 1
        divisor -= 1

    if amountDiv == 2:
        return("This number is a prime")
    else:
        return("This number is not a prime")

print(prime(7))

#Fibonacci

def fibonacci():
    firstNum = 0
    secondNum = 1
    nextNum = firstNum + secondNum
    for i in range(9):
        print(firstNum)
        firstNum = secondNum
        secondNum = nextNum
        nextNum = firstNum + secondNum

fibonacci()





