from math import *
from random import *
# global dictionary caesars cyhper so that it is accessable by all functions
caesar = {'a':'x' , 'b':'y' ,'c':'z' ,'d':'a' ,'e':'b' ,'f':'c' ,'g':'d' ,'h':'e' ,'i':'f' ,'j':'g' ,'k':'h' ,'l':'i' ,'m':'j' ,'n':'k' ,'o':'l' ,'p':'m' ,'q':'n' ,'r':'o' ,'s':'p' ,'t':'q' ,'u':'r' ,'v':'s' ,'w':'t' ,'x':'u' ,'y':'v' ,'z':'w'}



def decypher(a,b):
    for x in a: #a is a list, we need to read the strings
        for y in x: # so we need 2 for loops go read the letters
            for i,j in caesar.items():#we need a third loop to go through the caesar dictionary
                if y.isupper(): #if the letter is upper case                  
                    if y.lower() == j:# temporarily lowering it to match it with our cipher dictionary, also preserving the original case of the letter
                        b += i.upper()#adding the key of the caesar dictionary with its original case
                else:# if it is lower case
                    if y == j:#if our letter matches the value of the caesar dictionary
                        b+=i # we add the key
        b+="\n"# adding new lines to our code string so we can read it properly
          
    L = b.split('\n') #splitting the code into lines and using them as a list to itereate through them
    secret_message = [] #our secret message will be stored in this list
    counter = 0 # to check if its the first letter of the line
    
    for i in L: #again, L is a list with lines, we needto read the letters
        for j in i: # so we need 2 loops to read the letters
            if (counter != 0 and j.isupper() == True): #if its not the first letter of the line and if the letter is upper case
                secret_message.append(j)#then its a code so we store it in our secret message list
                
            else:#otherwise do nothing, this line is not necessary but it makes the code more organized
                pass
            counter +=1 #to count where we are in the line
        counter =0 # resetting it when we get to a new line
    secret_message_string = ''.join(secret_message)#converting the list to a string
    return secret_message_string # returning our secret code message as a string




if __name__ == "__main__":
    file_I = open('secret_code.txt', 'r') #opening secret code file
    secret_code = file_I.readlines() #reading the text from the file line by line
    file_I.close() #closing the file
    code = decypher(secret_code, '')# calling the code decipher function
    code = "https://tinyurl.com/"+code #combining the code with the url
    with open('code_cracked.txt','w') as file_O:#opening a new text file as write mode
        file_O.write(code)#adding/writing the secret code to this file 
        file_O.close()# closing the file
    
