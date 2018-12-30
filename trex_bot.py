from numpy import *
from PIL import ImageGrab,ImageOps
import pyautogui as py


def pressSpace():
    py.keyDown('space')
    py.keyUp('space')


def IMG():
    Box=(202,471,303,509)    #Use your own Coordinates here
    image=ImageGrab.grab(Box)
    image=ImageOps.grayscale(image)
    arr=array(image.getcolors())
    return(arr.sum())


def main():
    print("Starting Game.....")
    x=0
    while(1):
        ab=IMG()
        print(ab)
        if(ab !=4085):
            pressSpace()
            x=x+1
            print("     Jumping "+str(x)+" times")


main()

