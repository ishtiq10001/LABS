from math import floor,ceil,pi
from random import randint,random,randrange


def add_rec(a,b):
    if b == 1:
        return a+1

    else:

        return 1 + add_rec(a,b-1)

def log2(x):
    if x <= 1:
        return 0
    else:
        return 1+log2(x/2)

def reverse(sentence):
    pass





















if __name__ == "__main__":
    print(add_rec(5,9))
    print(log2(23))
    print()
