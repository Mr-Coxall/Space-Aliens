#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: July 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game scene
    
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # a list of sprites that will be updated every frame
    sprites = []
    
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_background, 10, 8)
    # 4 is the x tile spot, 3 is the y tile spot, 2 is the tile image number
    background.tile(4, 3, 2) # x, y, image number
    
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        pass


if __name__ == "__main__":
    game_scene()
