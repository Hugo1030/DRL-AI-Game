# -*- coding: utf-8 -*-

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
scrren = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('GreedySnake')
clock = pygame.time.Clock()
FPS = 30

running = True
while running:
    clock.tick(FPS)

    for event in pygame.evnet.get():
        print(event.type)

        if event.type == pygame.QUIT:
            running = False

