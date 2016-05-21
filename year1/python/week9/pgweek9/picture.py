#!/usr/bin/env python3
# Example of drawing a simple picture using easypg.
#
# Copyright (c) 2011-12 Nick Efford <nick.efford (at) gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import pygame

from easypg.colours import AQUA, GREEN, NAVY, PURPLE, RED, WHITE
from easypg.fonts import FONTS
from easypg.drawing import draw_ellipse, draw_rect
from easypg.drawing import draw_lines, draw_polygon, draw_text
from easypg.utils import Window, create_surface

pygame.init()

size = (640, 480)
window = Window(size, 'Picture')
background = create_surface(size, WHITE)

draw_rect(background, RED, (80, 75, 120, 165))
draw_ellipse(background, GREEN, (120, 45, 190, 130))

points = ((290, 380), (400, 190), (510, 380))
draw_polygon(background, AQUA, points)
draw_lines(background, NAVY, points, closed=True, antialias=True)

FONTS.set_font(40, 'Sans', bold=True)
draw_text(background, 'easypg', PURPLE, (334, 320))

window.display(background)
