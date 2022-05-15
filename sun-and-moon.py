"""
Rohan Shah
Mouseclick to draw sun -- moon will follow """

import pygame


SIENNA = (160, 82, 45)
FORESTGREEN = (34, 139, 34)
SADDLEBROWN = (139, 69, 19)
LIGHTSKYBLUE = (135, 206, 250)
GOLD = (255, 215, 0)
LIGHTGRAY = (211, 211, 211)

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption("Sun and Moon")

#skies
screen.fill(LIGHTSKYBLUE)
pygame.draw.rect(screen, (0, 0, 0), (0, 200, 400, 200))

#top trees
pygame.draw.rect(screen, SIENNA,  (305, 190, 5, 10))
pygame.draw.polygon(screen, FORESTGREEN, ((300, 190), (315, 190),( 307, 160)))

pygame.draw.rect(screen, SIENNA,  (335, 190, 5, 10))
pygame.draw.polygon(screen, FORESTGREEN, ((330, 190),( 345, 190), (337, 140)))

# bottom trees
pygame.draw.polygon(screen, SADDLEBROWN, ((305, 200), (310, 200), (307, 250)))
pygame.draw.line(screen, SADDLEBROWN, (305, 210), (300, 215), 3)
pygame.draw.line(screen, SADDLEBROWN, (308, 215), (315, 220), 3)

pygame.draw.polygon(screen, SADDLEBROWN, ((335, 200), (340, 200), (337, 270)))
pygame.draw.line(screen, SADDLEBROWN, (338, 215), (345, 220), 3)
pygame.draw.line(screen, SADDLEBROWN, (335, 225), (330, 230), 3)
pygame.draw.line(screen, SADDLEBROWN, (338, 235), (345, 240), 3)

# sun/moon
sunX = 100
sunY = 100
moonX = 100
moonY = 300
pygame.draw.circle(screen, GOLD, (sunX, sunY), 20)
pygame.draw.circle(screen, LIGHTGRAY, (moonX, moonY), 20)

while True:
    #skies
    screen.fill(LIGHTSKYBLUE)
    pygame.draw.rect(screen, (0, 0, 0), (0, 200, 400, 200))
    
    #top trees
    pygame.draw.rect(screen, SIENNA,  (305, 190, 5, 10))
    pygame.draw.polygon(screen, FORESTGREEN, ((300, 190), (315, 190),( 307, 160)))
    
    pygame.draw.rect(screen, SIENNA,  (335, 190, 5, 10))
    pygame.draw.polygon(screen, FORESTGREEN, ((330, 190),( 345, 190), (337, 140)))
    
    # bottom trees
    pygame.draw.polygon(screen, SADDLEBROWN, ((305, 200), (310, 200), (307, 250)))
    pygame.draw.line(screen, SADDLEBROWN, (305, 210), (300, 215), 3)
    pygame.draw.line(screen, SADDLEBROWN, (308, 215), (315, 220), 3)
    
    pygame.draw.polygon(screen, SADDLEBROWN, ((335, 200), (340, 200), (337, 270)))
    pygame.draw.line(screen, SADDLEBROWN, (338, 215), (345, 220), 3)
    pygame.draw.line(screen, SADDLEBROWN, (335, 225), (330, 230), 3)
    pygame.draw.line(screen, SADDLEBROWN, (338, 235), (345, 240), 3)

    pygame.draw.circle(screen, GOLD, (sunX, sunY), 20)
    pygame.draw.circle(screen, LIGHTGRAY, (moonX, moonY), 20)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] < 180:
                sunX = pos[0]
                sunY = pos[1]
                moonX = pos[0]
                moonY = 400 - pos[1]
                
                

    pygame.display.update()