# A Python password generator

# 15 Characters
# 5 Lowercase
# 5 Uppercase
# 2 Symbols
# 3 Numbers

import string
import random as r

# Text variables
SYMBOLS = ("?", "@", "£", "$", "!")
LOWERCASE = tuple(string.ascii_lowercase)
UPPERCASE = tuple(string.ascii_uppercase)
NUMBERS = tuple(string.digits)

def main():
    password = []
    print(gen_pass(password))


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

    return str(''.join(pw))

if __name__ == "__main__":
    main()
