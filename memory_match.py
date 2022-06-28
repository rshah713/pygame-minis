"""
Rohan Shah
simple memory match game
click on the cards before the time runs out
"""


import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('memory match')
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 30)
time_fnt = pygame.font.Font('freesansbold.ttf', 20)
directions_fnt = pygame.font.Font('freesansbold.ttf', 16)
win_fnt = pygame.font.Font('freesansbold.ttf', 40)

FPS = 1
ROWS = 3
COLS = 4
CARDS = [[None, None, None, None], [None, None, None, None], [None, None, None, None]]
FIRST_CARD = None
SECOND_CARD = None
timer = 45
chosen_row1 = None
chosen_col1 = None
chosen_row2 = None
chosen_col2 = None

def set_color(color):
    global CARDS, cnt

    row = random.randrange(0, ROWS)
    col = random.randrange(0, COLS)

    while CARDS[row][col] is not None:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)

    x = 20 + col * 100
    y = 100 + row * 100
    r = pygame.Rect(x, y, 60, 80)
    # convert 2d index to 1d
    ind = (row * ROWS) + col
    CARDS[row][col] = {ind:[r, color]}


def initialize_cards():
    # colors = [ 'red', 'lightBlue', 'blue', 'orange', 'pink', 'purple' ]
    colors = [(255, 0, 0), (173, 216, 230), (0, 0, 255), (255, 165, 0), (255, 192, 203), (128, 0, 128)]

    for color in colors:
        set_color(color)
        set_color(color)

    for row in CARDS:
        for pair in row:
            rect = list(pair.values())[0][0]
            pygame.draw.rect(screen, (169, 169, 169), rect)
            pygame.draw.rect(screen, (0,0,0), rect, 4)


def find_card(x, y):
    global chosen_row1, chosen_col1, chosen_row2, chosen_col2
    for row in range(ROWS):
        for col in range(COLS):
            crd_item = CARDS[row][col]
            card = list(crd_item.values())[0][0]
            if card.collidepoint(x, y):
                if FIRST_CARD == None:
                    chosen_row1 = row
                    chosen_col1 = col
                else:
                    chosen_row2 = row
                    chosen_col2 = col
                return crd_item

def check_win():
    for row in range(ROWS):
        for col in range(COLS):
            if (list(CARDS[row][col].values())[0][1] != (0, 0, 0)):
                return False
    return True

screen.fill((255, 255, 255))
msg = font.render('Memory Match', True, (0, 0, 0))
msg_rect = msg.get_rect()
msg_rect.center = (200, 20)
screen.blit(msg, msg_rect)

msg = time_fnt.render('Time Remaning: ', True, (0, 0, 0))
msg_rect = msg.get_rect()
msg_rect.center = (180, 50)
screen.blit(msg, msg_rect)


msg = directions_fnt.render('Try to match all of the cards before time runs out', True, (0, 0, 0))
msg_rect = msg.get_rect()
msg_rect.center = (200, 80)
screen.blit(msg, msg_rect)

msg = time_fnt.render(str(timer), True, (0, 0, 0))
msg_rect = msg.get_rect()

initialize_cards()

while True:

    clock.tick(FPS)

    pygame.draw.rect(screen, (255, 255, 255), msg_rect)
    
    msg = time_fnt.render(str(timer), True, (0, 0, 0))
    msg_rect = msg.get_rect()
    msg_rect.center = (270, 50)
    screen.blit(msg, msg_rect)



    if SECOND_CARD != None:
        # Check if we've clicked on two cards.
        # Compare the fills of the cards.
        # If they don't match, set the fills to darkGray.
        # If they do match, set the borders to lime.
        # Either way, reset both card variables to None.
        if list(FIRST_CARD.values())[0][1] != list(SECOND_CARD.values())[0][1]:
            pygame.draw.rect(screen, (169, 169, 169), list(FIRST_CARD.values())[0][0])
            pygame.draw.rect(screen, (0,0,0), list(FIRST_CARD.values())[0][0], 4)
            pygame.draw.rect(screen, (169, 169, 169), list(SECOND_CARD.values())[0][0])
            pygame.draw.rect(screen, (0,0,0), list(SECOND_CARD.values())[0][0], 4)
        else:
            pygame.draw.rect(screen, (0, 255, 0), list(FIRST_CARD.values())[0][0], 4)
            pygame.draw.rect(screen, (0, 255, 0), list(SECOND_CARD.values())[0][0], 4)

            # set the fill of CARDS to black to show card is done
            pair = CARDS[chosen_row1][chosen_col1]
            pairlist = list(pair.values())[0]
            pairlist[1] = (0, 0, 0)
            CARDS[chosen_row1][chosen_col1] = {list(pair.keys())[0]: pairlist}

            pair2 = CARDS[chosen_row2][chosen_col2]
            pairlist2 = list(pair2.values())[0]
            pairlist2[1] = (0, 0, 0)
            CARDS[chosen_row2][chosen_col2] = {list(pair2.keys())[0]: pairlist2}

            

        FIRST_CARD = None
        SECOND_CARD = None

    if check_win():
        pygame.draw.rect(screen, (0,0,0), (0, 100, 400, 200))
        msg = win_fnt.render('YOU WIN', True, (255, 255, 255))
        msg_rect = msg.get_rect()
        msg_rect.center = (200, 200)
        screen.blit(msg, msg_rect)
        pygame.display.update()
        pygame.time.wait(10000*100)


    if timer == 0:
        pygame.draw.rect(screen, (0,0,0), (0, 100, 400, 200))
        msg = win_fnt.render('GAME OVER', True, (255, 255, 255))
        msg_rect = msg.get_rect()
        msg_rect.center = (200, 200)
        screen.blit(msg, msg_rect)
    else: 
        timer -= 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            card = find_card(*pos)
            if (card is not None) and (list(card.values())[0][1] != (0,0,0)):
                if FIRST_CARD == None:
                    FIRST_CARD = card
                    pygame.draw.rect(screen,list(card.values())[0][1], list(card.values())[0][0])
                    pygame.draw.rect(screen, (0,0,0), list(card.values())[0][0], 4)
                elif SECOND_CARD ==  None:
                    SECOND_CARD = card
                    pygame.draw.rect(screen,list(card.values())[0][1], list(card.values())[0][0])
                    pygame.draw.rect(screen, (0,0,0), list(card.values())[0][0], 4)

                    
                    
    
    pygame.display.update()