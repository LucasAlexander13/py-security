from char_list import *

##############################################################################

def encode(message, key, encoded):
    for char in range(len(message)):
        if message[char] == ' ':
            encoded.append(' ')

        elif message[char] in upper_letters:
            position = upper_letters.index(message[char]) + key
            if position >= len(upper_letters):
                position = position - len(upper_letters)
                encoded.append(upper_letters[position])
            else:
                encoded.append(upper_letters[position])

        elif message[char] in lower_letters:
            position = lower_letters.index(message[char]) + key
            if position >= len(lower_letters):
                position = position - len(lower_letters)
                encoded.append(lower_letters[position])
            else:
                encoded.append(lower_letters[position])

        elif message[char] in numbers:
            position = numbers.index(message[char]) + key
            if position >= len(numbers):
                position = position - len(numbers)
                encoded.append(numbers[position])
            else:
                encoded.append(numbers[position])
        else:
            encoded.append(message[char])

    encoded = ''.join(encoded)
    print(f'\nYour message is: {encoded}\n')

##############################################################################

def decode(message, key, decoded):
    for char in range(len(message)):
        if message[char] == ' ':
            decoded.append(' ')

        elif message[char] in upper_letters:
            position = upper_letters.index(message[char]) - key
            if position >= len(upper_letters):
                position = position - len(upper_letters)
                decoded.append(upper_letters[position])
            else:
                decoded.append(upper_letters[position])

        elif message[char] in lower_letters:
            position = lower_letters.index(message[char]) - key
            if position < 0:
                position = position - len(lower_letters)
                decoded.append(lower_letters[position])
            else:
                decoded.append(lower_letters[position])

        elif message[char] in numbers:
            position = numbers.index(message[char]) - key
            if position < 0:
                position = len(numbers) + position
                decoded.append(numbers[position])
            else:
                decoded.append(numbers[position])
        else:
            decoded.append(message[char])

    decoded = ''.join(decoded)
    print(f'\nYour message is: {decoded}\n')
