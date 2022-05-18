"""
Rohan Shah
realistic ball bouncing based on mouse chosen height
ball speeds as it gets closer to mimic acceleration
"""

import pygame
from pygame.locals import *

FPS = 30
pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption("bouncing ball")
clock = pygame.time.Clock()

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )        

radius = 20
ball_centerY = 200
ball_centerX = 200
ball_speed = 0
while True:
    
    gradientRect(screen, (255, 250, 250), (135, 206, 235), pygame.Rect(0, 0, 400, 400))

    pygame.draw.circle(screen, (128, 0, 0), (ball_centerX, ball_centerY), radius)

    bottom = ball_centerY + radius

    if bottom < 400:
        ball_speed += 1
    else:
        ball_speed *= -1

    ball_centerY += ball_speed

    if ball_centerY + radius > 400:
        ball_centerY = 400 - radius
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            ball_centerX, ball_centerY = pos
            ball_speed = 0

    clock.tick(FPS)
    pygame.display.update()