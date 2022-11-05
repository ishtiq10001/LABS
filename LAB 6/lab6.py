from math import *
from cmath import *
from time import *


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



def question_4():
    
 

    
if __name__ == "__main__" :
    #question_1('y','2','3','4','c')
    #print(maxL([24,"2",2.4,5.6,7.8,"blue"]))
    #print(longest(['the sky is blue', 'this is a long string', 'the white house', 'green']))
