#Charlie Goodrich
#11/18/17
#snow.py - makes snow fall and accumulates on the ground

from ggame import *
from random import randint

#CONSTANTS
WINDOW_X = 1000
WINDOW_Y = 520
CELL_SIZE = 10

def spawnSnow():
    data["snowList"].append(Sprite(snow,(randint(0, WINDOW_X))))

def step():
    data["frames"] += 1
    if data["frames"] == 5:
        spawnSnow()
    for flake in data["snowList"]:
        if flake.y <= WINDOW_X:
            flake.y += 5

if __name__ == "__main__":
    
    snowList = []
    
    data = {}
    data["snowList"] = []
    
    
    white = Color(0xFFFFFF, 1)
    blue = Color(0x000080, 1)
    
    snow = RectangleAsset(CELL_SIZE, CELL_SIZE, LineStyle(1, white), white)
    sky = RectangleAsset(WINDOW_X, WINDOW_Y, LineStyle(1, blue), blue)
    
    Sprite(sky)
    
    
    
    
    App().run(step)
    
    
