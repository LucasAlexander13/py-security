from char_list import *

'''
create a program that can encode and decode any 
message in another one with ceasar cipher method
'''

while True:
    message = list(input('Type the message: '))
    encrypt_key = int(input('Enter the key: '))
    process = input('Encode or decode: ').lower()
    new_message = []

    if process == 'encode':
        for char in range(len(message)):
            if message[char] == ' ':
                new_message.append(' ')

            elif message[char] in upper_letters:
                position = upper_letters.index(message[char]) + encrypt_key
                if position >= len(upper_letters):
                    position = position - len(upper_letters)
                    new_message.append(upper_letters[position])
                else:
                    new_message.append(upper_letters[position])

            elif message[char] in lower_letters:
                position = lower_letters.index(message[char]) + encrypt_key
                if position >= len(lower_letters):
                    position = position - len(lower_letters)
                    new_message.append(lower_letters[position])
                else:
                    new_message.append(lower_letters[position])

            elif message[char] in numbers:
                position = numbers.index(message[char]) + encrypt_key
                if position >= len(numbers):
                    position = position - len(numbers)
                    new_message.append(numbers[position])
                else:
                    new_message.append(numbers[position])

        new_message = ''.join(new_message)
        print(f'\nYour message is: {new_message}\n')

        replay = input('Enter "Y" to continue: ').lower()
        if replay != 'y': break

    elif process == 'decode':
        for char in range(len(message)):
            if message[char] == ' ':
                new_message.append(' ')

            elif message[char] in upper_letters:
                position = upper_letters.index(message[char]) - encrypt_key
                if position >= len(upper_letters):
                    position = position - len(upper_letters)
                    new_message.append(upper_letters[position])
                else:
                    new_message.append(upper_letters[position])

            elif message[char] in lower_letters:
                position = lower_letters.index(message[char]) - encrypt_key
                if position < 0:
                    position = position - len(lower_letters)
                    new_message.append(lower_letters[position])
                else:
                    new_message.append(lower_letters[position])

            elif message[char] in numbers:
                position = numbers.index(message[char]) - encrypt_key
                if position < 0:
                    position = len(numbers) + position
                    new_message.append(numbers[position])
                else:
                    new_message.append(numbers[position])

        new_message = ''.join(new_message)
        print(f'\nYour message is: {new_message}\n')

        replay = input('Enter "Y" to continue: ').lower()
        if replay != 'y': break

    else:
        print(f'\nTry again, something goes wrong.\n')
