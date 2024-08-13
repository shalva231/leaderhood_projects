import pyautogui
import time
import os


target_image =  os.path.join(r'C:\Users\PC\Desktop\projects\projects\july and august\TEST', 'image.png')


def scroll_down():
    pyautogui.scroll(-300)


while True:
    try: 
        location = pyautogui.locateOnScreen(target_image)
        print("Element found!")
        break

    except pyautogui.ImageNotFoundException:
        pass

    finally:
        scroll_down()
