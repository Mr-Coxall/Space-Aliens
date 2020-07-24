#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: July 2020
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage

import constants


# image banks for CircuitPython
image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

# a list of sprites that will be updated every frame
sprites = []

def main():
    # this function shows 2 sprites on a background
    
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_background, constants.SCREEN_X, 
                            constants.SCREEN_Y)
    
    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_sprites, 9, 
                         int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                         int(constants.SCREEN_Y / 2 - constants.SPRITE_SIZE / 2))
    sprites.append(alien) 
    ship = stage.Sprite(image_bank_sprites, 5,
                        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - 16))
    sprites.insert(0, ship) # insert at top of sprite list
    
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X != 0:
            print("A")
        if keys & ugame.K_O != 0:
            print("B")
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")
            
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)
        
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
                
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        
        # update game logic
        
        # redraw sprite list
        game.render_sprites(sprites)
        game.tick() # wait until refresh rate finishes


if __name__ == "__main__":
    main()