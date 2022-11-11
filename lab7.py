from cmath import *
from math import *
from random import *
from statistics import *

def dice_gen(n,t):#returns list of randomly generated values
    D_list = []
    
    for rand in range(1,n+1):
        if t == False:
            D_list.append(randint(1,6))
        else:
            if randint(0,1) == 0:
                D_list.append(False)
            else:
                D_list.append(True)
        
        
    return D_list

def question_1(dice):
    print(str(dice)+"- original list")
    new_list = []
    value = 0
    while value < 20:
        if value == 0:
            if (dice[value] == dice[value+1]):
                new_list.append("(" + str(dice[value]))
            else:
                new_list.append(dice[value])
        elif value>0 and value<len(dice)-1:
            if ((dice[value] == dice[value+1]) and (dice[value] != dice[value-1])):
                new_list.append("(" + str(dice[value]))

            elif ((dice[value] == dice[value-1]) and (dice[value] != dice[value+1])):
                new_list.append(str(dice[value])+")")

            else:
                new_list.append(dice[value])

        else:
            if (dice[value] == dice[value-1]):
                new_list.append(str(dice[value]) + ")")
            else:
                new_list.append(str(dice[value]))
            
        value +=1
    print(" ".join(str(x) for x in new_list)) #formatting
                
                
def sequenceFinder(L):
    start = 0
    end = 0
    counter = 0

    t_list = []
    print(L)
    while True:     
        if (counter != 0 and counter != len(L)-1):
            if L[counter] == L[counter+1] and L[counter] != L[counter-1]:
                start = counter
                counter +=1
            elif L[counter] == L[counter-1] and L[counter] != L[counter+1]:
                end = counter
                t_list.append((start,end))
                counter +=1

            else:
                counter +=1

        elif counter == 0:
            if L[counter] == L[counter+1]:
                start = counter
                counter +=1
            else:
                counter +=1
        elif counter == len(L)-1:
            if L[counter] == L[counter-1]:
                end = counter
                t_list.append((start,end))
                break
            else:
                break
                
        else:
            pass
    if len(t_list) == 0:
        pass
    else:
        return t_list[longest_seq(mag_elem(t_list))]
        

    

def mag_elem(t_list):
    l_list = []
    for i in range(len(t_list)):
        l_list.append(t_list[i][1] - t_list[i][0])
    return l_list

def longest_seq(t_1):
    val = 0
    for i in range(len(t_1)):      
        for j in range(i,len(t_1)):   
            if t_1[i]<t_1[j]:
                break
            elif t_1[i]>t_1[j]:
                val = t_1[i]
                if j < len(t_1)-1:
                    continue
                else:
                    return (i)
            elif t_1[i] == t_1[j]:
                val = t_1[i]
                if j < len(t_1)-1:
                    continue
                else:
                    return (i)
                
def question_2(orig_list, indx):
    x = orig_list[indx[0]]
    y = orig_list[indx[1]]

    orig_list[indx[0]] = "("+str(x)
    orig_list[indx[1]] = str(y)+")"
    
    return orig_list
    

def longestFalse(L, p=False): #question 3
    start = 0
    end = 0
    counter = 0

    t_list = []
    if p==False:
        print(L)
    else:
        pass
    while True:      
        if (counter > 0 and counter < len(L)-1):
            if L[counter] == p:
                if L[counter] == L[counter+1] and L[counter] != L[counter-1]:
                    start = counter
                    counter +=1
                elif L[counter] == L[counter-1] and L[counter] != L[counter+1]:
                    end = counter
                    t_list.append((start,end))
                    counter +=1

                else:
                    counter +=1
            else:
                counter +=1
        elif counter == 0:
            if L[counter] == p:
                if L[counter] == L[counter+1]:
                    start = counter
                    counter +=1
                else:
                    counter +=1

            else:
                counter +=1
        elif counter == len(L)-1:
            if L[counter] == p:
                if L[counter] == L[counter-1]:
                    end = counter
                    t_list.append((start,end))
                    break
                else:
                    break
            else:
                counter +=1
        else:
            break
    if len(t_list) == 0:
        pass
    else:
        return t_list[longest_seq(mag_elem(t_list))]
            



def occupy(emp):
    """
        1. get highest sequence tuple
        2. mean(highest sequence tuple)
        3. ceil that
        4. put X on the index of the ceil
        5. reiterate until all indexes have X

    """
    counter = 0
    counter2 = 0
    while True:  
        
        nest = longestFalse(emp,"_")
        
        if nest == None:
            if emp[counter2] == "_":
                nest = counter2
                emp[nest] = "X"   
                print(emp)
                counter2 +=1

            else:
                counter2+=1
        else:
            
            m = mean(nest)
            c = ceil(m)
            emp[c] = "X"
            print(emp)
        
        
        if emp == ['X','X','X','X','X','X','X','X','X','X']:
            break
        else:
            counter +=1
            



def question_5(P):
    original = P
    reverse = []
    counter = len(original)-1
    while counter >= 0:
        reverse.append(original[counter])
        counter -=1

    if original == reverse:
        print("this list is a palindrome")
    else:
        print("this list is not a palindrome")
    
        


if __name__ == "__main__":
    emp = ["_","_","_","_","_","_","_","_","_","_"]  
    #question1
    print("Q1")
    question_1(dice_gen(20,False))     
    #question 2
    print("Q2")
    randDice = dice_gen(20,False)
    sequence = sequenceFinder(randDice)
    print(" ".join(str(x) for x in question_2(randDice,sequence))) #formatting
    
    #question 3
    print("Q3")
    randFalse = dice_gen(10,True)
    print(longestFalse(randFalse, False))
    #question 4
    print("Q4")
    occupy(emp)
    #question 5
    print("Q5")
    t_List1 = [0,2,2,3,3,2,2,0]
    question_5(t_List1)
