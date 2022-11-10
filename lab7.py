from cmath import *
from math import *
from random import *


def dice_gen(n):#returns list of randomly generated dice values
    D_list = []
    
    for rand in range(1,n+1):
        D_list.append(randint(1,6))
       
        
    
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
    print(" ".join(str(x) for x in new_list))
                
                
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
    
         

def question_5(P):
    original = P
    reverse = []
    counter = len(original)-1
    while counter >= 0:
        reverse.append(original[counter])
        counter -=1

    if original == reverse:
        return True
    else:
        return False
    
        


if __name__ == "__main__":
    #t_List1 = [2,1,2,3,4,4,3,2,1,2]
    #print(question_1(dice_gen(20)))
    #print(question_5(t_List1))
    #print(f(dice_gen(20)))
    #print(longest_seq([4,5,5,5,2,1,3,4,2,1]))
    randlist = dice_gen(20)
    sequence = sequenceFinder(randlist)
    print(question_2(randlist,sequence))
