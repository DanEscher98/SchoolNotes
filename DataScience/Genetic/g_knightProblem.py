import unittest
from datetime import datetime
import random
import string
from math import ceil, log, sqrt
from typing import List, Set
import genetic


# ###############################################
# PROBLEM DEFINITION ############################

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toTuple(self):
        return (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 1000 + self.y


class Knight(Position):
    def __init__(self, position, boardSize):
        super().__init__(position.x, position.y)
        self.attacks = get_attacks(position, boardSize)


class Board:
    def __init__(self, positions, size):
        # size.x = 4 if size.x < 4 else size.x
        # size.y = 4 if size.x < 4 else size.y
        board = [['·'] * size.x for _ in range(size.y)]
        for knight in positions:
            board[knight.y][knight.x] = '♞'
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

def get_NumKnigths(boardSize) -> int:
    width = boardSize.x
    height = boardSize.y
    n = ceil(sqrt(width*height))
    factor = 3/5  # Theorethically, 1/2 should work
    return ceil(factor * n**2 / log(n))


def get_attacks(location, boardSize) -> Set[Position]:
    attacks = set()
    moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
             (1, 2), (2, 1), (2, -1), (1, -2)]
    for (x, y) in moves:
        if 0 <= x + location.x < boardSize.x:
            if 0 <= y + location.y < boardSize.y:
                attacks.add(Position(x + location.x, y + location.y))
    return attacks


def get_fitness(genes, boardSize) -> int:
    attacked = set(pos for knight in genes
                   for pos in knight.attacks)
    return len(attacked)


def display(candidate, start_t, boardSize):
    time_diff = datetime.now() - start_t
    board = Board(candidate.genes, boardSize)
    board.print()
    print("\t{}\t{}\n".format(
        # ', '.join(map(str, candidate.genes)),
        candidate.fitness, str(time_diff)))


def create(expectedKights, get_randomPos, boardSize) -> List[Knight]:
    genes = set()
    while len(genes) < expectedKights:
        genes.add(Knight(get_randomPos(), boardSize))
    return list(genes)


def mutate(genes, get_randomPos, boardSize,
           allPositions, nonEdgePositions) -> List[Knight]:
    # Local minimum: when it ends with a knight
    # configuration where moving any knight results in a
    # worse fitness.
    count = 2 if random.randint(0, 10) == 0 else 1
    # This gives a 1/10 chance of making two changes, in
    # order to find the right pair of moves to get past a
    # local maximum.
    while count > 0:
        count -= 1
        # Determine which knights attack which squares
        positionToKnightIndexes = dict((p, [])
                                       for p in allPositions)
        for i, knight in enumerate(genes):
            for position in knight.attacks:
                positionToKnightIndexes[position].append(i)

        # Get a list of indexes of knights whose attacks are
        # all covered by some other knight and build a list
        # of the squares that are no under attack
        knightIndexes = set(i for i in range(len(genes)))
        unattacked = []
        for kvp in positionToKnightIndexes.items():
            if len(kvp[1]) > 1:
                continue
            if len(kvp[1]) == 0:
                unattacked.append(kvp[0])
                continue
            for p in kvp[1]:
                if p in knightIndexes:
                    knightIndexes.remove(p)

        # Get list of locations from which the unattacked
        # squares can be attacked. More duplicates makes
        # them more likely to be selected.
        potentialKnightPositions = \
            [p for positions in
             map(lambda x: get_attacks(x, boardSize),
                 unattacked)
             for p in positions if p in nonEdgePositions] \
            if len(unattacked) > 0 else nonEdgePositions

        # Then we choose a knight to replace.
        geneIndex = random.randrange(0, len(genes)) \
            if len(knightIndexes) == 0 \
            else random.choice([i for i in knightIndexes])

        # We replace the knight to try to improve the fitness
        position = random.choice(potentialKnightPositions)
        genes[geneIndex] = Knight(
            position, boardSize)
    return genes


def knightPositions(boardSize):
    # boardSize should be at least 3x4
    # A knight can attack at most, 4 squares from and edge,
    # whereas being located just one square away from any
    # edge increases that to 6 squares
    allPositions = [Position(x, y)
                    for y in range(boardSize.y)
                    for x in range(boardSize.x)]
    if boardSize.x < 6 or boardSize.y < 6:
        nonEdgePositions = allPositions
        low_limit = 0
        x_limit = boardSize.x
        y_limit = boardSize.y
    else:
        nonEdgePositions = [i for i in allPositions
                            if 0 < i.x < boardSize.x - 1 and
                            0 < i.y < boardSize.y]
        low_limit = 1
        x_limit = boardSize.x - 1
        y_limit = boardSize.y - 1

    def get_randomPos():
        return Position(random.randrange(low_limit, x_limit),
                        random.randrange(low_limit, y_limit))
    start_t = datetime.now()
    optimal_fitness = boardSize.x * boardSize.y
    numOfKnights = get_NumKnigths(boardSize)

    best = genetic.get_best(
        None, None, optimal_fitness,
        get_fitness=lambda genes:
            get_fitness(genes, boardSize),
        display=lambda candidate:
            display(candidate, start_t, boardSize),
        custom_mutation=lambda genes:
            mutate(genes, get_randomPos, boardSize,
                   allPositions, nonEdgePositions),
        custom_create=lambda:
            create(numOfKnights, get_randomPos, boardSize))
    return best


#################################################
# Tests and Main Function #######################

class KnightsTest(unittest.TestCase):
    def test_3x4(self):
        boardSize = Position(16, 16)
        optimal_fitness = boardSize.x * boardSize.y
        best = knightPositions(boardSize)
        self.assertTrue(not optimal_fitness > best.fitness)


if __name__ == '__main__':
    unittest.main()
