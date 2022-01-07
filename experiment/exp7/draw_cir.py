import pygame
import sys
from pygame.locals import *


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("move cir")
    x, y = 50, 50
    pygame.draw.circle(screen, [255, 0, 0], [x, y], 50, 0)
    clock = pygame.time.Clock()

    while True:
        clock.tick(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x -= 10
                if event.key == K_RIGHT:
                    x += 10
                if event.key == K_UP:
                    y -= 10
                if event.key == K_DOWN:
                    y += 10
        if x + 50 < 600 and y == 50:
            x += 1
        if x + 50 == 600 and y + 50 < 500:
            y += 1
        if y == 450:
            x -= 1
        if x == 50:
            y -= 1
        pygame.display.update()
        screen.fill([255, 255, 255])
        pygame.draw.circle(screen, [255, 0, 0], [x, y], 50, 0)
