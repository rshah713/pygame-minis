"""
Rohan Shah

math-based graphical representation of wins v. rebounds
"""

import pygame
from pygame.locals import *

BLACK = (0,0,0)
GHOSTWHITE = (248,248,255)
DARKGREY = (169,169,169)
DARKORANGE = (255,140,0)
MINX = 0
MAXX = 80
MINY = 40
MAXY = 50
DATA = {
    'Milwaukee Bucks': [60, 49.73170731707317],
    'Golden State Warriors': [57, 46.18292682926829],
    'Toronto Raptors': [58, 45.19512195121951],
    'Utah Jazz': [50, 46.353658536585364],
    'Houston Rockets': [53, 42.0609756097561],
    'Boston Celtics': [49, 44.548780487804876],
    'Portland Trail Blazers': [53, 47.98780487804878],
    'Denver Nuggets': [54, 46.390243902439025],
    'Indiana Pacers': [48, 43.02439024390244],
    'Oklahoma City Thunder': [49, 48.073170731707314],
    'Philadelphia 76ers': [51, 47.76829268292683],
    'San Antonio Spurs': [48, 44.71951219512195],
    'Los Angeles Clippers': [48, 45.51219512195122],
    'Orlando Magic': [42, 45.41463414634146],
    'Brooklyn Nets': [42, 46.573170731707314],
    'Detroit Pistons': [41, 44.97560975609756],
    'Miami Heat': [39, 46.34146341463415],
    'Sacramento Kings': [39, 45.426829268292686],
    'Charlotte Hornets': [39, 43.80487804878049],
    'New Orleans Pelicans': [33, 47.292682926829265],
    'Dallas Mavericks': [33, 45.31707317073171],
    'Minnesota Timberwolves': [36, 44.792682926829265],
    'Los Angeles Lakers': [37, 46.58536585365854],
    'Memphis Grizzlies': [33, 41.78048780487805],
    'Washington Wizards': [32, 42.353658536585364],
    'Atlanta Hawks': [29, 46.09756097560975],
    'Chicago Bulls': [22, 42.890243902439025],
    'New York Knicks': [17, 44.73170731707317],
    'Phoenix Suns': [19, 40.3780487804878],
    'Cleveland Cavaliers': [19, 42.65853658536585]
}

def draw_axes():
    msg = font.render('Wins/Rebound Per Team in the 2018-2019 NBA season', True, GHOSTWHITE)
    msg_r = msg.get_rect()
    msg_r.center = (200, 25)
    screen.blit(msg, msg_r)

    msg = axis_fnt.render('Rebounds Per Game', True, GHOSTWHITE)
    msg_r = msg.get_rect()
    msg_r.center = (95, 55)
    screen.blit(msg, msg_r)

    msg = axis_fnt.render('Wins', True, GHOSTWHITE)
    msg_r = msg.get_rect()
    msg_r.center = (350, 345)
    screen.blit(msg, msg_r)

    pygame.draw.line(screen, DARKGREY, (70, 65), (70, 365), 3)
    pygame.draw.line(screen, DARKGREY, (70, 360), (340, 360), 3)
    # tiny ticks lol
    for i in range(11):
        cx = 70 + i * 270 / 10
        val = int(MINX + i * (MAXX - MINX) / 10)
        pygame.draw.line(screen, DARKGREY, (cx, 357), (cx, 363))

        msg = axis_fnt.render(str(val), True, GHOSTWHITE)
        msg_r = msg.get_rect()
        msg_r.center = (cx, 375)
        screen.blit(msg, msg_r)

    for i in range(11):
        cy = 350 - i * 270 / 10
        val = int(MINY + i * (MAXY - MINY) / 10)
        pygame.draw.line(screen, DARKGREY, (67, cy), (73, cy))

        msg = axis_fnt.render(str(val), True, GHOSTWHITE)
        msg_r = msg.get_rect()
        msg_r.midright = (60, cy)
        screen.blit(msg, msg_r)

def draw_basketball(x, y):
    """AHHH IM GOING CRAXY
    HOW TF DO I SCALE ELLIPSES AND CIRCLES BY 1.5 W:H RATIO
    AND THEN APPLY IT TO LINES 
    BRUHHH WHY CANT I JUST COPY THIS CODE FROM ONLINE 
    
    coding lame af plz this scaling thing should not take so long"""


    
    """
    aight nvm i took a break and its actually rlly ez
    just subtract centerx/y by applied W:H ratio + treat ellipse like bounding rect and just shove it around the screen
    """
    pygame.draw.ellipse(screen, DARKORANGE, (x-18/2, y-18/2,
                                             18, 18))
    pygame.draw.ellipse(screen, BLACK, (x-3-6, y-15//2, 6, 15), 1)
    
    pygame.draw.ellipse(screen, BLACK, (x-3+6, y-15//2, 6, 15), 1)

    pygame.draw.line(screen, BLACK, (x, y-9), (x, y+9), 1)
    pygame.draw.line(screen, BLACK, (x-9, y), (x+9, y), 1)

def draw_scatterplot():
        # For each team in the data, draw a basketball positioned so that the
    # x-coordinate relates to the number of wins the team had, and the y-coordinate
    # relates to the number of rebounds the team averaged per game.
    for team in DATA:
        wins, rebounds = DATA[team]
        x = 70 + 270 * (wins - MINX) / (MAXX - MINX)
        y = 350 - 270 * (rebounds - MINY) / (MAXY - MINY)
        draw_basketball(x, y)
        
pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
font = pygame.font.Font('freesansbold.ttf', 15)
axis_fnt = pygame.font.Font('freesansbold.ttf', 13)
pygame.display.set_caption('NBA Rebounding data')



screen.fill((75, 100, 130))
pygame.draw.rect(screen, (30, 45, 60), (20, 40, 360, 345))

draw_scatterplot()
draw_axes()

while True:
    pygame.display.update()