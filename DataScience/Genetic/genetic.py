import random

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
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate(parent, gene_set, get_fitness):
    """Change one letter. Selects two random characters, and
    a random index. If one of the chars is equal to the
    elemento at the index, then the other is selected."""
    index = random.randrange(0, len(parent.genes))
    child_genes = list(parent.genes)
    new_gene, alternate = random.sample(gene_set, 2)
    child_genes[index] = alternate \
        if new_gene == child_genes[index] \
        else new_gene
    genes = ''.join(child_genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def get_best(get_fitness, target_len,
             optimal_fitness, gene_set, display):
    """Algorithm loop. Mutates until the fitness of child is
    equal or better than the optimal_fitness"""
    random.seed()
    best_parent = _generate_parent(
        target_len, gene_set, get_fitness)
    display(best_parent)
    if best_parent.fitness >= optimal_fitness:
        return best_parent

    while True:
        child = _mutate(best_parent, gene_set, get_fitness)
        if child.fitness > best_parent.fitness:
            display(child)
            if optimal_fitness > child.fitness:
                best_parent.fitness = child.fitness
                best_parent = child
            else: return child # Success!
