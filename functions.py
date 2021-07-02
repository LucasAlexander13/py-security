from char_list import *

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

    encoded = ''.join(encoded)
    print(f'\nYour message is: {encoded}\n')

