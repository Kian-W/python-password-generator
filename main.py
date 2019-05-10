#!/usr/bin/env python3

# A Python password generator
# Generates a random password with given variables.
# User can enter their own variables (eg, amount of uppercase characters)

import random
import string
import sys
import os


# Text variables

SYMBOLS = ("?", "@", "*", "$", "!")
LOWERCASE = tuple(string.ascii_lowercase)
UPPERCASE = tuple(string.ascii_uppercase)
NUMBERS = tuple(string.digits)


# Main function
def main():
    password = gen_pass([])
    while True:
        clear_console()

        # Ask user to save
        print("Password:", password)
        print("\nWould you like to save this password? [Y/N]")
        choice = input('>> ')

        if choice.upper() == 'Y':
            save_pass(password)

        # Ask user to gen new pass
        print("\nWould you generate a new password? [Y/N]")
        choice = input('>> ')
        if choice.upper() == 'Y':
            clear_console()
            password = gen_pass([])
        else:
            sys.exit()


# Function to generate password
def gen_pass(pw):
    # Ask user if they want to enter their own values
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


    # Build password

    for i in range(num_of_lower):  # lowercase letters
        pw.append(random.choice(LOWERCASE))

    for i in range(num_of_upper):  # Uppercase letters
        pw.insert(random.randint(0, len(pw)), random.choice(UPPERCASE))

    for i in range(num_of_symbols):  # Symbols
        pw.insert(random.randint(0, len(pw)), random.choice(SYMBOLS))

    for i in range(num_of_numbers): # Numbers
        pw.insert(random.randint(0, len(pw)), random.choice(NUMBERS))

    return str(''.join(pw))  # Return string instead of list


# Function to save password to a .txt file
def save_pass(pw):
    with open("passwords.txt", "a+") as f:  
        print("What is this password for?")
        use = input('>> ')
        f.write(f'{use}: {pw}\n')
        print('Password saved!')


# Function to clear the console 
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    main()
