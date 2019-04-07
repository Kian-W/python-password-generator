# A Python password generator

"""
Password must have -

- 15 Characters
- 5 Lowercase
- 5 Uppercase
- 2 Symbols
- 3 Numbers
"""


import random
import string
import sys
import os


# Text variables

SYMBOLS = ("?", "@", "£", "$", "!")
LOWERCASE = tuple(string.ascii_lowercase)
UPPERCASE = tuple(string.ascii_uppercase)
NUMBERS = tuple(string.digits)

NUM_OF_SYMBOLS = 2
NUM_OF_LOWER = 5
NUM_OF_UPPER = 5
NUM_OF_NUMBERS = 3

###############


# Main function
def main():
    password = gen_pass([])
    while True:
        os.system('cls' if os.name=='nt' else 'clear') # clear console

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
            password = gen_pass([])
        else:
            sys.exit()


# Function to generate password
def gen_pass(pw):
    print('Enter how many of each characters you need: ')

    while True:
        try:
            NUM_OF_LOWER = int(input('Lowercase Letters: '))
            NUM_OF_UPPER = int(input('Uppercase Letters: '))
            NUM_OF_SYMBOLS = int(input('Symbols: '))
            NUM_OF_NUMBERS = int(input('Numbers: '))
            break
        except ValueError:
            continue

    
    for i in range(NUM_OF_LOWER):  # lowercase letters
        pw.append(random.choice(LOWERCASE))
        pass_len = len(pw)

    for i in range(NUM_OF_UPPER):  # Uppercase letters
        pw.insert(random.randint(0, pass_len), random.choice(UPPERCASE))
        pass_len = len(pw)

    for i in range(NUM_OF_SYMBOLS):  # Symbols
        pw.insert(random.randint(0, pass_len), random.choice(SYMBOLS))
        pass_len = len(pw)

    for i in range(NUM_OF_NUMBERS): # Numbers
        pw.insert(random.randint(0, pass_len), random.choice(NUMBERS))
        pass_len = len(pw)

    return str(''.join(pw))  # Return string instead of list


# Function to save password
def save_pass(pw):
    with open("passwords.txt", "a+") as f:  
        print("What is this password for?")
        use = input('>> ')
        f.write(f'{use}: {pw}\n')


if __name__ == "__main__":
    main()
