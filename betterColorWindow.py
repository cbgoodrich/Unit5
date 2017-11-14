#Charlie Goodrich
#11/14/17
#betterColorWindow.py - a better color window program

from ggame import *
from random import randint

num = randint(0,3)

colorList = [0xFF0000, 0x00FF00, 0x0000FF]

def mouseClick(event):
    
    color = Color(num, 1)
    
    rect = RectangleAsset(1000, 1000, LineStyle(1, color), color)
    Sprite(rect)

App().listenMouseEvent("click", mouseClick)
App().run()
