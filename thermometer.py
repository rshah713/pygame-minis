"""
Rohan Shah
Click around to notice how the temperature changes
"""

import pygame
from _dashes import draw_dashed_line

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('thermometer')
font = pygame.font.Font('freesansbold.ttf', 12)
disp_font = pygame.font.Font('freesansbold.ttf', 20)
temp_font = pygame.font.Font('freesansbold.ttf', 60)

temp = 120.0
meter_y2 = 90
background = (250, 128, 114) # salmon
while True:
    screen.fill(background)
   
    # thermometer
    pygame.draw.rect(screen, (220, 220, 220), (50, 90, 100, 250))
    pygame.draw.circle(screen, (220, 220, 220), (100, 90), 50)
    pygame.draw.circle(screen, (220, 220, 220), (70, 340), 20)
    pygame.draw.circle(screen, (220, 220, 220), (130, 340),20)
    pygame.draw.rect(screen, (220, 220, 220), (70, 340, 60, 20))

    pygame.draw.circle(screen, (255, 255, 255), (100, 320),20)
    pygame.draw.rect(screen, (255, 255, 255), (90, 75, 20, 250))
    pygame.draw.circle(screen, (255, 255, 255), (100, 75), 10)
    pygame.draw.circle(screen, (250, 128, 114), (100, 320), 13)

    # number labels and markings down the side
    draw_dashed_line(screen, (0, 0, 0), (78, 300), (78, 80), width=1, dash_length =5)
    draw_dashed_line(screen, (0, 0, 0), (120, 300), (120, 80), width=1, dash_length =3)

    message_text = font.render('F', True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (120, 70)
    screen.blit(message_text, message_rect)

    message_text = font.render('20', True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (135, 290)
    screen.blit(message_text, message_rect)

    message_text = font.render('40', True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (135, 250)
    screen.blit(message_text, message_rect)

    message_text = font.render('60', True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (135, 210)
    screen.blit(message_text, message_rect)

    message_text = font.render('80', True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (135, 170)
    screen.blit(message_text, message_rect)

    message_text = font.render('100', True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (135, 130)
    screen.blit(message_text, message_rect)

    message_text = font.render('120', True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (135, 90)
    screen.blit(message_text, message_rect)

    # display
    message_text = disp_font.render("° Fahrenheit", True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (275, 250)
    screen.blit(message_text, message_rect)

    message_text = temp_font.render(str(temp), True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (280, 180)
    screen.blit(message_text, message_rect)

    pygame.draw.line(screen,(250, 128, 114), (100, 320), (100, meter_y2), 5 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # First, adjust the meter length and display number depending on mouseY.
            meter_y2 = pos[1] / 2 + 90
            temp = (400 - pos[1]) / 4 + 20
            
            # Then, change the background according to the mouseY.
            if pos[1] <= 400:
                background = (65, 105, 225) # royal blue
            if pos[1] <= 350:
                background = (135, 206, 250) # light sky blue
            if pos[1] <= 300:
                background = (224, 255, 255) # light cyan
            if pos[1] <= 250:
                background = (240, 255, 240) # honeydew
            if pos[1] <= 200:
                background = (154, 205, 50) # yellow green
            if pos[1] <= 150:
                background = (255, 228, 181) # khaki
            if pos[1] <= 100:
                background = (255, 215, 0) # gold
            if pos[1] <= 50:
                background = (250, 128, 114) # salmon
            
    pygame.display.update()
    