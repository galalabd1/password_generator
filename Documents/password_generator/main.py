import random
import string


#characters used to generate our password
chars = string.ascii_letters + string.digits + "@#$%^&*"

def generate_password():
    password = []
    length = int(input("Enter the required length for password"))
    for i in range(length):
        password.append(random.choice(chars))

    random.shuffle(password)
    string_password = ''.join(password)
    print(string_password)

generate_password()

