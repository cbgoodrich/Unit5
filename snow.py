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
    xPos = randint(0, WINDOW_X-CELL_SIZE)
    data["snowList"].append(Sprite(snow, (CELL_SIZE*xPos, 0)))
    data["fallPosition"][xPos] += 1
    data["stopFlake"].append(data["fallPosition"][xPos])
    print(data["stopFlake"])


def step():
    data["frames"] += 1
    if data["frames"] == 5:
        spawnSnow()
        data["frames"] = 0
    spot = 0
    for flake in data["snowList"]:
        flake.y += 1
        if flake.y == (WINDOW_X - CELL_SIZE*(data["stopFlake"][spot])):
            data["snowList"].remove(flake)
            data["stopFlake"].remove(data["stopFlake"][spot])
        place += 1

if __name__ == "__main__":
    
    COLS = WINDOW_X/CELL_SIZE
    
    snowList = []
    
    data = {}
    data["frames"] = 0
    data["snowList"] = []
    data["fallPosition"] = []
    data["stopFlake"] = []
    
    for i in range(0, COLS):
        data["fallPosition"].append(0)
        
    
    
    white = Color(0xFFFFFF, 1)
    blue = Color(0x000080, 1)
    
    snow = RectangleAsset(CELL_SIZE, CELL_SIZE, LineStyle(1, white), white)
    sky = RectangleAsset(WINDOW_X, WINDOW_Y, LineStyle(1, blue), blue)
    
    Sprite(sky)
    
    
    
    
    App().run(step)
    
    
