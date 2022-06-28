'''
Rohan Shah

WASD to move blue, arrows to move purple
stay in the track and get to the finish
leaving the track makes opponent win
'r' restarts game '''


import pygame
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('dot race')
font = pygame.font.Font('freesansbold.ttf', 25)
clock = pygame.time.Clock()

WHITE = (255,255,255)
PALEGREEN = (152,251,152)
RED = (255,0,0)
DARKORCHID = (153,50,204)
DODGERBLUE = (30,144,255)

track = pygame.Rect(200-360//2, 200-360//2, 360, 360)
inner_grass = pygame.Rect(200-260//2, 200-260//2, 260, 260)
finish = pygame.Rect(320, 180, 80, 30)
purple = [45, 175]
blue = [45, 225]
message = 'Dot Race!'

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

while True:
    screen.fill(PALEGREEN)
    pygame.draw.rect(screen, (0,0,0), track)
    pygame.draw.rect(screen, PALEGREEN, inner_grass)
    draw_dashed_line(screen, WHITE, (200-310//2, 200-310//2), (200+310//2, 200-310//2))
    draw_dashed_line(screen, WHITE, (200-310//2, 200-310//2), (200-310//2, 200+310//2))
    draw_dashed_line(screen, WHITE, (200-310//2, 200+310//2), (200+310//2, 200+310//2))
    draw_dashed_line(screen, WHITE, (200+310//2,200-310//2),(200+310//2, 205+310//2) )

    msg = font.render(message, True, (0, 0, 0))
    msg_r = msg.get_rect()
    msg_r.center = (200, 200)
    screen.blit(msg, msg_r)

    draw_dashed_line(screen, WHITE, (320, 200), (400, 200), width=30)
    draw_dashed_line(screen, RED, (330, 200), (390, 200), width=30)

    pygame.draw.circle(screen, DARKORCHID, tuple(purple), 15)
    pygame.draw.circle(screen, DODGERBLUE, tuple(blue), 15)
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                purple = [45, 175]
                blue = [45, 225]
                message = 'Dot Race!'

    keys = pygame.key.get_pressed()
    if message == 'Dot Race!':
        if keys[K_UP]:
            purple[1] -= 10
        if keys[K_DOWN]:
            purple[1] += 10
        if keys[K_LEFT]:
            purple[0] -= 10
        if keys[K_RIGHT]:
            purple[0] += 10
        if keys[K_w]:
            blue[1] -= 10
        if keys[K_s]:
            blue[1] += 10
        if keys[K_a]:
            blue[0] -= 10
        if keys[K_d]:
            blue[0] += 10
    

    # Check if one of the dots wins and if so change the value of the message.
        # A dot wins if either it touches the finish line or the center of the
        # other dot is not on the track.
        if not(track.collidepoint(*purple)) or inner_grass.collidepoint(*purple):
            message = 'Blue dot won!'
        elif not(track.collidepoint(*blue)) or inner_grass.collidepoint(*blue):
            message = 'Purple dot won!'
        elif finish.collidepoint(*purple):
            message = 'Purple dot won!'
        elif finish.collidepoint(*blue):
            message = 'Blue dot won!'


        
    clock.tick(30)
    pygame.display.update()