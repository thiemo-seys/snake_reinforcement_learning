import random


class Board():
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = [[Square(x=x, y=y) for x in range(self.width)] for y in range(self.height)]
        # amount of iterations the board has gone through, also used to reduce the time to live of the food class
        self.snake = Snake((5, 5), dirx=1, diry=0)
        self.turn = 0


    def move_snake(self):
        self.snake.move_snake()

    # sets the snake to the relevant squares on the board
    def set_snake_to_board(self):
        for snake_body_piece in self.snake.body:
            print(f'setting snake body piece: {snake_body_piece}')
            print(f'snake x= {snake_body_piece.pos[0]}')
            x,y =snake_body_piece.pos[0], snake_body_piece.pos[1]
            self.board[x][y].square_object = snake_body_piece

    # TODO: this method needs to be split up in methods that each place a different object on the board
    def update_cell_object(self, x, y, new_object):
        self.board[x][y].square_object = new_object

    def placeSnakeHead(self, start_pos):
        self.board[start_pos[0]][start_pos[1]] = Snake(start_pos)

    def placeFood(self, start_pos=None):
        # no specific position was specified, so putting food in a random free place
        if start_pos is None:
            food_squares = self.get_food_squares()
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

            # check if the random food square is not yet occupied
            while (x, y) in food_squares:
                x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        else:
            x, y = start_pos

        self.board[x][y].square_object = Food(x, y)

    def get_squares_containing_object(self, object_name):
        # also add head and tail here
        object_name_type_mapping = {'empty': None, 'snake': Cube, 'food': Food, 'head': Snake, 'tail': Snake}

        squares_containing_object = []

        for x, row in enumerate(self.board):
            for y, square in enumerate(row):
                if object_name_type_mapping.get(object_name) is None:
                    if square.square_object is None:
                        squares_containing_object.append((x, y))

                elif isinstance(square.square_object, object_name_type_mapping.get(object_name)):
                    squares_containing_object.append((x, y))
        return squares_containing_object

    # check which squares contains a square object with value 1
    def get_empty_squares(self):
        return self.get_squares_containing_object('empty')

    def get_food_squares(self):
        return self.get_squares_containing_object('food')

    # TODO: check what is better
    # this method can be changed to a method in the Snake class
    def get_snake_body_squares(self):
        return self.get_squares_containing_object('snake')

    def get_snake_tail_pos(self):
        pass

    def get_snake_head_pos(self):
        pass

    def reset_board(self):
        self.board = [[Square(x=x, y=y) for x in range(self.width)] for y in range(self.height)]

    # maybe override this method for pretty printing?
    # but seems weird to print it pretty because return breaks the function
    # def __str__(self):
    #    pass


class Square():
    def __init__(self, x, y, square_object=None):
        self.x = x
        self.y = y
        self.square_object = square_object

    def __str__(self):
        return str(self.object)


#############################################################################################################################################
class Snake():
    def __init__(self, start_pos, dirx=1, diry=0):
        self.head = Cube(start_pos, dirx=dirx, diry=diry)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.pos = start_pos
        self.dirx = dirx
        self.diry = diry

    # get pos and direction velocities from latest snake body part
    def add_cube_to_tail(self):
        # get info of last element in the snakes body
        tail = self.body[-1]
        dirx, diry = tail.dirx, tail.diry
        x, y = tail.pos[0], tail.pos[1]
        # TODO: debug this to see if we do not need to offset the cubes position in account of the snakes tails velocity
        # add cube element after the last position in list
        self.body.append(Cube(start=(x, y), dirx=dirx, diry=diry))

    def change_direction(self, move):
        possible_moves = {'up': [0, 1], 'down': [0, -1], 'right': [1, 0], 'left': [-1, 0]}
        opposite_moves = {'up': 'down', 'down': 'up', 'right': 'left', 'left': 'right'}

        if move in possible_moves:
            # check if current move is not an impossible move
            if move != opposite_moves[self.move]:
                self.dirx = possible_moves[move][0]
                self.diry = possible_moves[move][1]

                # possible do this instead, so we don't change references to variables
                # self.turns[self.pos[:] = [self.dirx, self,diry]
                self.turns[self.pos] = [self.dirx, self.diry]
        else:
            raise ValueError(f'{move} is not a valid option, possible values: {[move for move in possible_moves]}')

    def move_snake(self):
        for cube in self.body:
            cube_pos = cube.pos[:]
            if cube_pos in self.turns:
                turn = self.turns[cube_pos]
                cube.set_direction(turn[0], turn[1])
            #move the cube
            cube.move()


# a piece of snake Body
class Cube():
    def __init__(self, start, dirx, diry):
        self.pos = start
        self.dirx = dirx
        self.diry = diry

    # sets the direction vectors of the cube
    def set_direction(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry

    # moves the cube 1 turn further
    def move(self):
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)


class Food():
    def __init__(self, x, y, value=100, time_to_live=100):
        self.x = x
        self.y = y
        self.value = value
        self.time_to_live = time_to_live

    def reduce_time_to_live(self, amount=1):
        self.time_to_live += -amount



bord = Board()
bord.set_snake_to_board()
print(bord.board[5][5].square_object)
print(bord.get_snake_body_squares())
bord.move_snake()
bord.set_snake_to_board()
print(bord.board[5][5].square_object)
print(bord.get_snake_body_squares())
