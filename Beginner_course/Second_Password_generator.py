from random import *
from string import * 
letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def find_sym(string):
    sym = choice(letter)
    while sym not in string:
        sym = choice(letter)
    else:
        return sym

def generate_password(length): 
    password = []
    password.append(find_sym(ascii_uppercase))
    password.append(find_sym(ascii_lowercase))
    password.append(find_sym(digits))
    another = []
    for i in range(length - 3):
        another.append(choice(letter))
    password += another
    shuffle(password)
    return ''.join(password)

def generate_passwords(count, length):
    passwords = [generate_password(length) for i in range(count)]
    print(*passwords, sep="\n")

generate_passwords(int(input()), int(input()))