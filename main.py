# A Python password generator

# 15 Characters
# 5 Lowercase
# 5 Uppercase
# 2 Symbols
# 3 Numbers


import random as r
import string
import sys
import os


# Text variables
SYMBOLS = ("?", "@", "£", "$", "!")
LOWERCASE = tuple(string.ascii_lowercase)
UPPERCASE = tuple(string.ascii_uppercase)
NUMBERS = tuple(string.digits)



def main():   
    password = gen_pass([])
    while True:
        os.system('cls')

        # Ask user to save
        print("Password:", password)
        print("\nWould you like to save this password? [Y/N]")
        choice = input('>>')

        if choice == 'Y':
            save_pass(password)

        # Ask user to gen new pass
        print("\nWould you generate a new password? [Y/N]")
        choice = input('>>')
        if choice == 'Y':
            password = gen_pass([])
        else:
            sys.exit()


# Function to generate password
def gen_pass(pw):
    for i in range(5):  # lowercase letters
        pw.append(r.choice(LOWERCASE))
        pass_len = len(pw)

    for i in range(5):  # Uppercase letters
        pw.insert(r.randint(0, pass_len), r.choice(UPPERCASE))
        pass_len = len(pw)

    for i in range(2):  # Symbols
        pw.insert(r.randint(0, pass_len), r.choice(SYMBOLS))
        pass_len = len(pw)

    for i in range(3): # Numbers
        pw.insert(r.randint(0, pass_len), r.choice(NUMBERS))
        pass_len = len(pw)

    return str(''.join(pw))  # Return characters instead of list


# Function to save password
def save_pass(pw):
    with open("passwords.txt", "a+") as f:
        print("What is this password for?")
        use = input('>>')
        f.write(f'{use}: {pw}\n')


if __name__ == "__main__":
    main()
