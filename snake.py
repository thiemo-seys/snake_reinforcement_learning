# TODO: work on detecting when snake is off board/hitting a wall.
# TODO: reset snake when hittig a wall
# TODO: place food and check if snake works when being longer

import random


class Board():
    def __init__(self, width=30, height=30):
        self.width = width
        self.height = height
        self.board = [[Square(x=x, y=y) for x in range(self.width)] for y in range(self.height)]
        # amount of iterations the board has gone through, also used to reduce the time to live of the food class
        self.snake = Snake((int(width/2), int(height/2)), dirx=1, diry=0)
        self.set_snake_to_board()
        self.food_coordinates = set([])
        self.score = 0
        self.turn = 0

    def move_snake(self):
        old_positions = set(body.pos for body in self.snake.body)
        self.snake.move_snake()
        new_positions = set(body.pos for body in self.snake.body)

        #TODO: this might be buggy, because we check the whole snake, and not only the head to see if it hits a food square
        for pos in new_positions:
            if pos in self.food_coordinates:
                self.food_coordinates.remove(pos)
                print('eaten a piece of food, increasing score')
                self.score = self.score+100
                self.snake.add_cube_to_tail()

        # gather coordinates that are only in the old set but not the new
        # and place a square object there again
        coordinates_to_set_empty = old_positions.difference(new_positions)

        for coordinate in coordinates_to_set_empty:
            x, y = coordinate
            self.board[x][y].square_object = None

        # set snake to board with updated positions
        self.set_snake_to_board()

    # sets the snake to the relevant squares on the board

    # turns the snake
    def turn_snake(self, direction):
        self.snake.change_direction(direction)

    def set_snake_to_board(self):
        # get future snake_pos
        for snake_body_piece in self.snake.body:
            x, y = snake_body_piece.pos[0], snake_body_piece.pos[1]
            self.board[x][y].square_object = snake_body_piece

    # TODO: this method needs to be split up in methods that each place a different object on the board
    def update_cell_object(self, x, y, new_object):
        self.board[x][y].square_object = new_object

    def placeSnakeHead(self, start_pos):
        self.board[start_pos[0]][start_pos[1]] = Snake(start_pos)

    def placeFood(self, start_pos=(15,15)):
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
        self.food_coordinates.add((x,y))

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

    #returns a tuple containing the snakes tail location
    def get_snake_tail_pos(self):
        return self.snake.body[0].pos

    #returns a tuple containing the snakes head location
    def get_snake_head_pos(self):
        return self.snake.body[-1].pos

    #resets to board to be fully empty squares
    def reset_board(self):
        self.board = [[Square(x=x, y=y) for x in range(self.width)] for y in range(self.height)]

class Square():
    def __init__(self, x, y, square_object=None):
        self.x = x
        self.y = y
        self.square_object = square_object

    #expand methods in here if every needed, at the moment the square class is rather useless

#############################################################################################################################################
class Snake():
    def __init__(self, start_pos, dirx=1, diry=0):
        self.head = Cube(start_pos, dirx=dirx, diry=diry)
        self.body = []
        self.body.append(self.head)
        self.turns = {}

    # get pos and direction velocities from latest snake body part
    def add_cube_to_tail(self):
        # get info of last element in the snakes body
        tail = self.body[-1]
        dirx, diry = tail.dirx, tail.diry
        x, y = tail.pos[0], tail.pos[1]
        # TODO: debug this to see if we do not need to offset the cubes position in account of the snakes tails velocity
        # add cube element after the last position in list
        self.body.append(Cube(start=(x-dirx, y-diry), dirx=dirx, diry=diry))

    # TODO; maybe make this a bit smarter by saving the moves dict as a class parameter
    def get_current_move(self):
        # invert dict, so we can use movement directions as keys
        possible_moves = {'up': (0, -1), 'down': (0, 1), 'right': (1, 0), 'left': (-1, 0)}
        possible_moves = {value: key for key, value in possible_moves.items()}
        head = self.body[0]
        x, y = head.dirx, head.diry
        return possible_moves[(x, y)]

    # TODO: needs work to actualy change head direction
    # decide if snake actualy needs to store its self.diry and dirx (probably not, because there is no global snake speed/direction!)
    def change_direction(self, move):
        opposite_moves = {'up': 'down', 'down': 'up', 'right': 'left', 'left': 'right'}
        possible_moves = {'up': (0, -1), 'down': (0, 1), 'right': (1, 0), 'left': (-1, 0)}

        current_move = self.get_current_move()
        if move in possible_moves:
            # check if current move is not an impossible move
            if move != opposite_moves[current_move] and move != current_move:
                self.dirx = possible_moves[move][0]
                self.diry = possible_moves[move][1]
                self.body[0].set_direction(self.dirx, self.diry)

                # possible do this instead, so we don't change references to variables
                # self.turns[self.pos[:] = [self.dirx, self,diry]
                self.turns[self.body[0].pos] = [self.body[0].dirx, self.body[0].diry]
        else:
            raise ValueError(f'{move} is not a valid option, possible values: {[move for move in possible_moves]}')

    def move_snake(self):
        for index, cube in enumerate(self.body):
            cube_pos = cube.pos
            # if tail is at a turn position, we remove the turn from the dictionary because the whole snake has passed the turn
            if cube_pos in self.turns:
                turn = self.turns[cube_pos]
                cube.set_direction(turn[0], turn[1])
                #if tail reached the turn, remove it form the dict
                if index == len(self.body)-1:
                    self.turns.pop(cube_pos)
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
