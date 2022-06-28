"""
keep in mind i have 0 idea how to make aesthetic colors

but woah an app in python !!!
"""

import pygame
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('color palette app')
font = pygame.font.Font('freesansbold.ttf', 18)
rgb_fnt = pygame.font.Font('freesansbold.ttf', 15)

selected = None
drag = False

red_slider_fill = (125, 0, 0)
green_slider_fill = (0, 125, 0)
blue_slider_fill = (0, 0, 125)

red_slider = [200, 35]
green_slider = [200, 85]
blue_slider = [200, 135]

c1_fill = (125, 125, 125)
c2_fill = (125, 125, 125)
c3_fill = (125, 125, 125)

c1_label = ''
c2_label = ''
c3_label = ''


def hit_test(circle_list, x, y):
    """
    Takes in point (x, y) and returns the shapes in the group that point (x, y) hits. If it hits nothing from the group, it returns None. If there are multiple shapes that it might hit, it returns the top shape.
"""
    for circle in circle_list:
        # circle: [x, y]
        if math.sqrt((circle[0]-x)**2+(circle[1]-y)**2)<=15:
            return circle
    return None

def map_value(value, value_min, value_max, target_min, target_max):
    ratio = (value - value_min) / (value_max - target_min)
    return ratio * (target_max-target_min) + target_min

def get_triad_colors(color):
    color1 = (color[1], color[2], color[0])
    color2 = (color[2], color[0], color[1])
    return color1, color2

def update_label(color):
    return 'rgb(' + str(color[0]) + ', ' + str(color[1]) + ', ' +str( color[2]) + ')'

def update_fills():
    global red_slider_fill, green_slider_fill, blue_slider_fill
    global c1_fill, c2_fill, c3_fill
    global c1_label, c2_label, c3_label
    red = int(map_value(red_slider[0], 45, 345, 0, 255))
    green = int(map_value(green_slider[0], 45, 345, 0, 255))
    blue = int(map_value(blue_slider[0], 45, 345, 0, 255))

    red_slider_fill = (red, 0, 0)
    green_slider_fill = (0, green, 0)
    blue_slider_fill = (0, 0, blue)

    c1_fill = (red, green, blue)
    c2_fill, c3_fill = get_triad_colors((red, green, blue))

    c1_label = update_label(c1_fill)
    c2_label = update_label(c2_fill)
    c3_label = update_label(c3_fill)
    
    

    
c1_label = update_label(c1_fill)
c2_label = update_label(c2_fill)
c3_label = update_label(c3_fill)
while True:
    screen.fill((230, 230, 230))
    

    for i in range(3):
        y = 35 + i * 50
        msg = font.render("0", (0, 0, 0), True)
        msg_r = msg.get_rect()
        msg_r.center = (20, y)
        screen.blit(msg, msg_r)

        msg = font.render("255", (0, 0, 0), True)
        msg_r = msg.get_rect()
        msg_r.center = (380, y)
        screen.blit(msg, msg_r)

        pygame.draw.rect(screen, (225, 225, 240), (45, y - 16, 300, 32))
        pygame.draw.rect(screen, (0,0,0), (45, y - 16, 300, 32), 1)
        pygame.draw.circle(screen, (225, 225, 240), (45, y), 16)
        pygame.draw.circle(screen, (0,0,0), (45, y), 16, 1)
        pygame.draw.circle(screen, (225, 225, 240), (345, y), 16)
        pygame.draw.circle(screen, (0,0,0), (345, y), 16, 1)
        pygame.draw.rect(screen, (225, 225, 240), (45, y - 15, 300, 30))

    pygame.draw.circle(screen, red_slider_fill, tuple(red_slider), 15)
    pygame.draw.circle(screen, green_slider_fill, tuple(green_slider), 15)
    pygame.draw.circle(screen, blue_slider_fill, tuple(blue_slider), 15)

    msg = rgb_fnt.render(c1_label, (0, 0, 0), True)
    msg_r = msg.get_rect()
    msg_r.center = (200, 320)
    screen.blit(msg, msg_r)

    msg = rgb_fnt.render(c2_label, (0, 0, 0), True)
    msg_r = msg.get_rect()
    msg_r.center = (65, 375)
    screen.blit(msg, msg_r)

    msg = rgb_fnt.render(c3_label, (0, 0, 0), True)
    msg_r = msg.get_rect()
    msg_r.center = (335, 375)
    screen.blit(msg, msg_r)

    pygame.draw.circle(screen, c1_fill, (200, 240), 70)
    pygame.draw.circle(screen, (0, 0, 0), (200, 240), 70, 2)
    pygame.draw.circle(screen, c2_fill, (65, 315), 45)
    pygame.draw.circle(screen, (0, 0, 0), (65, 315), 45, 1)
    pygame.draw.circle(screen, c3_fill, (335, 315), 45)
    pygame.draw.circle(screen, (0, 0, 0), (335, 315), 45, 1)

 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            drag = True
        if event.type == MOUSEBUTTONUP:
            drag = False
        if event.type == MOUSEMOTION:
            if drag:
                pos = pygame.mouse.get_pos()
                selected = hit_test((red_slider, blue_slider, green_slider), pos[0], pos[1])
                if selected is not None:
                    if selected == red_slider:
                        red_slider[0] = pos[0]
                        left = red_slider[0] - 15
                        right = red_slider[0] + 15
                        if left < 30:
                            red_slider[0] = 45
                        elif right > 360:
                            red_slider[0] = 345
                    elif selected == blue_slider:
                        blue_slider[0] = pos[0]
                        right = blue_slider[0] + 15
                        left = blue_slider[0] - 15
                        if left < 30:
                            blue_slider[0] = 45
                        elif right > 360:
                            blue_slider[0] = 345
                    else:
                        green_slider[0] = pos[0]
                        left = green_slider[0] - 15
                        right = green_slider[0] + 15
                        if left < 30:
                            green_slider[0] = 45
                        elif right > 360:
                            green_slider[0] = 345

                update_fills()
                        
            
    pygame.display.update()