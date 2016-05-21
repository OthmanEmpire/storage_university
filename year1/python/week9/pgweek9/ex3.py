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

# size = (640, 480)
image_size = pygame.image.load("background.jpg").get_size()
screen = pygame.display.set_mode(image_size)
pygame.display.set_caption('Pygame Example')

# E: Entity creation

background = pygame.image.load("background.jpg")
background.convert()

ship = pygame.image.load("ship.png")
ship.convert()
ship.set_colorkey((255,255,255))

rect = ship.get_rect()
rect.center = (300,300)


# background = pygame.Surface(screen.get_size()).convert()
# background.fill((0, 0, 128))


# A: Action, broken down as ALTER steps...

# A: Assign values to key variables
clock = pygame.time.Clock()
running = True

w, h = screen.get_size()

vx = 5
vy = 5

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
    screen.blit(ship, rect)
    #
    # Code to redraw any moving/changing objects would go here
    #
    rect.centerx += vx
    rect.centery += vy

    if rect.left < 0 or rect.right > w:
        vx *= -1
    if rect.top < 0 or rect.bottom > h:
        vy *= -1


    pygame.display.flip()
