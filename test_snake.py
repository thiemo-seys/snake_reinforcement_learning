import time

import pygame

from snake import *

screen_res = (1000, 1000)

pygame.init()

FONT = pygame.font.SysFont('Arial', 12)
display = pygame.display.set_mode(screen_res)
pygame.display.update()
pygame.display.set_caption('Pysnek')

# all colors
###########################################################################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def draw_board(board, display):
    rect_list = []
    square_width = screen_res[0] / bord.width
    square_height = screen_res[1] / bord.height

    types_list = []

    for x in range(0, board.height):
        for y in range(0, board.width):
            # drawing according to x, y, width, height
            square_object = bord.board[x][y].square_object
            types_list.append(square_object)
            if square_object is None:
                rect = pygame.draw.rect(display, BLACK,
                                        [x * square_width, y * square_height, square_width, square_height])
            elif isinstance(square_object, Food):
                rect = pygame.draw.rect(display, BLUE,
                                        [x * square_width, y * square_height, square_width, square_height])

            elif isinstance(square_object, Cube):
                if square_object == bord.snake.body[0]:
                    rect = pygame.draw.rect(display, RED,
                                            [x * square_width, y * square_height, square_width, square_height])

                elif square_object == bord.snake.body[-1]:
                    rect = pygame.draw.rect(display, GREEN,
                                            [x * square_width, y * square_height, square_width, square_height])


                else:
                    rect = pygame.draw.rect(display, WHITE,
                                            [x * square_width, y * square_height, square_width, square_height])


clock = pygame.time.Clock()
frames = 0
game_over = False

bord = Board(30, 30)
start_time = time.time()
while not game_over:
    clock.tick(60)
    if frames % 5 == 0:
        bord.move_snake()
    if frames % 300 == 0:
        bord.placeFood()
        print(bord.score)
        print(bord.food_coordinates)

    pygame.display.flip()
    frames += 1
    draw_board(bord, display)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('spacebar pressed, starting game')

            if event.key == pygame.K_UP:
                print(f'snake changed movement to up')
                bord.turn_snake('up')

            if event.key == pygame.K_DOWN:
                print(f'snake changed movement to down')
                bord.turn_snake('down')

            if event.key == pygame.K_RIGHT:
                print(f'snake changed movement to right')
                bord.turn_snake('right')

            if event.key == pygame.K_LEFT:
                print(f'snake changed movement to left')
                bord.turn_snake('left')

stop_time = time.time()
print(f'quiting program, ran for {frames} frames and {stop_time - start_time} seconds which is {frames / (stop_time - start_time)} fps')
pygame.quit()
