"""
Rohan Shah
Move the phone up and down to find the best service"""

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('cell reception')

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )         


cellPhonePos = [350, 320]
cellPhoneButtonPos = [350, 350]
pos = [500, 500]


while True:
  gradientRect( screen, (50, 205, 50), (255, 0, 0), pygame.Rect( 0,0, 400, 400 ) )
  
  
  # convert cellPhonePos from center coords to top left coords
  cellPhone = pygame.Rect(cellPhonePos[0] - 25, cellPhonePos[1]-40, 50, 80)
  cellPhoneBorder = pygame.Rect(cellPhonePos[0]-25+3, cellPhonePos[1]-40+3, 47, 77)
  
  # align bottom together
  barLow = pygame.Rect(180, 340, 10, 15)
  barMid = pygame.Rect(200, 355-30, 10, 30)
  barHigh = pygame.Rect(220, 355-45, 10, 45)
  
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
    if event.type == MOUSEMOTION:
      pos = pygame.mouse.get_pos()
      cellPhonePos = pos
      cellPhoneButtonPos = [pos[0], pos[1] + 30]
      
      
      
  pygame.draw.rect(screen, (105, 105, 105), cellPhone, 4)
  pygame.draw.rect(screen, (0,0,0), cellPhoneBorder)
  pygame.draw.circle(screen, (105, 105, 105), tuple(cellPhoneButtonPos), 5)
  
  if pos[1] <= 100:
    pygame.draw.rect(screen, (30, 144, 255), barLow)
    pygame.draw.rect(screen, (30, 144, 255), barMid)
    pygame.draw.rect(screen, (30, 144, 255), barHigh)
  elif pos[1] <= 200:
    pygame.draw.rect(screen, (30, 144, 255), barLow)
    pygame.draw.rect(screen, (30, 144, 255), barMid)
  elif pos[1] <= 300:
    pygame.draw.rect(screen, (30, 144, 255), barLow)
    
  pygame.draw.rect(screen, (30, 144, 255), barLow, 2)
  pygame.draw.rect(screen, (30, 144, 255), barMid, 2)
  pygame.draw.rect(screen, (30, 144, 255), barHigh, 2)
  
  pygame.display.update()
  