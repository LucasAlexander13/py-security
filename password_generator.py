from random import choice
from char_list import *

num_uletters = int(input('How much uppercase letters: '))
num_lletters = int(input('How much lowercase letters: '))
num_numbers = int(input('How much numbers: '))
num_symbols = int(input('How much symbols: '))

password_lenght = num_uletters + num_lletters + num_numbers + num_symbols
password = ''

for characters in range(password_lenght):
    random_char = choice(all_char)

    if random_char == 'upper_letter':
        if num_uletters != 0:
            password += choice(upper_letters)
            num_uletters -= 1
        if num_uletters == 0:
            all_char.remove('upper_letter')
    
    elif random_char == 'lower_letter':
        if num_lletters != 0:
            password += choice(lower_letters)
            num_lletters -= 1
        if num_lletters == 0:
            all_char.remove('lower_letter')

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
