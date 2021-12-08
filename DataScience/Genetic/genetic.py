import random
import statistics
from typing import Iterator
import time
import sys
from bisect import bisect_left
from math import exp


class Chromosome:
    def __init__(self, genes, fitness, mutations):
        self.genes = genes
        self.fitness = fitness
        self.mutations = mutations
        self.age = 0

    def reset(self):
        self.mutations = 0


class Results:
    def __init__(self, chromosome):
        self.best_chromosome = chromosome
        self.age_series = []

    def one_mut(self):
        self.mutations += 1

    def reset(self):
        self.mutations = 0

    def new_best(self, chromosome):
        self.best_chromosome = chromosome


def _initparent(length, geneset, get_fitness) -> Chromosome:
    genes = []
    while len(genes) < length:
        sample_size = min(length - len(genes), len(geneset))
        genes.extend(random.sample(geneset, sample_size))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness, 0)


def _mutate_typeA(genes, geneset) -> str:
    index = random.randrange(0, len(genes))
    new_gene, aux_gene = random.sample(geneset, 2)
    genes[index] = aux_gene if new_gene == genes[index] else new_gene
    return genes


def _mutate(parent, get_fitness, mutation_type) -> Chromosome:
    genes = parent.genes[:]
    genes = mutation_type(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness, parent.mutations + 1)


def _evolution(mutate, init_parent, max_age) -> Iterator[Chromosome]:
    parent = bestParent = init_parent()
    # result = Results(parent)
    yield parent
    historicalFitnesses = [bestParent.fitness]
    while True:
        child = mutate(parent)
        if parent.fitness > child.fitness:
            if max_age is not None:
                # One more time, the parent has better fitness
                parent.age += 1  # Aging
                if not max_age > parent.age:  # parent.age >= max_age
                    index = bisect_left(  # insert in order
                        historicalFitnesses,
                        child.fitness,
                        0,
                        len(historicalFitnesses),
                    )
                    proportionSimilar = 1 - index / len(historicalFitnesses)
                    # The lineage dies or steps backwards
                    if random.random() >= exp(-proportionSimilar):
                        parent = bestParent  # Worst case (reset)
                        parent.age = 0
                        # print("Worst case")
                    else:
                        parent = child  # Bad case (backwards)
                        # print("Set backwards")
        elif not child.fitness > parent.fitness:
            # same fitnezz
            child.age = parent.age + 1  # Aging
            parent = child  # Neutral case
            # print("Neutral case")
        else:
            # The child's fitness is greater than that of the parent
            parent = child  # Best local
            parent.age = 0  # Fresh progress
            if child.fitness > bestParent.fitness:
                yield child
                child.reset()
                bestParent = child  # Happy ending
                # print("Happy ending")
                historicalFitnesses.append(child.fitness)


def get_best(
    gene_set,
    length,
    optimal_fitness,
    get_fitness,
    display=None,
    custom_mutation=None,
    custom_create=None,
    max_age=None,
):
    """Algorithm loop. Mutates until the fitness of child is
    equal or better than the optimal_fitness"""
    # Initialize Functions
    if custom_mutation is None:

        def mutate(parent):
            return _mutate(
                parent,
                get_fitness,
                lambda genes: _mutate_typeA(genes, gene_set),
            )

    else:

        def mutate(parent):
            return _mutate(
                parent, get_fitness, lambda genes: custom_mutation(genes)
            )

    if custom_create is None:

        def init_parent():
            return _initparent(length, gene_set, get_fitness)

    else:

        def init_parent():
            genes = custom_create()
            return Chromosome(genes, get_fitness(genes), 0)

    # The Mutation-Selection Loop
    for count, generation in enumerate(
        _evolution(mutate, init_parent, max_age)
    ):
        print(
            "Generation {}, Mutations: {}".format(count, generation.mutations)
        )
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
                print(
                    "{0} {1:3.2f} {2:3.2f}".format(
                        1 + i,
                        mean,
                        statistics.stdev(timings, mean) if i > 1 else 0,
                    )
                )
