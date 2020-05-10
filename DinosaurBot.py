from PIL import ImageGrab, ImageOps
import pyautogui
import webbrowser
import time
from numpy import *

class Coordinates():
    replayBtn = (331, 417)
    dinosaur = (173, 422)
    game_over = (241, 368)
    #385  y   412 / 416
    #214  x   267/ 260 

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    #print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Coordinates.dinosaur[0]+60, Coordinates.dinosaur[1], Coordinates.dinosaur[0]+100, Coordinates.dinosaur[1]+23)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def gameOver():
    box = (Coordinates.game_over[0], Coordinates.dinosaur[1], Coordinates.dinosaur[0]+197, Coordinates.dinosaur[1]+13)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def restart():
    pyautogui.click(Coordinates.replayBtn)
           
def game():
    restart()
    time.sleep(0.1)
    while True:
        if(imageGrab()!=1167):
            if(gameOver()==2172):
                break
            pressSpace()
            time.sleep(0.1)

if __name__ == "__main__":
    game()
