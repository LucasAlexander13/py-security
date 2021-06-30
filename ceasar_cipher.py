'''
create a program that can encode and decode any 
message in another one with ceasar cipher method
'''

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    message = list(input('Type the message: ').lower())
    encrypt_key = int(input('Enter the key: '))
    process = input('Encode or decode: ').lower()
    new_message = []

    if process == 'encode':
        for char in range(len(message)):
            if message[char] == ' ':
                new_message.append(' ')
            elif message[char] in letter_list:
                position = letter_list.index(message[char]) + encrypt_key
                if position >= len(letter_list):
                    position = position - len(letter_list)
                    new_message.append(letter_list[position])
                else:
                    new_message.append(letter_list[position])

        new_message = ''.join(new_message)
        print(f'\nYour message is: {new_message}\n')

    elif process == 'decode':
        for char in range(len(message)):
            if message[char] == ' ':
                new_message.append(' ')
            elif message[char] in letter_list:
                position = letter_list.index(message[char]) - encrypt_key
                if position < 0:
                    position = len(letter_list) + position
                    new_message.append(letter_list[position])
                else:
                    new_message.append(letter_list[position])
        new_message = ''.join(new_message)
        print(f'\nYour message is: {new_message}\n')

    else:
        print(f'\nTry again, something goes wrong.\n')
