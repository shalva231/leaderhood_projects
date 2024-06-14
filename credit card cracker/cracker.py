import random

card_number = "50692"

first_9_numbers = ""

numbers = ["0","1","2","3","4","5","6","7","8","9"]

for i in range(9):
    for j in random.choice(numbers):
        first_9_numbers += str(i)

print(first_9_numbers + card_number)