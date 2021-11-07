import unittest
import datetime
import genetic

class oneMaxTests(unittest.TestCase):
    def test(self, length=100):
        geneset = [0, 1]
        start_t = datetime.datetime.now()
        optimal_fitness = length
        best = genetic.get_best(
            lambda candidate: display(candidate, start_t),
            lambda genes: get_fitness(genes),
            length, optimal_fitness, geneset)
    
    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(4000))


def get_fitness(genes):
    return genes.count(1)

def display(candidate, start_t):
    time_diff = datetime.datetime.now() - start_t
    print("{0}...{1}\t{2:3.2f}\t{3}".format(
        ''.join(map(str, candidate.genes[:15])),
        ''.join(map(str, candidate.genes[-15:])),
        candidate.fitness,
        str(time_diff)
    ))

if __name__=='__main__':
    unittest.main()
