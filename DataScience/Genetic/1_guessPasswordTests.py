import datetime
import unittest
import random
import genetic


def display(candidate, target, start_t):
    time_diff = datetime.datetime.now() - start_t
    print("{0}\t{1}\t{2}".format(
        ''.join(candidate.genes),
        candidate.fitness, str(time_diff)))


def get_fitness(guess, target):
    """Gets the total of characters matched"""
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)


class guessPasswordTests(unittest.TestCase):
    lower_case = "abcdefghijklmnñopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numbers = "0123456789"
    ascii_chars = " ,.!?@_-"
    gene_set = lower_case + upper_case + numbers + ascii_chars

    def test_Hello_World(self):
        target = "Hello World! My name is Daniel"
        best = guess_password(target, self.gene_set)
        self.assertEqual(''.join(best.genes), target)

    def test_Random(self):
        length = 50
        target = ''.join(random.choice(self.gene_set)
                         for _ in range(length))
        guess_password(target, self.gene_set)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Hello_World)


def guess_password(target, gene_set):
    start_t = datetime.datetime.now()
    optimal_fitness = len(target)
    return genetic.get_best(
        gene_set, len(target), optimal_fitness,
        lambda guess: display(guess, target, start_t),
        lambda guess: get_fitness(guess, target))


if __name__ == '__main__':
    unittest.main()
