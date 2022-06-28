'''
Rohan Shah

each mouseclick brings the volcano closer to eruption
'''

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
background1 = (135, 206, 235)
background2 = (235, 235, 235)
VOCANO_ERUPTED = False
LAVA_GREEN = 200
BURST_VISIBLE = False

def draw_spill():
    pygame.draw.polygon(screen, (235, 10, 20), ((153, 120), (175, 125), (165, 195), (145, 260), (80, 315), (125, 260), (150, 200), (155, 160)))
    pygame.draw.polygon(screen, (235, 10, 20), ((200, 120), (220, 108), (230, 160), (230, 210), (240, 240), (310, 345), (245, 280), (215, 225), (210, 160)))
    pygame.draw.polygon(screen, (235, 10, 20), ((235, 105), (247, 110), (255, 175), (270, 210), (310, 250), (255, 215), (240, 170), (240, 130)))

    
def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )
    
while True:

    gradientRect(screen, background1, background2, pygame.Rect(0, 0, 400, 400))

    pygame.draw.ellipse(screen, (255, LAVA_GREEN, 0), (200-90/2, 120-10, 90, 20))
    pygame.draw.ellipse(screen, (205, 133, 63), (200-90/2, 120-10, 90, 20), 4)

    pygame.draw.polygon(screen, (205, 133, 63), ((0, 400), (0, 380), (50, 340), (70, 300), (125, 225), (140, 180), (153, 120), (175, 125), (200, 120), (220, 108), (235, 105), (247, 110), (255, 175), (270, 210), (310, 250), (350, 325), (400, 375), (400, 400)))


    if BURST_VISIBLE:
        pygame.draw.polygon(screen, (255, 200, 75), ((100, 0), (310, 0), (260, 30), (245, 60), (240, 110), (235, 105), (220, 108), (200, 120), (175, 125), (160, 120), (150, 60), (130, 25)))
        draw_spill()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if LAVA_GREEN > 0:
                LAVA_GREEN -= 40
            elif not VOCANO_ERUPTED:
                BURST_VISIBLE = True
                background1 = (119, 136, 153)
                background2 = (211, 211, 211)
                VOCANO_ERUPTED = True
    pygame.display.update()

