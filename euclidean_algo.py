from math import *
from cmath import *

def gcd(a,b):
    if a == 0 and b == 0:
        return None
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a,b % a)

print("GCD Calculator")
print(gcd(int(input("first number: ")), int(input("second number: "))))
