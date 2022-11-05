from math import *
from cmath import *
from time import *
from random import *

def question_1(s1,s2,s3,s4,s5):
    string_list = []

    for s in (s1,s2,s3,s4,s5): 
        string_list.append(s)
  
    for i in range(len(string_list)-1,-1,-1):
        print(string_list[i])
        
def maxL(L):

    fl_list = []

    for char in L:
        if type(char) == float:
            fl_list.append(char)

        else:
            pass
    if len(fl_list) == 0:
        return None
    else:
        return (max(fl_list))
    

def longest(L):
    largest_yet = L[0]
    
    counter = 1
    for char in L:
        
        if len(char)>len(largest_yet):
            largest_yet = char
                        
        else:
            pass
    return largest_yet



def question_4(L,T):

    for i in range(1,101):#100
        L.append(i)
    
    for i in range(1,102):#51
        if i%2==1:
            L.append(i)
    
    for i in range(0,50):#50
        L.append(i**2)
    
    
    for i in range(1,61):#60
        L.append(randrange(0,50))

    
    for i in range(0,50):#50
        L.append(0)

    T = tuple(L)
    
    return T

def question_5(L):
    L = [x for x in range(1,101)] + [x for x in range(1,102) if x%2==1] 
    
    L+= [x**2 for x in range(0,50)] + [randint(0,50) for x in range(60)]

    L+= [0 for x in range(0,50)] 

    print(L)

def perimeter(poly):
                #sqrt ((x2       -  x1) ^2        +     ( y2 -   y1) ^2)
    mag = sqrt((poly[1][0]-poly[0][0])**2 + (poly[1][1]-poly[0][1])**2)
    print(mag)

def permutation(L):
    P = []
    C = list(L)

    for x in range(0,len(C)):
        i = randrange(0,len(C))
        P.append(C[i])
        C.pop(i)
    
    return P
        
def listGen():#list generator that creates a random list
    L  = []
    for i in range(0,30):
        g = randrange(0,31)
        L.append(g)
    return L

if __name__ == "__main__" :
    question_1('the blue moon','the red guitar','go home','spill the beans','winter in Oklahoma')
    print(maxL([100, 'blue', 3.5, 'sugar on the rocks', 7.0]))
    print(maxL([7, 2, 9, 1]))
    print(longest(['the sky is blue', 'this is a long string', 'the white house', 'green']))
    question_4([],())
    question_5([])

    x1 = 5
    x2 = 6
    y1 = 4
    y2 = 7
    #sqrt ((x2       -  x1) ^2        +     ( y2 -   y1) ^2)
    # = 3.1622776601683795 
    perimeter([(x1,y1),(x2,y2)])

    L_1 = [19, 4, 3, 17]
    poly = [(0, 0), (20, 0), (20, 10), (0, 10)]
    #print(permutation(listGen()))
    print("1 -- "+ str(permutation(range(0,30))))
    print("2 -- "+ str(permutation(range(0,30))))
    print("3 -- "+ str(permutation(L_1)))
    print("4 -- "+ str(permutation(poly)))


    
