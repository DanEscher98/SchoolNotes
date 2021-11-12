import unittest
import datetime
import random
import string
from math import ceil, log, sqrt
import genetic


# ###############################################
# PROBLEM DEFINITION ############################


class Position:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 1000 + self.y


class Knight():
    def __init__(self, position, boardSize):
        self.position = position
        self.attacks = get_attacks(position, boardSize)

    def __str__(self):
        return f"({self.position.x}, {self.position.y})"


class Board:
    def __init__(self, positions, size):
        # size.x = 4 if size.x < 4 else size.x
        # size.y = 4 if size.x < 4 else size.y
        board = [['·'] * size.x for _ in range(size.y)]
        for knight in positions:
            board[knight.position.y][knight.position.x] = '♞'
        self.board = board
        self.width = size.x
        self.height = size.y

    def print(self):
        # 0,0 prints in bottom left corner
        for i in reversed(range(self.height)):
            print("{:4d} {}".format(
                i+1, '  '.join(self.board[i])))
        if self.width < 27:
            x_labels = list(map(chr, range(65, 65+self.width)))
        else:
            x_labels = list(string.ascii_uppercase) + \
                list(map(str, list(range(27, self.width))))
        print("     {}".format('  '.join(x_labels)))


#################################################
# GENETIC ALGORITHM FUNCTIONS ###################


def get_NumKnigths(boardSize):
    width = boardSize.x
    height = boardSize.y
    n = ceil(sqrt(width*height))
    factor = 1/2  # Theorethically, 1/2 should work
    return ceil(factor * n**2 / log(n))


def get_attacks(location, boardSize):
    attacks = []
    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
             (1, 2), (2, 1), (2, -1), (1, -2)]
    for (x, y) in moves:
        if 0 <= x + location.x < boardSize.x:
            if 0 <= y + location.y < boardSize.y:
                attacks.append(Position(
                    x + location.x, y + location.y))
    return attacks


def get_fitness(genes, boardSize):
    attacked = set(pos for knight in genes
                   for pos in knight.attacks)
    return len(attacked)


def display(candidate, start_t, boardSize):
    time_diff = datetime.datetime.now() - start_t
    board = Board(candidate.genes, boardSize)
    board.print()
    print("\t{}\t{}\n".format(
        # ', '.join(map(str, candidate.genes)),
        candidate.fitness, str(time_diff)))


def create(expectedKights, get_randomPos, boardSize):
    genes = [Knight(get_randomPos(), boardSize)
             for _ in range(expectedKights)]
    return genes


def mutate(genes, get_randomPos, boardSize):
    index = random.randrange(0, len(genes))
    position = get_randomPos()
    genes[index] = Knight(position, boardSize)
    return genes


def knightPositions(boardSize):
    # boardSize should be at least 3x4
    # A knight can attack at most, 4 squares from and edge,
    # whereas being located just one square away from any
    # edge increases that to 6 squares
    if boardSize.x < 6 or boardSize.y < 6:
        low_limit = 0
        x_limit = boardSize.x
        y_limit = boardSize.y
    else:
        low_limit = 1
        x_limit = boardSize.x - 1
        y_limit = boardSize.y - 1

    def get_randomPos():
        return Position(random.randrange(low_limit, x_limit),
                        random.randrange(low_limit, y_limit))
    start_t = datetime.datetime.now()
    optimal_fitness = boardSize.x * boardSize.y
    numOfKnights = get_NumKnigths(boardSize)

    best = genetic.get_best(
        None, None, optimal_fitness,
        get_fitness=lambda genes:
            get_fitness(genes, boardSize),
        display=lambda candidate:
            display(candidate, start_t, boardSize),
        custom_mutation=lambda genes:
            mutate(genes, get_randomPos, boardSize),
        custom_create=lambda:
            create(numOfKnights, get_randomPos, boardSize))
    return best


#################################################
# Tests and Main Function #######################


class KnightsTest(unittest.TestCase):
    def test_3x4(self):
        boardSize = Position(100, 100)
        optimal_fitness = boardSize.x * boardSize.y
        best = knightPositions(boardSize)
        self.assertTrue(not optimal_fitness > best.fitness)


if __name__ == '__main__':
    unittest.main()
