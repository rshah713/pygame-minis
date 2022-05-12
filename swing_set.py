"""
Rohan Shah
Use advanced math to allow swing seat to follow mouse at a center point

---General Process---
1. Calculate midpoint, distance, and slope (to move line by its centerX)
2. Once we have the centerX, centerY we redraw outwards with the same slope
3. Set the centerX and centerY to mouse and use formula to redraw outwards
"""


import pygame, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption("swing set")
seat_center = [0, 0]
seat_start = (175, 260)
seat_end = (225, 270)

while True:
    screen.fill((0, 191, 255))
    pygame.draw.ellipse(screen, (255, 255, 255), (390-200, 90-75, 400, 150))
    pygame.draw.ellipse(screen, (185, 245, 150), (205-200, 315-75, 400, 150))

    # swing set left / top
    pygame.draw.line(screen, (139, 69, 19), (110, 98), (330, 113), 10)
    pygame.draw.line(screen, (139, 69, 19), (115, 100), (140, 270), 10)
    pygame.draw.line(screen, (139, 69, 19), (115, 100), (65, 320), 10)

    # seat

    """calculate midpoint, distance, slope"""
    """this lets us move the line by the center"""
    """and redraw outwards from centerx, centery"""
    
    dist = ((seat_end[0] - seat_start[0])**2) + ((seat_end[1] - seat_start[1])**2)
    dist = math.sqrt(dist) / 2

    slope = (seat_end[1] - seat_start[1]) / (seat_end[0] - seat_start[0])

    """use slope + midpoint + distance to draw line FROM the center mouse point outwards to each end """
 
    dx = dist / math.sqrt(1 + (slope*slope))
    dy = slope * dx 
    
    new_x = seat_center[0] + dx
    new_y = seat_center[1] + dy
    new_x2 = seat_center[0] - dx
    new_y2 = seat_center[1] - dy

    seat_start = (new_x, new_y)
    seat_end = (new_x2, new_y2)

    pygame.draw.line(screen, (255, 0, 0), seat_start, seat_end, 15)
    
    # ropes
    pygame.draw.line(screen, (0,0,0), (175, 105), seat_end, 2)
    pygame.draw.line(screen, (0,0,0), (225, 110), seat_start, 2)

    # swing right
    pygame.draw.line(screen, (139, 69, 19), (325, 115), (355, 330), 10)
    pygame.draw.line(screen, (139, 69, 19), (325, 115), (290, 365), 10)  
    


    

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEMOTION:
            seat_center = list(pygame.mouse.get_pos())
            
        
    pygame.display.update()