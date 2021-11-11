import random
import statistics
import time
import sys


class Chromosome:
    genes = None
    fitness = None

    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness


def _initparent(length, geneset, get_fitness) -> Chromosome:
    genes = []
    while len(genes) < length:
        sample_size = min(length - len(genes), len(geneset))
        genes.extend(random.sample(geneset, sample_size))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate_typeA(genes, geneset) -> str:
    index = random.randrange(0, len(genes))
    new_gene, aux_gene = random.sample(geneset, 2)
    genes[index] = aux_gene \
        if new_gene == genes[index] \
        else new_gene
    return genes


def _mutate(parent, get_fitness, mutation_type) -> Chromosome:
    genes = parent.genes[:]
    genes = mutation_type(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _evolution(mutate, init_parent) -> iter(str, int):
    count = 0
    parent = init_parent()
    yield (parent, count)
    while True:
        child = mutate(parent)
        count += 1
        if not parent.fitness > child.fitness:
            if child.fitness > parent.fitness:
                yield (child, count)
                count = 0
            parent = child


def get_best(gene_set, length, optimal_fitness,
             get_fitness, display=None, custom_mutation=None):
    """Algorithm loop. Mutates until the fitness of child is
    equal or better than the optimal_fitness"""
    if custom_mutation is None:
        def mutate(parent):
            return _mutate(
                parent, get_fitness,
                lambda genes: _mutate_typeA(genes, gene_set))
    else:
        def mutate(parent):
            return _mutate(
                parent, get_fitness,
                lambda genes: custom_mutation(genes))

    def init_parent():
        return _initparent(length, gene_set, get_fitness)

    for count, (generation, mutations) in enumerate(
            _evolution(mutate, init_parent)):
        print(f"Generation {count} Mutations: {mutations}")
        if display is not None:
            display(generation)
        if not optimal_fitness > generation.fitness:
            return generation


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
                    if i > 1 else 0))
