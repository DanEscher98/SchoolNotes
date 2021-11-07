import datetime
import unittest
import genetic


class guessPasswordTests(unittest.TestCase):
    lower_case  = "abcdefghijklmnñopqrstuvwxyz"
    upper_case  = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numbers     = "0123456789"
    ascii_chars = " ,.!?@_-"
    gene_set = lower_case + upper_case + \
        numbers + ascii_chars
    
    def test_Hello_World(self):
        target = "Hello World! Today is a sunny day."
        best = guess_password(target, self.gene_set)
        self.assertEqual(best.genes, target)


def get_fitness(guess, target):
    """Gets the total of characters matched"""
    return sum( 1 for expected, actual in zip(target, guess)
               if expected == actual )


def display(candidate, target, start_t):
    time_diff = datetime.datetime.now() - start_t
    print("{0}\t{1}\t{2}".format(
        candidate.genes, candidate.fitness, str(time_diff)))


def guess_password(target, gene_set):
    start_t = datetime.datetime.now()
    optimal_fitness = len(target)
    return genetic.get_best(
        lambda guess: get_fitness(guess, target),
        optimal_fitness,
        optimal_fitness,
        gene_set,
        lambda guess: display(guess, target, start_t))


if __name__=='__main__':
    unittest.main()
