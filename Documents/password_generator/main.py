from tkinter import *

import random
import string
import numpy as np

#characters used to generate our password
alphabet = string.ascii_letters
numbers = string.digits
s_chars = "@#$%^&*"

def generate_password():
    length = int(input("Enter a length of atleast 8"))

    ## generating a list so atleast one special character and number selected

    numbers_count = random.randint(1, length//2)
    schars_count = random.randint(1, length//2)
    alphabets_count = length - numbers_count - schars_count

    #generating password
    password = []
    for i in range(alphabets_count):
        password.append(random.choice(alphabet))

    for i in range(numbers_count):
        password.append(random.choice(numbers))

    for i in range(schars_count):
        password.append(random.choice(s_chars))


    random.shuffle(password)
    string_password = ''.join(password)
    print(string_password)

generate_password()
