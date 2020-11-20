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
    
    # sets the background to image 0 in the image bank
    #   and the sie (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)
    
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
