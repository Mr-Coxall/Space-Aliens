#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: July 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

# a list of sprites that will be updated every frame
sprites = []

def main():
    # this function a single background tile
    
    # sets the background to image 2 in the image bank (space ship)
    # if your 0 image is magenta, your background will most likely be distorted
    # backgrounds do not have magenta as a transparent color
    background = stage.Grid(image_bank_background, 10, 8)
    
    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_sprites, 9, 64, 26)
    sprites.append(alien) 
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    sprites.insert(0, ship) # insert at top of sprite list
    
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        
        # update game logic
        
        # redraw sprite list
        game.render_sprites(sprites)
        game.tick() # wait until refresh rate finishes


if __name__ == "__main__":
    main()
