#!/usr/bin/env python3

# A Python password generator
# Generates a random password with given variables.
# User can enter their own variables (eg, amount of uppercase characters)

import random
import string
import sys
import os



SYMBOLS = ("?", "@", "*", "$", "!")
LOWERCASE = tuple(string.ascii_lowercase)
UPPERCASE = tuple(string.ascii_uppercase)
NUMBERS = tuple(string.digits)


def main():
    password = gen_pass([])
    while True:
        clear_console()
        print("Password:", password)
        print("\nWould you like to save this password? [Y/N]")
        choice = input('>> ')

        if choice.upper() == 'Y':
            save_pass(password)

        print('Press any key to continue')
        input()
        clear_console()
        main()


def gen_pass(pw):
    print('Would you like to enter your own password vales? (eg: amount of symbols) [Y/N]')
    print('Default is 5 lowercase letters and upper, 2 symbols and 3 numbers.')
    
    choice = input('>> ')
    if choice.upper() == 'Y':
        print('Enter how many of each characters you need: ')
        while True:
            try:
                num_of_lower = int(input('Lowercase Letters: '))
                num_of_upper = int(input('Uppercase Letters: '))
                num_of_symbols = int(input('Symbols: '))
                num_of_numbers = int(input('Numbers: '))
                break
            except ValueError:
                clear_console()
                continue
    else:
        num_of_lower = 5
        num_of_upper = 5
        num_of_symbols = 2
        num_of_numbers = 3

    for i in range(num_of_lower):  
        pw.append(random.choice(LOWERCASE))

    for i in range(num_of_upper):  
        pw.insert(random.randint(0, len(pw)), random.choice(UPPERCASE))

    for i in range(num_of_symbols):  
        pw.insert(random.randint(0, len(pw)), random.choice(SYMBOLS))

    for i in range(num_of_numbers): 
        pw.insert(random.randint(0, len(pw)), random.choice(NUMBERS))

    return str(''.join(pw))  


def save_pass(pw):
    with open("passwords.txt", "a+") as f:  
        print("What is this password for?")
        use = input('>> ')
        f.write(f'{use}: {pw}\n')
        print('Password saved!')


def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    main()
