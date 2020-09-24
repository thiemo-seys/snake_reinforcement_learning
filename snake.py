import random
import math


class Board():
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = [[Square(x=x, y=y) for x in range(self.width)] for y in range(self.height)]

    #TODO: this method needs to be split up in methods that each place a different object on the board
    def update_cell_object(self, x, y, new_object):
        self.board[x][y] = new_object

    def placeSnakeHead(self, start_pos):
        self.board[start_pos[0]][start_pos[1]] = Snake(start_pos)

    def placeFood(self, start_pos=None):
        #no specific position was specified, so putting food in a random free place
        if start_pos is None:
           x,y = random.randint(0, self.width)
           y = random.randint(0, self.height)

    #check which squares contains a square object with value 1
    def get_free_squares(self):
        free_squares_list = []
        for y, row in enumerate(self.board):
            for x, square in enumerate(row):
                if type(square) == 'Square' and :



    def reset_board(self):
        self.board = [[Square(x=x, y=y) for x in range(self.width)] for y in range(self.height)]

    def display_board(self):
        for row in self.board:
            print(row)

    #maybe override this method for pretty printing?
    #but seems weird to print it pretty because return breaks the function
    #def __str__(self):
    #    pass



class Square():
    def __init__(self, x, y, object = 0):
        self.x = x
        self.y = y
        self.object = object

    def __str__(self):
        return str(self.object)

#############################################################################################################################################
class Snake():
    def __init__(self, start_pos, dirx=1, diry=0, color=(255,0,0)):
        self.head = Cube(start_pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.pos = start_pos
        self.dirx = dirx
        self.diry = diry
        self.move = ''
        self.color = color

    def add_cube(self):
        pass

    def change_direction(self, move):
        possible_moves = {'up': [0,1], 'down': [0,-1], 'right': [1,0] , 'left': [-1,0] }
        opposite_moves = {'up': 'down', 'down': 'up', 'right': 'left', 'left': 'right'}

        if move in possible_moves:
            if  move != opposite_moves[self.move]:
                self.dirx = possible_moves[move][0]
                self.diry = possible_moves[move][1]

                #possible do this instead, so we don't change references to variables
                #self.turns[self.pos[:] = [self.dirx, self,diry]
                self.turns[self.pos] = [self.dirx, self.diry]

        for index, cube in enumerate(self.body):
            cube_pos = cube.pos[:]
            if cube_pos in self.turns:
                turn = self.turns[cube_pos]
                cube.move(turn[0], turn[1])
        else:
            raise ValueError(f'{move} is not a valid option, possible values: {[move for move in possible_moves]}')


class Cube():
    def __init__(self, start, dirx=1, diry=0, color=(255,255,255)):
        self.pos = start
        self.dirx = dirx
        self.diry = diry
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

class Food():
    def __init__(self, x, y, value=100, time_to_live = 100):
        self.x = x
        self.y = y
        self.value = value
        self.time_to_live = time_to_live

    def reduce_time_to_live(self):
        self.time_to_live += -1


