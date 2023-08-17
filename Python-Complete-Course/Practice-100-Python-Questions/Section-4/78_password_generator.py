#  create a program that generate a password of random 6 letters a-z A-Z and !@#$%^&*()?
import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

def password_generator():
    chosen = random.sample(characters,6)
    password = "".join(chosen)
    print(password)

password_generator()