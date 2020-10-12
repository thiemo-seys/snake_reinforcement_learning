class SnakeEnv:
    SIZE = 10
    RETURN_IMAGES = True
    MOVE_PENALTY = 1
    FOOD_REWARD = 25
    OBSERVATION_SPACE_VALUES = (SIZE, SIZE, 3)  # 4
    ACTION_SPACE_SIZE = 4
    PLAYER_N = 1  # player key in dict
    FOOD_N = 2  # food key in dict
    # the dict! (colors)
    d = {1: (255, 175, 0),
         2: (0, 255, 0)}

