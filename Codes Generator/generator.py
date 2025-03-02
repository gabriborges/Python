import os
os.system('cls')
from itertools import product

#define the code you wnat to generate codes from it
initial_code = '4E71-4155-B95C'

#capslock list of characters, most common on several codes
LIST_ascii = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H',
'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#non capslock list of characters
list_asciis = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h',
'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#case sensitive list of characters(notice that there you be more possible combinations, this inflicts directly at the amount of generated codes whitch can reach extreme amounts)
List_Asciis = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h',
'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

codes = []

def generateCodes(position,number_of_combinations=1,letter_position=0):
    #the number of combinations of the characters is 1 by default, but you can change at the 2ª parameter of the function

                                            #replace the LIST_ascii for another one right here for other list if you need it
    pre_codes = [''.join(x) for x in product(LIST_ascii, repeat=number_of_combinations)]

    #if you want to position at the star of the code, put 'start' in the parameter
    if position=='start':
        for combination in pre_codes:
            code=combination+initial_code
            codes.append(code)
    
    #if you want to position at the end of the code, put 'end' in the parameter
    elif position=='end':
        for combination in pre_codes:
            code=initial_code+combination
            codes.append(code)

    #if you want to position at the middle of the code, put 'mid' in the parameter
    #and in the last parameter put the position(1,2,3,4,...) of the letter you want the pre_code to be add right after
    elif position=='mid':
        for combination in pre_codes:
            code=initial_code
            code= code[:letter_position] + combination + code[letter_position:]
            codes.append(code)
    else:
        print("Define de position.")

#Ex: (at the end of the initial code, combinations of 1 are being add)
generateCodes('end',1)

#Ex: (at the middle of the initial code, combinations of 2 are being add, after the 1ª character)
generateCodes('mid',2,1)

#finally the codes are being saved on a text file
codesfile = open("Codes Generator\codes.txt","r+")
codesfile.truncate(0)
for Code in codes:
    codesfile.write(Code + "\n")
codesfile.close()
