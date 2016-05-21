#!/usr/bin/env python3
# CR11 Semester 2, Lab 5

import pygame
import sprites

pygame.init()

# Configure display

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('CR11 Lab 5')

# Define some colours

grey = (180, 180, 180)
red = (255, 0, 0)

# Create a background image and display it

background = pygame.Surface(size).convert()
background.fill(grey)
screen.blit(background, (0, 0))

# TODO: Create sprite and sprite group

disc1 = sprites.Disc(screen, 50, (128,0,0))
disc2 = sprites.Disc(screen, 25, (0,128,0), velocity=(10,10))
disc3 = sprites.Disc(screen, 10, (0,0,128), velocity=(25,25))
group = pygame.sprite.Group(disc1, disc2, disc3)

mons1 = sprites.Monster(screen)
group.add(mons1)

player = sprites.Player(screen)
group.add(player)


# Define variables to control the action

clock = pygame.time.Clock()
running = True

# Enter the main event loop...

while running:
    clock.tick(30)   # max 30 fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: Clear, update and redraw sprite group

    group.clear(screen, background)
    group.update()
    group.draw(screen)

    pygame.display.flip()
