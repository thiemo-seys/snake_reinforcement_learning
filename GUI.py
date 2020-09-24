from snake import *

import pygame

screen_height, screen_width = 960, 960


pygame.init()

myfont = pygame.font.SysFont('Arial', 12)
dis = pygame.display.set_mode((screen_width, screen_height))
pygame.display.update()
pygame.display.set_caption('PYSNEK')

# all colors
###########################################################################
white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
###########################################################################

bord = Board()
bord.display_board()
bord.placeSnakeHead((4,4))
print('after snek placement')
bord.display_board()