"""
Rohan Shah
If clicked in the sky, cloud is drawn based on RGB of mouseY
If """

import pygame
from pygame.locals import *
from _flowers_and_clouds import draw_cloud, draw_flower

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption("flowers and clouds")

screen.fill((0, 191, 255))

# ground
pygame.draw.rect(screen, (107, 142, 35), (0, 255, 400, 145))
pygame.draw.ellipse(screen, (107, 142, 35), (0, 255-10, 400, 20))

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] < 255:
                draw_cloud(screen, pos[0], pos[1], (pos[1], pos[1], pos[1]))
            if pos[1] >= 255:
                draw_flower(screen, pos[0], pos[1])

    pygame.display.update()