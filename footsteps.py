import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('footsteps')


def draw_footsteps(x, y, color):
    pygame.draw.ellipse(screen, color,( x - 22//2, (y-5)-40//2, 22, 40))
    pygame.draw.circle(screen, color, (x, y+20), 8)
    pygame.draw.rect(screen, (255, 255, 255), (x-16//2, y+13-3//2, 16, 3))
# background
screen.fill((255, 255, 255))
pygame.draw.rect(screen, (0,0,0), (190, 0, 10, 400))
pygame.draw.rect(screen, (210, 180, 140), (200, 0, 10, 400))




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < 200:
                draw_footsteps(pos[0], pos[1], (0,0,0))
            else:
                draw_footsteps(pos[0], pos[1],(210, 180, 140) )

    pygame.display.update()