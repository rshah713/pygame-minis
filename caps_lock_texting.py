"""
Rohan Shah
8/28/22

Change the line at the bottom to change the texts
True/False controls Caps Lock
Each string is a text bubble
"""

import pygame
from pygame.locals import *
import string

GREY = (128,128,128)
LIGHTGREY = (211,211,211)
WHITE = (255,255,255)
DIMGREY = (105,105,105)
GHOSTWHITE = (248,248,255)
GAINSBORO = (220,220,220)
RED = (255,0,0)
LIGHTGRAY = (211,211,211)
DODGERBLUE = (30,144,255)
DARKGREY = (169,169,169)
DARKGRAY = (169,169,169)
CORNSILK = (255,248,220)
WHEAT = (245,222,179)
BLACK = (0, 0, 0)

# Letters used to populate the keyboard.
LETTERS = string.ascii_lowercase

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )  

def centerLeft(tup):
    # center-aligned rect --> left-top aligned rect
    new_x = tup[0] - tup[2]//2
    new_y = tup[1] - tup[3]//2
    return (new_x, new_y, tup[2], tup[3])

def bottomLeft(tup):
    # bottom-left rect --> left-top aligned rect
    new_y = tup[1] - tup[3]
    return (tup[0], new_y, tup[2], tup[3])


def draw_keyboard():
    # outline and buttons
    pygame.draw.rect(screen, LIGHTGREY, (110, 235, 180, 90))

    pygame.draw.rect(screen, WHITE, (116, 218, 155, 15))
    pygame.draw.rect(screen, LIGHTGREY, (116, 218, 155, 15), 1)
    txt = contactFont2.render('Text Message', True, DARKGREY)
    txt_r = txt.get_rect()
    txt_r.topleft = (120, 222)
    screen.blit(txt, txt_r)
    pygame.draw.rect(screen, DODGERBLUE, (275, 218, 12, 15))
    pygame.draw.rect(screen, WHITE, (281-2, 224, 4, 5))
    pygame.draw.polygon(screen, WHITE, ((281, 220), (285, 224), (277, 224)))
    pygame.draw.rect(screen, WHITE, (200-35, 308, 70, 12))
    pygame.draw.rect(screen, DARKGREY, (262, 285, 21, 20))
    txt = contactFont2.render('del', True, BLACK)
    txt_r = txt.get_rect()
    txt_r.center = (272, 295)
    screen.blit(txt, txt_r)
    pygame.draw.rect(screen, DARKGREY, (116, 285, 19, 20))

    pygame.draw.polygon(screen, WHITE, ((125, 288), (131, 295), (119, 295)))
    arrow = pygame.Rect(125, 295, 5, 7)
    arrow.midtop = (125, 295)
    pygame.draw.rect(screen, WHITE, arrow)

    # Draws all of the keys using the letters string.
    for index in range(len(LETTERS)):
        letter = LETTERS[index]

        # first row?
        if index < 10:
            x = 123 + index * 17
            y = 248
        # 2nd row
        elif index < 19:
            x = 130 + (index - 10) * 17
            y = 271
        # The third row.
        else:
            x = 147 + (index - 19) * 17
            y = 295

        let = pygame.Rect(x, y, 14, 20)
        let.center = (x, y)
        pygame.draw.rect(screen, WHITE, let)

        let = letterFont.render(letter, True, BLACK)
        let_r = let.get_rect()
        let_r.center = (x, y)
        screen.blit(let, let_r)



def caps_lock(isCapsOn, text1, text2, text3):
    if isCapsOn:
        text1 = text1.upper()
        text2 = text2.upper()
        text3 = text3.upper()
    else:
        text1 = text1.lower()
        text2 = text2.lower()
        text3 = text3.lower()
    f = contactFont2.render(text1, True, BLACK)
    f_r = f.get_rect()
    f_r.topleft = (125, 125)
    screen.blit(f, f_r)
    f = contactFont2.render(text2, True, WHITE)
    f_r = f.get_rect()
    f_r.topleft = (185, 155)
    screen.blit(f, f_r)
    f = contactFont2.render(text3, True, BLACK)
    f_r = f.get_rect()
    f_r.topleft = (125, 185)
    screen.blit(f, f_r)
        
    
    
    
pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Caps Lock Texting')
font = pygame.font.Font('freesansbold.ttf', 6)
contactFont = pygame.font.Font('freesansbold.ttf', 8)
contactFont2 = pygame.font.Font('freesansbold.ttf', 10)
letterFont = pygame.font.Font('freesansbold.ttf', 12)

# background
gradientRect(screen, CORNSILK, WHEAT, pygame.Rect(0, 0, 400, 400))

# screen borders
pygame.draw.rect(screen, BLACK, (100, 30, 200, 340))
pygame.draw.rect(screen, BLACK, (110, 20, 180, 360))
pygame.draw.circle(screen, BLACK, (110, 30), 10)
pygame.draw.circle(screen, BLACK, (110, 370), 10)
pygame.draw.circle(screen, BLACK, (290, 30), 10)
pygame.draw.circle(screen, BLACK, (290, 370), 10)

pygame.draw.rect(screen, WHITE, (110, 60, 180, 265))
pygame.draw.rect(screen, DIMGREY, centerLeft((200, 45, 50, 5)))
pygame.draw.rect(screen, GHOSTWHITE, (110, 60, 180, 50))
pygame.draw.line(screen, GAINSBORO, (110, 110), (290, 110))
pygame.draw.circle(screen, DIMGREY, (150, 45), 5)
pygame.draw.circle(screen, DIMGREY, (200, 30), 3)
pygame.draw.circle(screen, DIMGREY, (200, 350), 13)

# status bar
pygame.draw.rect(screen, BLACK, bottomLeft((113, 70, 2, 2)))
pygame.draw.rect(screen, BLACK, bottomLeft((116, 70, 2, 3)))
pygame.draw.rect(screen, BLACK, bottomLeft((119, 70, 2, 5)))
pygame.draw.rect(screen, LIGHTGREY, bottomLeft((122, 70, 2, 7)))
time = font.render('8:00', True, BLACK)
time_r = time.get_rect()
time_r.center = (200, 65)
screen.blit(time, time_r)
pygame.draw.rect(screen, GHOSTWHITE, (275, 63, 10, 5))
pygame.draw.rect(screen, GREY, (275, 63, 10, 5), 1)
pygame.draw.rect(screen, RED, (276, 64, 2, 3))

# contact info
pygame.draw.circle(screen, LIGHTGREY, (200, 83), 11)
cf2 = contactFont2.render('PM', True, WHITE)
cf2_r = cf2.get_rect()
cf2_r.center = (200, 83)
screen.blit(cf2, cf2_r)
cf = contactFont.render("Pygame Minis", True, BLACK)
cf_r = cf.get_rect()
cf_r.center = (200, 100)
screen.blit(cf, cf_r)

# text bubbles
pygame.draw.rect(screen, LIGHTGREY, (120, 120, 100, 20))
pygame.draw.rect(screen, DODGERBLUE, (280-100, 150, 101, 20))
pygame.draw.rect(screen, LIGHTGREY, (120, 180, 100, 20))
pygame.draw.polygon(screen, LIGHTGREY, ((120, 140), (130, 140), (120, 150)))
pygame.draw.polygon(screen, DODGERBLUE, ((280, 170), (270, 170), (280, 180)))
pygame.draw.polygon(screen, LIGHTGREY, ((120, 200), (130, 200), (120, 210)))


draw_keyboard()

### CHANGE CODE HERE
### UNCOMMMENT ONE OF THESE LINES OR MAKE YOUR OWN
### True/False represents caps lock

caps_lock(True, 'sup ma dude', 'y u yelling?', 'sorry caps lock')

# caps_lock(False, 'NEW PHONE WHO DIS', 'pls stop w that lol', 'sorry sorry')

# caps_lock(False, 'IS CAPS LOCK WORKING?', 'i guess not', 'aww thats sad')


pygame.display.update()

