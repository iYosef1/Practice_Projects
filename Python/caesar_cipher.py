#CONTEMPORARY CAESAR-CIPHER ENCRYPTION & DECRYPTION


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


import math
from building_blocks_module import keyboard_preference, item_by_any_index


def keyboard_code(keyboard):
    code=''
    if 'a' in keyboard:
        code+='1'
    else:
        code+='0'
    if '0' in keyboard:
        code+='1'
    else:
        code+='0'
    if '~' in keyboard:
        code+='1'
    else:
        code+='0'
    return code
    



def cipher_message():
    print('\n\nENCRYPTION:\n\nThe keyboard of your encrypted message can consist of letters, numbers,\
    \nand/or symbols. You have the option of deciding your keyboard preference.\
    \nThe encryption of your message will be different depending on your preference.\n')

    #keyboard preference:
    modern_keyboard=None
    while modern_keyboard==None:
        modern_keyboard=keyboard_preference()
        if modern_keyboard==None:
            print('\nPlease try again.\n')
    if modern_keyboard!=None:
        print(f'\nYour 3-digit keyboard code is {keyboard_code(modern_keyboard)}.')
    
    #personal message for encryption:
    message=input('\nEnter your message to be encrypted: ').lower()
    split_message=message.split(' ')
    for item in split_message:
        for part in item:
            if part in modern_keyboard:
                pass
            else:
                print('\n\nSorry! Your keyboard preference does not suffice for the characters of your message. \
Your keyboard needs to be readjusted.\n')
                try_again=''
                while try_again!='Y' and try_again!='N':
                    try_again=input('Do you wish to readjust your keyboard preference(Y/N)?: ').upper()
                    if try_again=='Y':
                        cipher_message()
                        return
                    elif try_again=='N':
                        print('Goodbye!')
                        return

    #choose shift number:                  
    print('\nTip: A larger shift value will give you a more concealed encryption of your message.')
    shift=''
    while shift.isdigit() is False:
        shift=input('\nEnter number of shifts: ')
    print('\n\n')

    #encrypting the message:
    ciphered_list=[]
    for item in split_message:
        new_part=''
        for each_part in item:
            part_index=modern_keyboard.index(each_part)
            ciphered_index=part_index+int(shift)
            ciphered_part=item_by_any_index(modern_keyboard,ciphered_index) 
            new_part=new_part+ciphered_part
        ciphered_list.append(new_part)
    encrypted_message='  '.join(ciphered_list)
    print('ENCRYPTED MESSAGE:',encrypted_message)
    return




def decipher_message():
    print('\n\nDECRYPTION: ')
    
    #enter the keyboard code required for your keyboard:
    print('\nYou need a 3-digit keyboard code and the shift number to deciphor the encrypted message.')
    keyboard_code=''
    keyboard_codes=['111','100','010','001','110','011','101']
    while keyboard_code not in keyboard_codes:
        keyboard_code=input('\nEnter the 3-digit keyboard code: ')
    modern_keyboard=keyboard_preference(keyboard_code)

    #message for decoding:
    message=input('\nEnter your encrypted message for decryption: ').lower()
    split_message=message.split('  ')

    #enter your secret shift number:
    shift=''
    while shift.isdigit() is False:
        shift=input('\nEnter number of shifts: ')   
    print('\n\n')

    #decrypting the message:
    deciphered_list=[]
    for item in split_message:
        new_part=''
        for each_part in item:
            part_index=modern_keyboard.index(each_part)
            deciphered_index=part_index-int(shift)
            deciphered_part=item_by_any_index(modern_keyboard,deciphered_index)
            new_part=new_part+deciphered_part
        deciphered_list.append(new_part)
    decrypted_message='  '.join(deciphered_list)
    print('DECRYPTED MESSAGE:',decrypted_message)




if __name__ == '__main__':
    print(logo)
    cipher=True
    while cipher:
        caesar_cipher=''
        while caesar_cipher!='0' and caesar_cipher!='1':
            caesar_cipher=input('\nEnter 0 or 1 to encode (0) or decode (1): ')
            if caesar_cipher!='0' and caesar_cipher!='1':
                print('Please enter 0 or 1.')
        if caesar_cipher=='0':
            cipher_message()
        else:
            decipher_message()
        cipher=input('\nDo you wish to continue ciphering (Y/N)?: ').upper()
        if cipher=='Y':
            cipher=True
        else:
            cipher=False
            print('\n\nGoodbye.')







