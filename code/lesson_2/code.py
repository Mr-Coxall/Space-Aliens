#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: July 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens_background.bmp")

def main():
    # this function a single background tile
    
    # sets the background to image 2 in the image bank (space ship)
    # if your 0 image is magenta, your background will most likely be distorted
    # backgrounds do not have magenta as a transparent color
    background = stage.Grid(image_bank_1, 10, 8)
    # 4 is the x tile spot, 3 is the y tile spot, 2 is the tile image number
    background.tile(4, 3, 2) # x, y, image number
    
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # repeat forever, or you turn it off!
        pass


if __name__ == "__main__":
    main()
