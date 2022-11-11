from math import *
from random import *
# global dictionary caesars cyhper
caesar = {'a':'x' , 'b':'y' ,'c':'z' ,'d':'a' ,'e':'b' ,'f':'c' ,'g':'d' ,'h':'e' ,'i':'f' ,'j':'g' ,'k':'h' ,'l':'i' ,'m':'j' ,'n':'k' ,'o':'l' ,'p':'m' ,'q':'n' ,'r':'o' ,'s':'p' ,'t':'q' ,'u':'r' ,'v':'s' ,'w':'t' ,'x':'u' ,'y':'v' ,'z':'w'}



def decypher(a,b):
   
    for x in a:
        for y in x:
            y = y.lower()
            for i,j in caesar.items():
                if y == j:
                    b +=i
        b+="\n"
            
    print(b)




if __name__ == "__main__":
    

    file_I = open('secret_code.txt', 'r')
    secret_code = file_I.readlines()
    file_I.close()
    
    
    decypher(secret_code, '')
