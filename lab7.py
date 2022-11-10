from random import *
from time import *
from math import *


def bool_gen(n):
    bool_list = []
    for num in range(1,n+1):
        a = randint(0,1)
        if a == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)

    return bool_list


def longestFalse(L,B):
    t_list = []
    counter = 0
    start = 0
    end = 0
    print(L)
    while True:
        pass
##        try:
##            if counter != 0 and counter != len(L):
##                
##                if L[counter] == B and L[counter-1] != B:
##                    start = counter
##                    counter+=1
##                elif L[counter] == B and L[counter+1] != B:
##                    end = counter
##                    t_list.append((start,end))
##                    counter +=1
##                else:
##                    counter +=1
##            elif counter == len(L):
##                if L[counter] == B and L[counter-1] != B:
##                    pass
##                
##                elif L[counter] == B and L[counter-1] == B:
##                    end = counter
##                    t_list.append((start,end))
##                    counter +=1
##            elif counter == 0:
##                if L[counter] == B and L[counter+1] == B:
##                    start = counter
##                else:
##                    pass
##                
##            else:
##                pass
##        except:
##            print("error")
##            counter+=1
##        
##        if counter == len(L)+1:
##            break
        
          
            
    return(t_list) #print the highest difference tuple

def highest(T):
    high = []
    for i in T:
        high.append(i[1]-i[0])
    high.sort()
    return(high[len(high)])
    

def matrix(m):
    for i in range(len(m)):
        printRow(m[i])
        print("\n")

def printRow(row):
    for i in range(len(row)):
        print(row[i],end=" ")

def generate_nest(n):
    bird = []

    for i in range(n):
        bird.append("_")

    
    return(bird)

def bird_occupy(nests):
    start = 0
    end = 0
    t_list = []
    counter = 0

    





if __name__ == "__main__":
    mx = [[0,1,2],[7,8,9],[2,4,7],[0,2,6]]
    counter = 0
    while True:
        print(longestFalse(bool_gen(10),False))
        if counter == 30:
            break
        counter+=1
    #matrix(mx)
    bird_occupy(generate_nest)
    
    
