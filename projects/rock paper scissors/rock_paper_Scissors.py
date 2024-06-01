import random
import time

time.sleep(2)


choice = [ "rock" , "paper" , "scissors"]

drawing = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

]

choice_end = '''_______________________________________________'''

p1 = ""
p2 = ""

disconected = random.choice([
"Network issues" , 
"Weak signal or interference" , 
"driver issues" , 
"software-related problems"
])

print("\n ---------- \nhello dear player welcome to my !ONLINE! rock paper scissors \n enjoy playing agains bots.. i mean tottally real people")

time.sleep(1)
print("\n \n searching fo a lobby.... ")

time.sleep(2)
print("!lobby found!")
print("\n")
time.sleep(2)

p2 = random.choice(choice)
p2_index = choice.index(p2)
p2_final = f" ----------\n player 2's choice \n ---------- \n {p2} \n {drawing[p2_index]}"


p1 = input("please choose(rock , paper , scissors):  ")
while p1 not in choice:
    print(choice_end)
    print("!!invalid!!! \n .try again.")
    print(choice_end)
    p1 = input("please choose(rock , paper , scissors):  ")

else:
    p1_index = choice.index(p1)
    p1_final = f" ----------\n player 1's choice \n ---------- \n {p1} \n {drawing[p1_index]}"

#figure out who the winner is

if p1 == p2:
    result = f"p1 and p2 had a draw in this game"


            #[ "rock" , "paper" , "scissors"]
            #[    0        1           2    ]

elif p1 == choice[0] and p2 == choice[2] or p1 == choice[1] and p2 == choice[0] or p1 == choice[2] and p2 == choice[1]:
    result = f"p1 won this game by playing a {p1} \n ||!!CONGRATS!!||"
else:
    result = f"p2 won this game by playing a {p2}"

time.sleep(1)
print("loading p1 results... ")
time.sleep(5)
print("[loaded] \n")

time.sleep(1)
print(p1_final)
print(choice_end)

time.sleep(1)
print("loading p2 results... ")
time.sleep(5)
print("[loaded] \n")

time.sleep(1)
print(p2_final)
print(choice_end)

time.sleep(1)
print("loading results... ")
time.sleep(5)
print("[loaded] \n")

time.sleep(1)
print("\n",result)
print(choice_end)
print("\n")
print(choice_end)
print(f"disconected why? ({disconected})")
print(choice_end)
print("\n")

    


