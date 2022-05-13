"""
Rohan Shah
Click anywhere to add food to the plate
Enough food will make the cat happy
Cat's eyes will follow as mouse moves
"""


import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
font = pygame.font.Font('freesansbold.ttf', 25)

print("DIRECTIONS:")
print("Click to feed cat")
print('eyes follow the food')

foodPileWidth = 10
foodPileHeight = 5
foodX = 200
foodY = 30
tearsVisible = True
leftEyeX = 165
leftEyeY = 185
rightEyeX = 235
rightEyeY = 185
messageValue = 'pleeeease'

while True:
    screen.fill((170, 185, 55))
    pygame.draw.circle(screen, (255, 255, 255), (200, 200), 150)

    # ears
    pygame.draw.polygon(screen, (53, 31, 22), ((261, 158), (305, 132), (280, 195)))
    pygame.draw.polygon(screen, (145, 170, 110), ((290, 147), (280, 178), (270, 158)))

    pygame.draw.polygon(screen, (53, 31, 22), ((139, 158), (95, 132), (120, 195)))
    pygame.draw.polygon(screen, (145, 170, 110), ((108, 147), (128, 157), (120, 177)))

    pygame.draw.polygon(screen, (55, 30, 20), ((227, 129), (305, 133), (264, 160)))
    pygame.draw.polygon(screen, (0,0,0), ((285, 140), (265, 153), (250, 137)))

    pygame.draw.polygon(screen, (55, 30, 20), ((173, 129), (95, 133), (136, 160)))
    pygame.draw.polygon(screen, (0,0,0), ((115, 140), (138, 153), (150, 137)))

    # face and body
    pygame.draw.ellipse(screen, (55, 30, 20), (200-60, 276-65, 120, 130))
    """
    FORMULA FOR ELLIPSE BORDERS
    CENTERX + BORDERWIDTH - SIZEX/2
    CENTERY + BORDERWIDTH - SIZEY/2
    SIZEX - BORDERWIDTH *2
    SIZEY - BORDERWIDTH *2"""
    pygame.draw.ellipse(screen, (0,0,0), (206-60, 282-65, 120-12, 130-12))

    pygame.draw.circle(screen, (55, 30, 20), (200, 200), 80)
    pygame.draw.circle(screen, (0,0,0), (200, 200), 80-8)

    # plate 245, 245, 220)
    pygame.draw.ellipse(screen, (55, 30, 20), (200-70, 323-45//2, 140, 45))
    pygame.draw.ellipse(screen, (245, 245, 220),(203-70, 326-45//2, 140 - 6, 45-6))

    pygame.draw.ellipse(screen, (55, 30, 20), (200 - 100, 312 - 25, 200, 50))
    pygame.draw.ellipse(screen, (255, 255, 255), (204 - 100, 316 - 25, 200 - 8, 50 - 8))

    pygame.draw.ellipse(screen, (170, 185, 55), (200 -  150//2, 317 - 15, 150, 30), 3)

    # hands
    pygame.draw.ellipse(screen, (55, 30, 20), (165-15, 285-35//2, 30, 35))
    pygame.draw.ellipse(screen, (0,0,0), (170-15, 290-35//2, 30 - 10, 35 - 10))

    pygame.draw.ellipse(screen, (55, 30, 20), (235-15, 285-35//2, 30, 35))
    pygame.draw.ellipse(screen, (0,0,0), (240-15, 290-35//2, 30-10, 35-10))

    # eyes and tears
    pygame.draw.ellipse(screen, (245, 245, 220), (163-75//2, 193-50, 75, 100))
    pygame.draw.ellipse(screen, (245, 245, 220), (237-75//2, 193-50, 75, 100))

    pygame.draw.ellipse(screen, (55, 30, 20), (leftEyeX-45//2, leftEyeY-55//2, 45, 55))
    pygame.draw.ellipse(screen, (0,0,0), ((leftEyeX+4) - 45//2, (leftEyeY+4) - 55//2, 45-8, 55-8))

    pygame.draw.ellipse(screen, (55, 30, 20), (rightEyeX-45//2, rightEyeY-55//2, 45, 55))
    pygame.draw.ellipse(screen, (0,0,0), ((rightEyeX+4) - 45//2, (rightEyeY+4) - 55//2, 45-8, 55-8))

    if tearsVisible: # 224, 255, 255
        pygame.draw.ellipse(screen, (85, 130, 125), (150-25//2, 240-15//2, 25, 15))
        pygame.draw.ellipse(screen, (224, 255, 255), (152-25//2, 242 - 15//2, 25-4, 15-4))

        pygame.draw.ellipse(screen, (85, 130, 125), (250-25//2, 240-15//2, 25, 15))
        pygame.draw.ellipse(screen, (224, 255, 255), (252-25//2, 242 - 15//2, 25-4, 15-4))
        


    # message
    message_text = font.render(messageValue, True, (170, 185, 55))
    message_rect = message_text.get_rect()
    message_rect.center = (200, 90)
    screen.blit(message_text, message_rect)

    # food
    pygame.draw.ellipse(screen, (255, 160, 122), (210-foodPileWidth//2, 315-foodPileHeight//2, foodPileWidth, foodPileHeight))
    pygame.draw.circle(screen, (0,0,0), (foodX, foodY), 10)
    pygame.draw.circle(screen,(255, 160, 122), (foodX, foodY), 6)
        

    
    

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if foodPileHeight < 30:
                foodPileWidth += 5
                foodPileHeight += 2
                
                
            if foodPileHeight >= 30:
                messageValue = 'meow'
                tearsVisible = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            foodX = pos[0]
            foodY = pos[1]

            # represents CENTER of shape
            leftEyeX = 155 + (pos[0] / 20)
            leftEyeY = 180 + (pos[1] / 20)
            rightEyeX = 225 + (pos[0] / 20)
            rightEyeY = 180 + (pos[1] / 20)

            
    pygame.display.update()