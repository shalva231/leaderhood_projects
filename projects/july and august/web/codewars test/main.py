import pyautogui
import time
import os

# Image paths
kyu = os.path.join(r'C:\Users\PC\Desktop\projects\projects\july and august\web\codewars test\imgs', '8.png')
cgpt = os.path.join(r'C:\Users\PC\Desktop\projects\projects\july and august\web\codewars test\imgs', 'cgpt.png')
chat = os.path.join(r'C:\Users\PC\Desktop\projects\projects\july and august\web\codewars test\imgs', 'chat.png')
copy = os.path.join(r'C:\Users\PC\Desktop\projects\projects\july and august\web\codewars test\imgs', 'copy.png')



#time to go to opera
time.sleep(2)

while True:

    # Locate and click 'kyu' image
    location = pyautogui.locateOnScreen(kyu)
    if location:
        x, y = pyautogui.center(location)
        print(f"Image found at: {location}, center: ({x}, {y})")
        pyautogui.click(x, y)
        time.sleep(4)
    else:
        print("Kyu image not found on the screen.")

    # click on first kata
    pyautogui.click(x=605, y=375)
    time.sleep(4)

    # Open the kata
    kata1 =  os.path.join(r'C:\Users\PC\Desktop\projects\projects\july and august\web\codewars test\imgs', 'train.png')
    kata2 =  os.path.join(r'C:\Users\PC\Desktop\projects\projects\july and august\web\codewars test\imgs', 'train1.png')
    
    try:
        location = pyautogui.locateOnScreen(kata1)
        x, y = pyautogui.center(location)
        print(f"Image found at: {location}, center: ({x}, {y})")
        pyautogui.click(x, y)

    except pyautogui.ImageNotFoundException:
        location = pyautogui.locateOnScreen(kata2)
        x, y = pyautogui.center(location)
        print(f"Image found at: {location}, center: ({x}, {y})")
        pyautogui.click(x, y)
 
    time.sleep(3)

    # Copy the kata to clipboard
    pyautogui.moveTo(x=136, y=340)

    pyautogui.dragTo(360, 730, duration=3)    
    
    pyautogui.hotkey('ctrl', 'c')

    # Locate and click 'cgpt' image
    location = pyautogui.locateOnScreen(cgpt)
    if location:
        x, y = pyautogui.center(location)
        print(f"Image found at: {location}, center: ({x}, {y})")
        pyautogui.click(x, y, duration=1)
        time.sleep(2)
    else:
        print("GPT image not found on the screen.")

    # Locate and click 'chat' image
    pyautogui.click(x=814, y=662)


    # Tell GPT to solve the kata
    pyautogui.typewrite("in py Solve the kata without any explanations no comments no examples no test cases write just the solved kata. the kata is:", interval=0.02)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(x=141, y=18)
    pyautogui.click(x=918, y=430)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')

    location = pyautogui.locateOnScreen(cgpt)
    if location:
        x, y = pyautogui.center(location)
        print(f"Image found at: {location}, center: ({x}, {y})")
        pyautogui.click(x, y)
        time.sleep(2)
    else:
        print("GPT image not found on the screen.")

    pyautogui.click(x=1150, y=660)
    pyautogui.hotkey('shift', 'enter')
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('enter')
    time.sleep(2)




    # Wait for the solution
    time.sleep(10)
    pyautogui.moveRel(0, -100) 
    
    Try:
        
    
    while True:
        try:
            location = pyautogui.locateOnScreen(copy)
            x, y = pyautogui.center(location)
            print(f"Image found at: {location}, center: ({x}, {y})")
            pyautogui.click(x, y)
            break

        except pyautogui.ImageNotFoundException:
            pyautogui.scroll(50)

    # Complete the kata
    pyautogui.click(x=141, y=18)
    pyautogui.click(x=918, y=430)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(0.5)
    pyautogui.scroll(-2000)
    pyautogui.scroll(-2000)

    pyautogui.moveTo(x=1293, y=688)
    pyautogui.click(x=1293, y=688)
    time.sleep(5)
    pyautogui.click(x=1293, y=688)
    time.sleep(5)












