import random
import time

special_char = ["?","!","@","#","$","%","^","&","*","/",",",".","<",">"]
nums = [1,2,3,4,5,6,7,8,9,0]
letters = ['a', 'b', 'c', 'd', 'e',
           'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z']
password = []
time_range = [4,6,3,7,5]
decor = '''___________________________'''
decor2 = "------------"

#write a func to figure out how many characters the user wants in his/her password (there are only two genders)
def get_range ():
    global spec_range , nums_range , letters_range
    spec_range = (input("\nhow many special characters do you want to be in your password: "))
    nums_range = (input("\nhow many numbers do you want to be in your password: "))
    letters_range = (input("\nhow many letters do you want to be in your password: "))

def make_range_int():
    global spec_range , nums_range , letters_range
    spec_range = int(spec_range)
    nums_range = int(nums_range)
    letters_range = int(letters_range)

time.sleep(1)
print("\n")
print(decor)
time.sleep(1)
print("hello welcome to my first ever built password generator")
time.sleep(1)
print("i hope this generator will be of help to you")
time.sleep(1)
print(decor)
print("\n")

#figure out how many of the character user wants in his/her (there are only two genders) password
get_range()

while not nums_range.isnumeric() or not letters_range.isnumeric() or not spec_range.isnumeric():
    print("\n")
    print(decor)
    print(decor2)
    time.sleep(1)
    print("please enter a numerical value")
    time.sleep(1)
    print(decor2)
    print(decor)
    print("\n")
    get_range()
    print(decor)

#if the input is numerical use the make_range_numerical func to turn the strings to integers
make_range_int()


time.sleep(1)
print("\n")
print(decor)
time.sleep(1)
print("calculating how long your password will be...")
time.sleep(random.choice(time_range))
print(decor2)
print("[calculated]")
print(decor2)

time.sleep(1)
print(decor)
print("\n")
print(f"your password will be {spec_range+nums_range+letters_range} characters long")
time.sleep(1)
print("\n")
print(decor)
print("\n")

#print how long the password will be 


for i in range(spec_range):
    password.append(random.choice(special_char))
for i in range(nums_range):
    password.append(str(random.choice(nums)))
for i in range(letters_range):
    password.append(random.choice(letters))

random.shuffle(password)
password = "".join(password)

time.sleep(1)
print("generating your password...")
time.sleep(random.choice(time_range))
print(decor2)
print("[generated]")
print(decor2)

time.sleep(1)
print(decor)

time.sleep(1)
print("\n shhhh this will be your password dont forget it ;)")
print("\n")

time.sleep(1)
print(decor)
print(decor2)
print(password)
print(decor2)
print(decor)

time.sleep(1)
print("\n")
print(decor)




