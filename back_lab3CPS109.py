# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:37:22 2022

@author: IQ
"""

def question_8(w,x,y,z):
    pairs = 0
    arr = [w,x,y,z]
    
    for num in arr:
        if (num == arr):
            pairs +=1
        
    


def question_9(T):

    count = 0
    arr = []
    for num in T:   #seperating the unit(string) and the temperature(int)
        if (count == len(T)-1): # and storing it on a list
            break 
        arr.append(int(num))
        count +=1 

    value = 0
    count = 0
    while (count < len(arr)):#converting the elements on the list to a whole number
        value += 10**((len(arr)-1)-count) * arr[count]
        count +=1
        
    if ("C" in T):
        if (value <= 0):
            print("Solid")
        elif(value > 0 and value < 100):
            print("liquid")
        else:
            print("gas")            
    elif ("F" in T):
        if (value <= 32):
            print("ice")
        elif(value > 32 and value < 212):
            print("liquid")
        else:
            print("gas")
            
    else:
        print("Temperature type not given")
    
def question_10(grade):
    value = 0.3
    base = 0
    # this function doesnt work for some reason, it should return the variable "base" after processing it, but it 
    # returns the global variable "base" 
    # this would've made my code more efficient, but it is what it is
    def add_sub(grade, base): 
        if ("+" in grade):
            base += value
        elif("-" in grade):
            base -= value
        else:
              pass
                
    if ("A" in grade):
        base = 4
        if ("+" in grade):
            base += value
        elif("-" in grade):
            base -= value
        else:
             pass
        print(base)
        
    elif ("B" in grade):
        base = 3
        if ("+" in grade):
            base += value
        elif("-" in grade):
            base -= value
        else:
             pass
        print(base)
        
    elif ("C" in grade):
        base = 2
        if ("+" in grade):
            base += value
        elif("-" in grade):
            base -= value
        else:
             pass
        print(base)
        
    elif("D" in grade):
        base = 1
        if ("+" in grade):
            base += value
        elif("-" in grade):
            base -= value
        else:
             pass
        print(base)
        
    else:
        print(base)
        
if (__name__ == "__main__"):
    #question_9("132F")
    #question_10("F+")
    pass