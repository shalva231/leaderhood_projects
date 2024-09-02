import pyautogui
import os
import time
import random
#shrek
shrek = os.path.join(r"C:/Users/er555/Desktop/leaderhood_projects/projects/july/pyautogui/shrekey", "shrek.png")
text = os.path.join(r"C:/Users/er555/Desktop/leaderhood_projects/projects/july/pyautogui/shrekey", "text.png")
#monkey
monkey = os.path.join(r"C:/Users/er555/Desktop/leaderhood_projects/projects/july/pyautogui/shrekey", "monkey.png")
text2 = os.path.join(r"C:/Users/er555/Desktop/leaderhood_projects/projects/july/pyautogui/shrekey", "text2.png")

print("\n ------- \n")
choice = input("please choose shrek or monkey: ")
print("\n ------- \n")


while choice.lower() != "shrek" and choice.lower() != "monkey":
    print(f"\n==========================\n Invalid choice. \n ----------------- \n ")
    choice = input("please choose shrek or monkey: ")

count = 0

if choice.lower() == "shrek":
    Tim = random.randint(1,3)

    location = pyautogui.locateOnScreen(shrek)
    if location:
        center_x, center_y = pyautogui.center(location)
        print(f"Image found at: {location}, center: ({center_x}, {center_y})")
        pyautogui.doubleClick(center_x, center_y,)
        time.sleep(2)
    else:
        print("Shrek image not found on the screen.")

    while True:
        Tim= random.randint(1,3)
        time.sleep(Tim)
            
        location1 = pyautogui.locateOnScreen(text)
        if location1:
            corner_x, corner_y = pyautogui.center(location1)
            print(f"repetition {count} \n --- \n Image found at: {location1}, center: ({corner_x}, {corner_y}) \n ================ \n")
            count += 1
            pyautogui.moveTo(corner_x, corner_y)
            pyautogui.dragTo(3368, 804, duration=3)
            time.sleep(2)
            pyautogui.dragTo(2000, 804, duration=2)
            
        else:
            print("Corner image not found on the screen.")
elif choice.lower() == "monkey":
    Tim = random.randint(1,3)

    location = pyautogui.locateOnScreen(monkey)
    if location:
        center_x, center_y = pyautogui.center(location)
        print(f"Image found at: {location}, center: ({center_x}, {center_y})")
        pyautogui.doubleClick(center_x, center_y)
        time.sleep(1)
    else:
        print("Shrek image not found on the screen.")

    while True:
        Tim= random.randint(1,3)
        time.sleep(Tim)
            
        location1 = pyautogui.locateOnScreen(text2)
        if location1:
            corner_x, corner_y = pyautogui.center(location1)
            print(f"Image found at: {location1}, center: ({corner_x}, {corner_y})")
            pyautogui.moveTo(corner_x, corner_y)
            pyautogui.dragTo(3368, 804, duration=2)
            time.sleep(2)
            pyautogui.dragTo(2000, 804, duration=2)
        else:
            print("Corner image not found on the screen.")    

    