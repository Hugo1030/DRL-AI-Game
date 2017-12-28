# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *
from math import pi

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Drawing!')

# colors init
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)

# draw line
pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
