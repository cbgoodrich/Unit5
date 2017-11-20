#Charlie Goodrich
#11/20/17
#antsDemo.py - how to use lists with graphics

from ggame import *
from random import randint

#CONSTANTS
WIDTH = 1000
HEIGHT = 500

def step():
    for ant in data["antList"]:
        dx = randint(-4,3)
        dy = randint(-4,3)
        ant.x += dx
        ant.y += dy

if __name__ == "__main__":
    
    red = Color(0xFF0000, 1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    data = {}
    data["antList"] = []
    
    
    for i in range(10):
        data["antList"].append(Sprite(ant,(randint(1,WIDTH), randint(1,HEIGHT))))
    
    App().run(step)
