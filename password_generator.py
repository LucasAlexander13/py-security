from random import choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all_char = ['letter', 'number', 'symbol']

num_letters = int(input('How much letters: '))
num_numbers = int(input('How much numbers: '))
num_symbols = int(input('How much symbols: '))

password_lenght = num_letters + num_numbers + num_symbols
password = ''

for characters in range(password_lenght):
    random_char = choice(all_char)

    if random_char == 'letter':
        if num_letters != 0:
            password += choice(letters)
            num_letters -= 1
            if num_letters == 0:
                all_char.remove('letter')

    elif random_char == 'number':
        if num_numbers != 0:
            password += choice(numbers)
            num_numbers -= 1
            if num_numbers == 0:
                all_char.remove('number')

    elif random_char == 'symbol':
        if num_symbols != 0:
            password += choice(symbols)
            num_symbols -= 1
            if num_symbols == 0:
                all_char.remove('symbol')

print(f'Your password is: {password}') 
