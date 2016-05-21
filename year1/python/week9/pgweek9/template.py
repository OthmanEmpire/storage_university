#!/usr/bin/env python3
################################################################
## Pygame template, following Harris' IDEA/ALTER approach.    ##
##                                                            ## 
## Author  : Nick Efford                                      ##
## Updated : 2010-11-12                                       ##
################################################################

# I: Importing & initialising

import pygame

pygame.init()

# D: Display configuration

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame Example :o')

# E: Entity creation

background = pygame.Surface(size).convert()
background.fill((128, 0, 0))
i = 0

# A: Action, broken down as ALTER steps...

# A: Assign values to key variables
clock = pygame.time.Clock()
running = True

# L: Loop
while running:
    # T: Timing, to control frame rate
    clock.tick(30)



    # E: Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # R: Refresh display
    screen.blit(background, (0, 0))
    #
    # Code to redraw any moving/changing objects would go here
    #
    pygame.display.flip()
