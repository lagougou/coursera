# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        self.row = row
        self.col = col

    """initialize the """
    def eat_sprout(self):
        pass

    def __str__(self):
        return '{} at ({},{}) ate {}'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)




class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, r1, r2):
        self.maze = maze
        self.r1 = r1
        self.r2 = r2
        self.num_sprouts_left = 0

    """judge the location is wall?"""
    def is_wall(self, r, c):
        return self.maze[r][c] == WALL

    """"""
    def get_character(self, r, c):
        if self.maze[r][c] == RAT_1_CHAR or self.maze[r][c] == RAT_2_CHAR:
            return self.maze[r][c]

    def move(self, rat, vertical_move, horizon_move):
        new_col = rat.col + vertical_move
        new_row = rat.row + horizon_move
        # judge the new location is wall
        if self.is_wall(new_row, new_col):
            pass
        else:
            rat.set_location(rat.row, rat.col)
        return True

    def __str__(self):
        return "{1} \n {2} at ({3},{4}) ate {5}\n{7}at ({8},{9}) ate {10}",format()