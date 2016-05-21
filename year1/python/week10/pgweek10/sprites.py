# CR11 Semester 2, Lab 5


import pygame
import re


def draw_disc(diameter, colour, background=(0, 0, 0)):
    """Returns a surface representing a disc of the given diameter
       and colour, on a transparent background."""

    if diameter < 5:
        raise ValueError('invalid disc diameter')

    if colour == background:
        raise ValueError('colour and background must differ')

    x = y = radius = diameter // 2

    surface = pygame.Surface((diameter, diameter))
    surface = surface.convert()
    # surface.fill(background)
    surface.set_colorkey(background)

    pygame.draw.circle(surface, colour, (x, y), radius)

    return surface


class Disc(pygame.sprite.Sprite):
    """A simple disc-shaped sprite."""

    def __init__(self, screen, diameter, colour,
      background=(0, 0, 0), position=None, velocity=(5, 5)):
        """Creates a Disc for the given screen, with the given diameter
           and colour.  Initial position and velocity can be specified if
           necessary, as tuples.  By default, a Disc will appear in the
           middle of the screen."""

        super().__init__()   # invokes superclass constructor

        self.screen = screen
        self.image = draw_disc(diameter, colour, background)
        self.rect = self.image.get_rect()

        if position:
            self.rect.center = position
        else:
            # No position given, so put sprite at centre of screen
            width, height = self.screen.get_size()
            self.rect.center = (width // 2, height // 2)

        self.vx, self.vy = velocity
        self.w, self.h = self.screen.get_size()

    # TODO: Add an update method here

    def update(self):
        """Updates the sprite"""

        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        if self.rect.left < 0 or self.rect.right > self.w:
            self.vx *= -1

        if self.rect.top < 0 or self.rect.bottom > self.h:
            self.vy *= -1




# TODO: Write additional sprite classes here

class Monster(pygame.sprite.Sprite):

    def __init__(self, screen, velocity=(3, 3)):
        """King Arthur"""

        super().__init__()

        self.screen = screen

        self.images = []
        self.images.append(pygame.image.load("afraid__00.png").convert())
        self.images.append(pygame.image.load("afraid__01.png").convert())
        self.images[0].set_colorkey((97,68,43))
        self.images[1].set_colorkey((97,68,43))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.w, self.h = self.screen.get_size()
        self.vx, self.vy = velocity

        self.anime_speed = 0


    def update(self):
        """King Arthur"""

        self.rect.centerx += self.vx
        self.rect.centery += self.vy
        self.anime_speed += 1

        if self.anime_speed >= 20:

            self.anime_speed = 0
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[self.index]

        if self.rect.left < 0 or self.rect.right > self.w:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > self.h:
            self.vy *= -1



class Player(pygame.sprite.Sprite):

    def __init__(self, screen, velocity=(3, 3)):
        """King Arthur"""

        super().__init__()

        self.screen = screen

        self.images = []
        self.images.append(pygame.image.load("afraid__00.png").convert())
        self.images.append(pygame.image.load("afraid__01.png").convert())
        self.images[0].set_colorkey((97,68,43))
        self.images[1].set_colorkey((97,68,43))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.w, self.h = self.screen.get_size()
        self.vx, self.vy = velocity

        self.anime_speed = 0


    def move(self):
        """King Arthur"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.centerx -= self.vx
        if keys[pygame.K_RIGHT]:
            self.rect.centerx += self.vx
        if keys[pygame.K_UP]:
            self.rect.centery -= self.vy
        if keys[pygame.K_DOWN]:
            self.rect.centery += self.vx


    def check_bounds(self):
        """King Arthur"""
        if self.rect.centerx < 0:
            self.rect.centerx = self.w - 1
        elif self.rect.centerx > self.w:
            self.rect.centerx = 0
        elif self.rect.centery < 0:
            self.rect.centery = self.h - 1
        elif self.rect.centery > self.h:
            self.rect.centery = 0






    def update(self):
        """King Arthur"""

        self.move()
        self.check_bounds()

        # self.rect.centerx += self.vx
        # self.rect.centery += self.vy


        self.anime_speed += 1

        if self.anime_speed >= 20:

            self.anime_speed = 0
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[self.index]
