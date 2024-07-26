import pyautogui
import os
import time

monkey = os.path.join(r"C:\Users\er555\Desktop\leaderhood_projects\projects\july\pyautogui\monkey", "monkey.png")
text = os.path.join(r"C:\Users\er555\Desktop\leaderhood_projects\projects\july\pyautogui\monkey", "text.png")

location = pyautogui.locateOnScreen(monkey)
if location:
    center_x, center_y = pyautogui.center(location)
    print(f"Image found at: {location}, center: ({center_x}, {center_y})")
    pyautogui.doubleClick(center_x, center_y, duration=1)
    time.sleep(2)
    
    location1 = pyautogui.locateOnScreen(text)
    if location1:
        corner_x, corner_y = pyautogui.center(location1)
        print(f"Image found at: {location1}, center: ({corner_x}, {corner_y})")
        pyautogui.moveTo(corner_x, corner_y, duration=1)
        pyautogui.dragTo(3368, 804, duration=3)
        time.sleep(1)
        pyautogui.dragTo(2000, 804, duration=2)
    else:
        print("Corner image not found on the screen.")
else:
    print("monkey image not found on the screen.")
