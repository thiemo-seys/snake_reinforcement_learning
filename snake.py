import random


class Board():
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]


    def update_cell_object(self, x, y, new_object):
        self.board[x][y] = new_object


    def reset_board(self):
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]

    def __str__(self):
        #pretty print the board
        for row in self.board:
            print(row)



class Square(Board):
    def __init__(self, x, y, object):
        super().__init__()


class Snake():
    def __init__(self, start_pos, dirx=1, diry=0):
        pass

    def add_cube(self):
        pass

    def move(self, dirx, diry):
        pass

    def change_direction(self, x,y):
        self.dirx = x
        self.diry = y

    def reset(self):
        pass

class Cube():
    def __init__(self):
        pass


class Food():
    def __init__(self):
        pass