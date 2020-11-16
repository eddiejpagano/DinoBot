import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time

is_night = False
color = 83 # Color of the cactus and bird during daytime

def fast_night(data):
    if data[1700,125] != 255:  # Check is the color of the background has changed        
        return True
    return False

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):        
    for x in range(300, 550,5): # Change these numbers to match your screen
        for y in range(630, 670,3): # Change these numbers to match your screen
            #print(data[x,y])            
            if is_night and data[x, y] > color:
                hit("up")
                return
            elif data[x,y] == color:
                hit("up")                    
                return
        """ for y in range(550,565):
            if is_night and data[x, y] > color:
                hit("down")
                return
            elif data[x,y] == color:
                hit("down")                    
                return """
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        is_night = fast_night(data)
        isCollide(data)
            
       
