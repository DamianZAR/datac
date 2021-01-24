# -*- coding: utf-8 -*-
"""
@author: Damian
"""
import numpy as np

#Useful function to ask the user for a numerical opction.
def num_opt(liminf,limsup):
    try:
        integer=int(float(input('>>')))
        while integer < liminf or integer > limsup:
        #while liminf > integer > limsup:
            print('Please type an integer number between',liminf,'and',limsup)
            integer=int(float(input('>>')))                       
    except:
        print('Please type a number')           
    return integer

#Dictionary to generate password and Encrypt/Decrypt a message.
alphabet={'q':'+', 'w':'x', 'e':'3', 'r':'|', 't':'/', 'y':'>','u':'{', 'i':'<', 'o':'(', 'p':']',
      'a':'@', 's':'#', 'd':'$', 'f':'%', 'g':'¬', 'h':'&', 'j':'*', 'k':'¿', 'l':'¡',
      'z':'-', 'x':'_', 'c':'!', 'v':'?', 'b':'8', 'n':']', 'm':')', ' ':' ', 'ñ':'ñ'}

print('Welcome to GEME, Encryptor, Decryptor and Secure Password Generator.')
print('Now I ask you what would you like to do?')
print('Please choose an option with an integer number.')
print('1. Generate a Secure Password. \n')
print('2. Encrypt or Decrypt a Message (according to our system).')
opc=input('>>')

try:
    aux=int(opc)
    if aux==1:
        print('You choose the first opction. We are going to generate you a password.')
        print('Please type how many characters needs your password, between 4 and 12.')
        
        size=num_opt(4,12)
        print('Your password will have',size,'characters.')
            
        print('Will the password have only numbers or alphanumeric characters?')
        print('If you choose Alphanumeric, you will get a password with even amount of digits.')
        print('You only will have to remove the last or the firs one of i.')
        print('Type 1 to Only Numbers')
        print('Type 2 to Alphanumeric')
        
        typ=num_opt(1,2)
        password=list()
        
        if typ==1:
            for i in range(size):
                x=np.random.randint(1,9)
                y=str(x)
                password.append(y)
            p=''.join(password)
            print('Take note, your password is:',p)
            
        else:
            print('We are going to create the password with some information of you,')
            print('which you will type without accent mark.')
            print('It doesn´t matter if answers are real or don´t')
            print('What is your birthdate? Please in this format: dd-month-aaaa')
            birthdate=input('>>')
            while '-' not in birthdate:
                print('Please, in this format: dd-mm-aaaa')
                birthdate=input('>>')
            print('What is your first name?')
            n=input('>>')
            name=n.lower()
            print('And what is your last name?')
            lastn=input('>>')
            lastname=lastn.lower()
            
            birth=list()
            for i in birthdate:
                if i != '-':
                    birth.append(i)
                else:
                    continue

            if size==4:
                for i in range(2):
                    password.append(name[i])
                for i in range(2):
                    password.append(lastname[i])
                
            elif size > 4 and size <= 6:
                for i in range(3):
                    password.append(name[i])
                for i in range(3):
                    password.append(lastname[i])
            elif size > 6 and size <= 8:
                for i in range(3):
                    password.append(birth[i])
                for i in range(3):
                    password.append(name[i])
                for i in range(2):
                        password.append(lastname[i])
                
            elif size > 8 and size <= 10:
                for i in range(3):
                    password.append(birth[i])
                for i in range(3):
                    password.append(name[i])
                for i in range(2):
                    password.append(birth[-(i+1)])
                for i in range(2):
                        password.append(lastname[i])
            
            else:
                for i in range(4):
                    password.append(birth[i])
                for i in range(3):
                    password.append(name[i])
                for i in range(2):
                    password.append(birth[i+6])
                for i in range(3):
                        password.append(lastname[i])

                
            for i in range(len(password)):
                for k in alphabet.keys():
                    if password[i]==k:
                        password[i]=alphabet[k]
            
            p=''.join(password)
            print('Take note, your password is',p)
            
    elif aux==2:
        print('What would you like to do, encrypt or decrypt a message (according to our system)?')
        print('1. Encrypt')
        print('2. Decrypt')
        
        crypt=num_opt(1,2)
        
        if crypt==1:
            print('Write the message you like to encrypt.')
            message=input('>>')
            messagetoen=message.lower()
            messageen=list()
            for i in messagetoen:
                for j in alphabet.keys():
                    if i==j:
                        x=alphabet[j]
                        messageen.append(x)
            m=''.join(messageen)
            print('Your encrypted message is "',m,'".')
        else:
            print('Write the encrypted message you have.')
            message=input('>>')
            messagetode=message.lower()
            messagede=list()
            for i in messagetode:
                for k, v in alphabet.items():
                    if i==v:
                        x=k
                        messagede.append(x)
            m=''.join(messagede)
            print('Your decrypted message is "',m,'".')
    else:
        print('Please type 1 or 2.')
except:
    print('Please type a number.')
print('\nProgram has finished')
