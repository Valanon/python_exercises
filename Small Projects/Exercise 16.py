'''
https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
'''
import string
import random

def generate_password():
    password = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(random.randint(15,25)):
        password += random.choice(characters)
    return password

print(generate_password())