# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 21:30:39 2022

@author: Syed I

"""


def question_1(num):
    if (num > 0):
        print("positive")
    elif (num < 0):
        print("negative") 
    else:
        print("zero")
    
        
def question_2(num):   
    if (num == 0):
        print("zero") 
    elif(num > 1 and num < 1000):
        print("positive")
    elif(num < -1 and num > -1000):
         print("negative")   
    elif(num > 0 and abs(num) < 1):
        print("positive and small")
    elif(num < 0 and abs(num) < 1):
        print("negative and small")
    elif(num > 1000 and abs(num) > 1000):
        print("positive and large")  
    elif(num < -1000 and abs(num) > 1000):
        print("negative and large")
    else:
        pass
   
     
def question_3(num):          
    if (num < 0):
        num = num * -1
    if (num < 10):
        print("1 digit")
    elif (num > 9 and num < 100):
        print("2 digits")
    elif (num > 99 and num < 1000):
        print("3 digits")
    elif (num > 999 and num < 10000):
        print("4 digits")
    elif (num > 9999 and num < 100000):
        print("5 digits")
    elif (num > 99999 and num < 1000000):
        print("6 digits")     
    else:
        print("lots of digits")
 
    
def question_4(x,y,z):
    if (x == y == z):
        print("all the same")
    elif (x != y != z):
        print("they're all different")   
    else:
        print("neither")
 
             
def question_5(a,b,c):
    if (a > b and b > c):
        print("decreasing")

    elif (a < b and b < c):
        print("increasing")

    else:
        print("neither")           
   
        
def question_6(a,b,c, user):
    if (user == "strict"):
        if (a > b and b > c):
            print("decreasing")

        elif (a < b and b < c):
            print("increasing")

        else:
            print("neither") 
        
    if (user == "linient"):      
        
         
        if (a == b == c):
            print("both increasing and decreasing")
        
        elif (a >= b and b >= c):
            print("decreasing")
            
        elif (a <= b and b <= c):
            print("increasing")
    
        else:
            print("neither")

def question_7(p,q,r):
    if (p >= q and q >= r):
        print("sorted")

    elif (p <= q and q <= r):
        print("sorted")

    else:
        print("not sorted")
    

def question_8(a,b,c,d):
    
    if (a == b == c == d):
        print("two pairs")
        
    elif((a != b or c or d) and (c == a or b or c)):
        print("not two pairs")
    elif((a == b or c or d) and (b == a or c or d)):
        print("two pairs")      
    elif((c == a or b or d) and (d == a or b or c)):
        print("two pairs")
    else:
        print("Not two pairs")
    
def question_9(T):
    for 
        

if (__name__ == "__main__"):
    #question_1(-100)
    #question_2(0.99)
    #question_3(-800065)
    #question_4(1,2,3)
    #question_5(4,3,2)
    #question_6(1,1,1,"linient")
    #question_7(-3,0,1)
    question_8(3,3,3,2)
