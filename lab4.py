# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:29:40 2022

@author: Syed Hossain
"""


def question_1(): 
    sum = 0
    for i in range(2,101,2):
        sum += i
        print(sum)
    
def question_2():
    sum = 0
    for i in range(1,11):
        sum += i**2
        print(sum)

def question_3():
    for i in range(0,21):
        val = 2**i
        print(val)

def question_4(a,b):
    sum = 0
    for i in range(int(a),int(b)+1):
        if (i % 2  == 1):
            sum += i
    print(sum)

def question_5(n):
    sum = 0
    for i in n:
        p = int(i)
        if(p % 2 == 1):
            sum += p
            
    print(sum)
            

def question_6(): # works
    counter = 0
    arr = []
    while counter <= 10:
        user = int(input("number " + str(counter)+ ": "))
        arr.append(user) 
        counter +=1 
    counter = 0    
    arr.sort(reverse = True)
    for elem in arr:
        if (elem % 2 == 1):
            print("Largest odd number is " + str(elem))
            break
        
        elif (elem % 2 != 1 and counter == len(arr)-1):
            print("no odd number given")
        elif (elem % 2 != 1):
            counter +=1
        else:
            print("no odd number given")
            
      
def question_7(x):
    arr = []
    for char in x:
        if char:
            arr.append(char)
        else:
            pass
    print(arr)
if (__name__ == "__main__"):
    # question_1()
    # question_2()
    # question_3()
    # question_4(input("lower bound: "),input("upper bound: "))
    # question_5(str(13))
    # question_6()
    question_7("what are you doing1")
    