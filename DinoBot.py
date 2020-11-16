import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time
is_night = False
color = 83

def fast_night(data):
    global color
    if data[1700,125] != 255:          
        return True
    return False

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):        
    for x in range(300, 550,5):
        for y in range(630, 670,3):
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
            
       
