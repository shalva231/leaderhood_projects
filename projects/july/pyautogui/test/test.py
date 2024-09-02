import pyautogui
import time
import os

def find_element_on_screen(image_path, max_attempts=10, scroll_amount=-100):
    """
    Scrolls the screen until the specified image is found or max attempts are reached.

    :param image_path: Path to the image file to be detected on screen.
    :param max_attempts: Maximum number of scroll attempts before raising an error.
    :param scroll_amount: The amount to scroll on each attempt (negative for scrolling down).
    :return: Location of the element if found.
    :raises: Exception if the element is not found after max_attempts.
    """
    attempts = 0
    
    while attempts < max_attempts:
        location = pyautogui.locateOnScreen(image_path)
        if location:
            return location
        
        pyautogui.scroll(scroll_amount)
        time.sleep(1)  # Add a delay to allow the screen to refresh
        
        attempts += 1
    
    raise Exception(f"Element not found after {max_attempts} attempts")

try:
    element_location = os.path.join(r"C:/Users/er555/Desktop/leaderhood_projects/projects/july/pyautogui/shrekey", "monkey.png")
    print(f"Element found at: {element_location}")
except Exception as e:
    print(str(e))
