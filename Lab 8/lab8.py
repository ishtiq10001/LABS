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
    else:
        countcalls +=1
        return x * power(x,n-1)













if __name__ == "__main__":
    print(add_rec(5,9))
    print(log2(23))
    print(reverse('sentence'))
    #print(power(3,9))
    print(f"2**10 = {power(2,10)}, recursion called: {countcalls} times")
    countcalls = 0
    print(f"5**10 = {power(5,10)}, recursion called: {countcalls} times")
    countcalls = 0
    print(f"5**0 = {power(5,0)}, recursion called: {countcalls} times")
    countcalls = 0
