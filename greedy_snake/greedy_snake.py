# -*- coding: utf-8 -*-

import pygame
import random

WHITE = (0xff, 0xff, 0xff)
BLACK = (0, 0, 0)
GREEN = (0, 0xff, 0)
RED = (0xff, 0, 0)
LINE_COLOR = (0x33, 0x33, 0x33) # gray -80%

D_LEFT, D_RIGHT, D_UP, D_DOWN = 0, 1, 2, 3

pygame.init()

WIDTH, HEIGHT = 500, 500
CUBE_WIDTH = 20
GRID_WIDTH_NUM, GRID_HEIGHT_NUM = int(WIDTH / CUBE_WIDTH), int(HEIGHT / CUBE_WIDTH)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GreedySnake")

# refreshing init
clock = pygame.time.Clock()
FPS = 30

running = True
counter = 0
direction = D_LEFT

# add body to the tail
snake_body = []
snake_body.append((int(GRID_WIDTH_NUM / 2) * CUBE_WIDTH,
                   int(GRID_HEIGHT_NUM / 2) * CUBE_WIDTH))

def draw_grids():
    for i in range(GRID_WIDTH_NUM):
        pygame.draw.line(screen, LINE_COLOR,
                         (i * CUBE_WIDTH, 0), (i * CUBE_WIDTH, HEIGHT))

    for i in range(GRID_HEIGHT_NUM):
        pygame.draw.line(screen, LINE_COLOR,
                         (0, i * CUBE_WIDTH), (WIDTH, i * CUBE_WIDTH))

def draw_body():
    for sb in snake_body:
        pygame.draw.rect(screen, WHITE, (sb[0], sb[1], CUBE_WIDTH, CUBE_WIDTH))

    # chage head red
    pygame.draw.rect(screen, RED,
                     (snake_body[0][0],
                      snake_body[0][1],
                      CUBE_WIDTH,
                      CUBE_WIDTH))

food_pos = None

def generate_food():
    return (random.randint(0, GRID_WIDTH_NUM - 1),
            random.randint(0, GRID_HEIGHT_NUM -1))

def draw_food():
    pygame.draw.rect(screen, GREEN,
                     (food_pos[0] * CUBE_WIDTH,
                      food_pos[1] * CUBE_WIDTH, CUBE_WIDTH, CUBE_WIDTH))

def grow():
    if snake_body[0][0] == food_pos[0] * CUBE_WIDTH and\
            snake_body[0][1] == food_pos[1] * CUBE_WIDTH:
        return True
    return False


