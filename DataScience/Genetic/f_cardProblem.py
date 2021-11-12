import unittest
import datetime
import numpy
import random
import genetic


class Fitness:
    def __init__(self, group1Sum, group2Mul, clon_count):
        self.clon_count = clon_count
        self.group1Sum = group1Sum
        self.group2Mul = group2Mul
        self.difference = \
            abs(36 - group1Sum) + abs(360 - group2Mul)

    def __gt__(self, other):
        if self.difference == other.difference:
            return self.clon_count < other.clon_count
        else:
            return self.difference < other.difference

    def __str__(self):
        return "sum: {} prod: {} clones: {}".format(
            self.group1Sum, self.group2Mul, self.clon_count)


def get_fitness(genes):
    group1Sum = sum(genes[0:5])
    group2Mul = numpy.product(genes[5:10])
    clon_count = (len(genes) - (len(set(genes))))
    return Fitness(group1Sum, group2Mul, clon_count)


def display(candidate, start_t):
    time_diff = datetime.datetime.now() - start_t
    print("[{}] [{}]\t{}\t{}".format(
        ', '.join(map(str, candidate.genes[0:5])),
        ', '.join(map(str, candidate.genes[5:10])),
        candidate.fitness, time_diff))


def mutate(genes, geneset):
    if len(genes) == len(set(geneset)):
        count = random.randint(1, 4)
        while count > 0:
            count -= 1
            iA, iB = random.sample(
                range(len(genes)), 2)
            genes[iA], genes[iB] = genes[iB], genes[iA]
    else:
        iA = random.randrange(0, len(genes))
        iB = random.randrange(0, len(geneset))
        genes[iA] = geneset[iB]
    return genes


def cardGame():
    geneset = [i + 1 for i in range(10)]
    start_t = datetime.datetime.now()
    optimal_fitness = Fitness(36, 360, 0)
    best = genetic.get_best(
        geneset, 10, optimal_fitness,
        lambda genes: get_fitness(genes),
        display=lambda candidate:
            display(candidate, start_t),
        custom_mutation=lambda genes:
            mutate(genes, geneset))
    return best, optimal_fitness


class CardTest(unittest.TestCase):
    def test(self):
        solution, optimal = cardGame()
        self.assertTrue(not optimal > solution.fitness)


if __name__ == '__main__':
    unittest.main()
