'''
Rohan Shah

the coolest thing ive prolly ever coded
besides the barriers game

if puck gets stuck press 'r' to reset it
'''

import pygame, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('air hockey?!?!?!')
font = pygame.font.Font('freesansbold.ttf', 30)
clock = pygame.time.Clock()
FPS = 30

WHITE = (255, 255, 255)
FIREBRICK = (178,34,34)
CORNFLOWERBLUE = (100,149,237)
AZURE = (240,255,255)
MIDNIGHTBLUE = (25,25,112)
GREY = (128,128,128)
ROYALBLUE = (65,105,225)
SNOW = (255,250,250)
CRIMSON = (220,20,60)

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

# score for players
scoreR = 0
scoreB = 0

r_score = font.render(str(scoreR), True, FIREBRICK)
r_score_rect = r_score.get_rect()
r_score_rect.center = (375, 40)
b_score = font.render(str(scoreB), True, ROYALBLUE)
b_score_rect = b_score.get_rect()
b_score_rect.center = (25, 360)


player = [200, 365]
goalie = [200, 35]

def reset_puck():
    global puck, puck_dx, puck_dy, puck_numhits
    puck = [200, 200]
    puck_dx = 3
    puck_dy = 3
    puck_numhits = 0

def hit_puck(paddle):
    global puck_dx, puck_dy, puck_numhits
    # Deflect the puck differently based on if it hits on the left, middle,/ right
    # return math.sqrt((puck[0]-paddle[0])**2+(puck[1]-paddle[1])**2)<=12+10
    if puck[0] - paddle[0] >= 4:
        puck_dx = 3 + puck_numhits
    elif paddle[0] - puck[0] >= 4:
        puck_dx = -3 - puck_numhits
    else:
        puck_dx = 0


    if (puck[1] - paddle[1] >= 6):
        puck_dy = 3 + puck_numhits
    elif (paddle[1] - puck[1] >= 6):
        puck_dy = -3 - puck_numhits

    if (puck_numhits <= 10):
        puck_numhits += 1

    
reset_puck()
while True:
    screen.fill(WHITE)

    # board and lines
    b = pygame.Rect(200, 200, 295, 375)
    b.center = (200, 200)
    pygame.draw.rect(screen, (55, 75, 120), b)
    pygame.draw.circle(screen, FIREBRICK, (200, 10), 40, 3)
    pygame.draw.circle(screen, CORNFLOWERBLUE, (200, 390), 40, 3)
    b = pygame.Rect(0, 0, 90, 10)
    b.center = (200, 5)
    pygame.draw.rect(screen, WHITE, b)
    b = pygame.Rect(0, 0, 90, 10)
    b.center = (200, 395)
    pygame.draw.rect(screen, WHITE, b)
    pygame.draw.line(screen, FIREBRICK, (50, 85), (350, 85))
    pygame.draw.line(screen, CORNFLOWERBLUE, (50, 305), (350, 305))
    draw_dashed_line(screen, AZURE, (50, 200), (350, 200))
    pygame.draw.circle(screen, (55, 75, 120), (200, 200), 25)
    pygame.draw.circle(screen, AZURE, (200, 200), 25, 2)
    pygame.draw.circle(screen, AZURE, (200, 200), 3)


    # border
    pygame.draw.circle(screen, MIDNIGHTBLUE, (60, 20), 10, 5)
    pygame.draw.circle(screen, MIDNIGHTBLUE, (340, 20), 10, 5)
    pygame.draw.circle(screen, MIDNIGHTBLUE, (60, 380), 10, 5)
    pygame.draw.circle(screen, MIDNIGHTBLUE, (340, 380), 10, 5)
    pygame.draw.circle(screen, (55, 75, 120), (65, 25), 13)
    pygame.draw.circle(screen, (55, 75, 120), (335, 25), 13)
    pygame.draw.circle(screen, (55, 75, 120), (65, 375), 13)
    pygame.draw.circle(screen, (55, 75, 120), (335, 375), 13)
    pygame.draw.line(screen, MIDNIGHTBLUE, (60, 10), (340, 10), 5)
    pygame.draw.line(screen, MIDNIGHTBLUE, (50, 20), (50, 380), 5)
    pygame.draw.line(screen, MIDNIGHTBLUE, (350, 20), (350, 380), 5)
    pygame.draw.line(screen, MIDNIGHTBLUE, (60, 390), (340, 390), 5)


    # scores
    pygame.draw.rect(screen, WHITE, r_score_rect)
    r_score = font.render(str(scoreR), True, FIREBRICK)
    r_score_rect = r_score.get_rect()
    r_score_rect.center = (375, 40)
    screen.blit(r_score, r_score_rect)

    pygame.draw.rect(screen, WHITE, b_score_rect)
    b_score = font.render(str(scoreB), True, ROYALBLUE)
    b_score_rect = b_score.get_rect()
    b_score_rect.center = (25, 360)
    screen.blit(b_score, b_score_rect)

    # hockey puck
    pygame.draw.circle(screen, SNOW, tuple(puck), 10)
    pygame.draw.circle(screen, GREY, tuple(puck), 10, 2)

    #player/goalie
    pygame.draw.circle(screen, ROYALBLUE, tuple(player), 12)
    pygame.draw.circle(screen, CORNFLOWERBLUE, tuple(player), 8)
    pygame.draw.circle(screen, FIREBRICK, tuple(goalie), 12)
    pygame.draw.circle(screen, CRIMSON, tuple(goalie), 8)

    puck[0] += puck_dx
    puck[1] += puck_dy

     # If there is a goal, increment the score and reset the puck.
    if ((puck[0] >= 165) and (puck[0] <= 235) and
        ((puck[1] <= 20) or (puck[1] >= 380))):
        if (puck[1] <= 20):
            scoreB += 1
        elif (puck[1] >= 380):
            scoreR += 1

        reset_puck()

    # Bounce the puck if necessary.
    if ((puck[0] <= 60) or (puck[0] >= 340)):
        puck_dx *= -1
    if ((puck[1] <= 20) or (puck[1] >= 380)):
        puck_dy *= -1

    # Move the goalie.
    if (puck[0] - goalie[0] < 0):
        goalie[0] -= 5
    elif (puck[0] - goalie[0] > 0):
        goalie[0] += 5
    if (goalie[0] < 135):
        goalie[0] = 135
    elif (goalie[0] > 265):
        goalie[0] = 265

    if math.sqrt((puck[0]-player[0])**2+(puck[1]-player[1])**2)<=12+10:
        hit_puck(player)
    if math.sqrt((puck[0]-goalie[0])**2+(puck[1]-goalie[1])**2)<=12+10:
        hit_puck(goalie)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if ((pos[0] >= 60) and (pos[0] <= 340) and (pos[1] > 200)):
                player[0] = pos[0]
                player[1] = pos[1]
        if event.type == KEYDOWN:
            if event.key == K_r:
                reset_puck()

    clock.tick(FPS)
    pygame.display.update()