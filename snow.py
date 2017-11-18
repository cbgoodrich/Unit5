#Charlie Goodrich
#11/18/17
#snow.py - makes snow fall and accumulates on the ground

from ggame import *

#CONSTANTS
WINDOW_X = 1000
WINDOW_Y = 525
CELL_SIZE = 10

def moveSnow():
    snow.y += CELL_SIZE
    data["frames"] = 0
    if snow.y >= WINDOW_Y-CELL_SIZE:
        data["frames"] = 6

def step():
    data["frames"] += 1
    if data["frames"] == 5:
        moveSnow()

if __name__ == "__main__":
    
    data = {}
    data["frames"] = 0
    
    white = Color(0xFFFFFF, 1)
    blue = Color(0x000080, 1)
    
    whiteBox = RectangleAsset(CELL_SIZE, CELL_SIZE, LineStyle(1, white), white)
    sky = RectangleAsset(WINDOW_X, WINDOW_Y, LineStyle(1, blue), blue)
    
    Sprite(sky)
    snow = Sprite(whiteBox, (500, 200))
    
    App().run(step)
    
    
