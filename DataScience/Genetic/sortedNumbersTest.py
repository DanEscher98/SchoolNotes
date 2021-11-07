import unittest
import datetime
import genetic

class sortedNumbersTest(unittest.TestCase):
    def test_sort_10_numbers(self):
        self.sort_numbers(10)

    def sort_numbers(self, total_numbers):
        gene_set = [i for i in range(100)]
        start_t = datetime.datetime.now()

        optimal_fitness = Fitness(total_numbers, 0)
        best = genetic.get_best(
            lambda candidate: display(candidate, start_t),
            lambda genes: get_fitness(genes),
            total_numbers, optimal_fitness, gene_set)
        self.assertTrue(not optimal_fitness > best.fitness)


class Fitness:
    count_nums_inseq = None
    total_gap = None

    def __init__(self, count_nums_inseq, total_gap):
        self.count_nums_inseq = count_nums_inseq
        self.total_gap = total_gap

    def __gt__(self, other):
        if self.count_nums_inseq != other.count_nums_inseq:
            return self.count_nums_inseq > other.count_nums_inseq
        else:
            return self.total_gap < other.total_gap

    def __str__(self):
        return "Sequential: {0}, Total Gap: {1}".format(
            self.count_nums_inseq, self.total_gap)


def get_fitness(genes):
    fitness = 1
    gap = 0
    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Fitness(fitness, gap)

def display(candidate, start_t):
    time_diff = datetime.datetime.now()
    print("{0}\t=> {1}\t{2}".format(
        ", ".join(map(str, candidate.genes)),
        candidate.fitness,
        str(time_diff)))


if __name__=='__main__':
    unittest.main()
