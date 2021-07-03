from functions import encode, decode
import program_art

'''
create a program that can encode and decode any 
message in another one with ceasar cipher method
'''

print(program_art.logo)

while True:
    message = list(input('Type the message: '))
    encrypt_key = int(input('Enter the key: '))
    process = input('Encode or decode: ').lower()
    new_message = []

    if process == 'encode':
        encode(message, encrypt_key, new_message)
        
        replay = input('Enter "Y" to continue: ').lower()
        if replay != 'y': break

    elif process == 'decode':
        decode(message, encrypt_key, new_message)

        replay = input('Enter "Y" to continue: ').lower()
        if replay != 'y': break

    else:
        print(f'\nTry again, something goes wrong.\n')
