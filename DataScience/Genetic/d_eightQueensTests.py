import unittest
import datetime
import genetic


class Fitness:
    total = None

    def __init__(self, total):
        self.total = total

    def __gt__(self, other):
        return self.total < other.total

    def __str__(self):
        return "{0}".format(self.total)


class Board:
    def __init__(self, genes, size):
        board = [['·'] * size for _ in range(size)]
        for column in range(0, len(genes)):
            row = genes[column]
            board[row][column] = '♛'
        self.board = board

    def print(self):
        # 0,0 prints in bottom left corner
        for i in reversed(range(0, len(self.board))):
            print('  '.join(self.board[i]))

    def get(self, row, column):
        return self.board[column][row]


def get_fitness(genes) -> Fitness:
    size = len(genes)
    colsWithQueens = len(genes)
    rowsWithQueens = len(set(genes))
    northEastDiagonalsWithQueens = set()
    southEastDiagonalsWithQueens = set()
    for col, row in enumerate(genes):
        northEastDiagonalsWithQueens.add(row + col)
        southEastDiagonalsWithQueens.add(
            size - 1 - row + col)
    total = 4 * size - (colsWithQueens +
                        rowsWithQueens +
                        len(northEastDiagonalsWithQueens) +
                        len(southEastDiagonalsWithQueens))
    return Fitness(total)


def display(candidate, start_t, size):
    time_diff = datetime.datetime.now() - start_t
    board = Board(candidate.genes, size)
    board.print()
    print("{0}\t=> {1}\t{2}\n".format(
        '  '.join(map(lambda n: str(n+1), candidate.genes)),
        candidate.fitness,
        str(time_diff)))


def eightQueens(size):
    geneset = [i for i in range(size)]
    start_t = datetime.datetime.now()
    optimal_fitness = Fitness(0)
    best = genetic.get_best(
        geneset, size, optimal_fitness,
        lambda genes: get_fitness(genes),
        display=lambda candidate:
            display(candidate, start_t, size))
    return best, optimal_fitness


class eightQueensTests(unittest.TestCase):
    def test(self, size=50):
        solution, optimal = eightQueens(size)
        self.assertTrue(not solution.fitness > optimal)

    # def test_benchmark(self):
    #   genetic.Benchmark.run(lambda: self.test(10))


if __name__ == '__main__':
    eightQueens(120)

# size=1000 -> Generation 491 Mutations: 2104125

# def get_fitness(genes, size):
#     board = Board(genes, size)
#     rowsWithQueens = set()
#     colsWithQueens = set()
#     northEastDiagonalsWithQueens = set()
#     southEastDiagonalsWithQueens = set()
#     for row in range(size):
#         for col in range(size):
#             if board.get(row, col) == 'Q':
#                 rowsWithQueens.add(row)
#                 colsWithQueens.add(col)
#                 northEastDiagonalsWithQueens.add(row + col)
#                 southEastDiagonalsWithQueens.add(size - 1 -
#                                                  row + col)
#     total = 4 * size - (len(rowsWithQueens) +
#                         len(colsWithQueens) +
#                         len(northEastDiagonalsWithQueens) +
#                         len(southEastDiagonalsWithQueens))
#     return Fitness(total)
