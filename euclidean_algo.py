from math import *
from cmath import *

def gcd(int(a),int(b)):
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
print(gcd(input("first number: "), input("second number: ")))
