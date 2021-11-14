import unittest
from datetime import datetime
import random
import genetic


def get_sums(genes, size):
    rowSum = [0 for _ in range(size)]
    colSum = [0 for _ in range(size)]
    s_DiagonalSum = 0
    n_DiagonalSum = 0

    for row in range(size):
        for col in range(size):
            value = genes[row * size + col]
            rowSum[row] += value
            colSum[col] += value
        s_DiagonalSum += genes[row * size + row]
        n_DiagonalSum += genes[row * size +
                               (size - 1 - row)]
    return rowSum, colSum, s_DiagonalSum, n_DiagonalSum


def get_fitness(genes, size, expectedSum):
    rowSum, colSum, s_DiagonalSum, n_DiagonalSum = \
        get_sums(genes, size)
    fitness = sum(1 for s in rowSum + colSum +
                  [s_DiagonalSum, n_DiagonalSum]
                  if s == expectedSum)
    return fitness


def display(candidate, size, start_t):
    time_diff = datetime.now() - start_t
    rowSum, colSum, s_DiagonalSum, n_DiagonalSum = \
        get_sums(candidate.genes, size)
    for i in range(size):
        row = candidate.genes[i * size: (i+1) * size]
        print(f"\t {row} = {rowSum[i]}")
    print(n_DiagonalSum, "\t", colSum, "\t", s_DiagonalSum)
    print(' '.join('-'*size*3), candidate.fitness, time_diff)


def mutation(genes):
    indexes = list(range(len(genes)))
    index_a, index_b = random.sample(indexes, 2)
    genes[index_a], genes[index_b] = \
        genes[index_b], genes[index_a]
    return genes


def magicSquares(size):
    geneset = [i+1 for i in range(size**2)]
    expectedSum = size * (size**2 + 1) / 2
    optimal_fitness = 2 * (1 + size)
    start_t = datetime.now()
    best = genetic.get_best(
        geneset, size**2, optimal_fitness,
        get_fitness=lambda genes:
            get_fitness(genes, size, expectedSum),
        display=lambda candidate:
            display(candidate, size, start_t),
        custom_mutation=lambda genes: mutation(genes),
        custom_create=lambda:
            random.sample(geneset, len(geneset)))
    return best, optimal_fitness


class magicSquaresTest(unittest.TestCase):
    def test(self):
        best, optimal_fitness = magicSquares(100)
        self.assertTrue(not optimal_fitness > best.fitness)


if __name__ == '__main__':
    unittest.main()
