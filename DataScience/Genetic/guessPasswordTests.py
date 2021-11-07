import datetime
import unittest
import genetic


class guessPasswordTests(unittest.TestCase):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    
    def test_Hello_World(self):
        target = "Hello World!"
        best = guess_password(target, self.gene_set)
        self.assertEqual(best, target)

    


def get_fitness(guess, target):
    """Gets the total of characters matched"""
    return sum( 1 for expected, actual in zip(target, guess)
               if expected == actual )


def display(guess, target, start_t):
    time_diff = datetime.datetime.now() - start_t
    fitness = get_fitness(guess, target)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(time_diff)))


def guess_password(target, gene_set):
    start_t = datetime.datetime.now()
    optimal_fitness = len(target)
    return genetic.get_best(lambda guess: get_fitness(guess, target),
                     optimal_fitness,
                     optimal_fitness,
                     gene_set,
                     lambda guess: display(guess, target, start_t))

if __name__=='__main__':
    unittest.main()
