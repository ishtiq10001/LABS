from math import floor,ceil,pi
from random import randint,random,randrange


countcalls = 0

def add_rec(a,b):#q1
    if b == 1:
        return a+1

    else:

        return 1 + add_rec(a,b-1)

def log2(x):#q2
    if x <= 1:
        return 0
    else:
        return 1+log2(x/2)

def reverse(sentence):#q3
    if len(sentence) <= 1:
        return sentence
    else:
        return reverse(sentence[1:])+sentence[0]

def power(x,n):#q4
    global countcalls
    if n == 0:
        return 1
    elif n < 0:
        return None
    if x == 0:
        return 0
    else:
        countcalls +=1
        return x * power(x,n-1)


def powerHalf(x,n):
    global countcalls
    if n == 0:
        return 1
    elif n < 0:
        return None
    if x == 0:
        return 0

    elif n%2==0:
        countcalls +=1
        return ((powerHalf(x,n/2))**2)

    else:
        countcalls +=1
        return x * powerHalf(x,n-1)


def inputSeq():
    f = open('kdpF.txt') # opens a file for reading
    line = f.readline() # reads a single line
    #print(line)
    seq = ''
    for line in f : # reading the rest of the lines
        seq = seq + line
    seq = seq.replace('\n', '') # removing the newline characters
    seq = seq.upper()

    return seq


def gcContent(sequence):
    totalG = 0
    totalC = 0
    totalSeq = 0
    for x in sequence:
        if x.isupper() == True:
            totalSeq+=1

    for p in sequence:
        if p == 'G':
            totalG +=1
        elif p == 'C':
            totalC +=1
        else:
            pass

    percG = (totalG/totalSeq) * 100
    percC = (totalC/totalSeq) * 100

    print(f"percentage of G: {percG}")
    print(f"percentage of C: {percC}")





if __name__ == "__main__":
    print(add_rec(5,9)) #question 1
    print(log2(23)) #question2
    print(reverse('sentence'))#question 3
    print(power(3,9))#question 4
    #question 5
    print(f"2**10 = {power(2,10)}, recursion called: {countcalls} times")
    countcalls = 0
    print(f"5**10 = {power(5,10)}, recursion called: {countcalls} times")
    countcalls = 0
    print(f"5**0 = {power(5,0)}, recursion called: {countcalls} times\n")
    countcalls = 0

    #question 6
    print(f"\n2**10 = {powerHalf(2,10)}, recursion called: {countcalls} times")
    countcalls = 0
    print(f"5**10 = {powerHalf(5,10)}, recursion called: {countcalls} times")
    countcalls = 0
    print(f"5**0 = {powerHalf(5,0)}, recursion called: {countcalls} times")
    countcalls = 0

    gcContent(inputSeq()) #question 7
