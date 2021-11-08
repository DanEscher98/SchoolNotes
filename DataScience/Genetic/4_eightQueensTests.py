import unittest
import datetime
import genetic


class eightQueensTests(unittest.TestCase):
    def test(self, size=10):
        geneset = [i for i in range(size)]
        start_t = datetime.datetime.now()
        optimal_fitness = Fitness(0)
        best = genetic.get_best(
            lambda candidate: display(candidate, start_t,
                                      size),
            lambda genes: get_fitness(genes, size),
            size, optimal_fitness, geneset)
        self.assertTrue(not optimal_fitness > best.fitness)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(20))


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
        board = [['.'] * size for _ in range(size)]
        for column in range(0, len(genes)):
            row = genes[column]
            board[row][column] = 'Q'
        self._board = board

    def print(self):
        # 0,0 prints in bottom left corner
        for i in reversed(range(0, len(self._board))):
            print('  '.join(self._board[i]))

    def get(self, row, column):
        return self._board[column][row]


def get_fitness(genes, size):
    board = Board(genes, size)
    rowsWithQueens = set()
    colsWithQueens = set()
    northEastDiagonalsWithQueens = set()
    southEastDiagonalsWithQueens = set()
    for row in range(size):
        for col in range(size):
            if board.get(row, col) == 'Q':
                rowsWithQueens.add(row)
                colsWithQueens.add(col)
                northEastDiagonalsWithQueens.add(row + col)
                southEastDiagonalsWithQueens.add(size - 1 -
                                                 row + col)
    total = 4 * size - (len(rowsWithQueens) +
                        len(colsWithQueens) +
                        len(northEastDiagonalsWithQueens) +
                        len(southEastDiagonalsWithQueens))
    return Fitness(total)


def display(candidate, start_t, size):
    time_diff = datetime.datetime.now() - start_t
    board = Board(candidate.genes, size)
    board.print()
    print("{0}\t=> {1}\t{2}\n".format(
        '  '.join(map(str, candidate.genes)),
        candidate.fitness,
        str(time_diff)))


if __name__ == '__main__':
    unittest.main()
