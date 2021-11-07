import random
import statistics
import time
import sys

class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        print()
        for i in range(100):
            sys.stdout = None
            start_t = time.time()
            function()
            seconds = time.time() - start_t
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{0} {1:3.2f} {2:3.2f}".format(
                    1 + i, mean,
                    statistics.stdev(timings, mean)
                    if i > 1 else 0 ))


class Chromosome:
    genes = None
    fitness = None
    
    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness


def _generate_parent(length, gene_set, get_fitness):
    """Generates a random guess. The loop is useful if the
    gene_set length is smaller than the target length."""
    genes = []
    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sample_size))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate(parent, gene_set, get_fitness):
    """Change one letter. Selects two random characters, and
    a random index. If one of the chars is equal to the
    elemento at the index, then the other is selected."""
    index = random.randrange(0, len(parent.genes))
    # Work with lists and strings
    child_genes = parent.genes[:]
    new_gene, alternate = random.sample(gene_set, 2)
    child_genes[index] = alternate \
        if new_gene == child_genes[index] \
        else new_gene
    fitness = get_fitness(child_genes)
    return Chromosome(child_genes, fitness)


def _get_improvement(new_child, generate_parent):
    best_parent = generate_parent
    yield best_parent
    while True:
        child = new_child(best_parent)
        if best_parent.fitness > child.fitness:
            continue
        if not child.fitness > best_parent.fitness:
            best_parent = child
            continue
        yield child
        best_parent = child


def get_best(display, get_fitness, target_len,
             optimal_fitness, gene_set):
    """Algorithm loop. Mutates until the fitness of child is
    equal or better than the optimal_fitness"""
    random.seed()
    for improvement in _get_improvement(
        lambda parent: _mutate(parent, gene_set, get_fitness),
        _generate_parent(target_len, gene_set, get_fitness)):
        display(improvement)
        if not optimal_fitness > improvement.fitness:
            return improvement
    
