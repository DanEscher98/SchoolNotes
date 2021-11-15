import unittest
from datetime import datetime
from sys import maxsize
import random
import genetic


class Resource:
    def __init__(self, name, value, weight, volume):
        self.name = name
        self.value = value
        self. weight = weight
        self. volume = volume


class ItemQuantity:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __eq__(self, other):
        return self.item == other.item and \
            self.quantity == other.quantity


class Fitness:
    def __init__(self, totalWeight, totalVolume,
                 totalValue):
        self.totalWeight = totalWeight
        self.totalVolume = totalVolume
        self.totalValue = totalValue

    def __gt__(self, other):
        if self.totalValue != other.totalValue:
            return self.totalValue > other.totalValue
        elif self.totalWeight != other.totalWeight:
            return self.totalWeight < other.totalWeight
        else:
            return self.totalVolume < other.totalVolume

    def __str__(self):
        return "wt: {:0.2f} vol: {:0.2f} value: {}".format(
            self.totalWeight,
            self.totalVolume,
            self.totalValue)


def max_quantity(item, maxWeight, maxVolume):
    return min(int(maxWeight / item.weight)
               if item.weight > 0 else maxsize,
               int(maxVolume / item.volume)
               if item.volume > 0 else maxsize)


def add_item(genes, items, maxWeight, maxVolume):
    usedItems = {item_q.item for item_q in genes}
    item = random.choice(items)
    while item in usedItems:
        item = random.choice(items)

    maxQuantity = max_quantity(item, maxWeight, maxVolume)
    return ItemQuantity(item, maxQuantity) \
        if maxQuantity > 0 else None


def get_fitness(genes):
    totalWeight = 0
    totalVolume = 0
    totalValue = 0
    for item_q in genes:
        count = item_q.quantity
        totalWeight += item_q.item.weight * count
        totalVolume += item_q.item.volume * count
        totalValue += item_q.item.value * count
    return Fitness(totalWeight, totalVolume, totalValue)


def display(candidate, start_t):
    time_diff = datetime.now() - start_t
    genes = candidate.genes[:]
    genes.sort(key=lambda item_q: item_q.quantity,
               reverse=True)
    descriptions = [str(item_q.quantity) + "x" + item_q.item.name
                    for item_q in genes]
    if len(descriptions) == 0:
        descriptions.append("Empty")
    print("{}\t{}\t{}".format(
        ', '.join(descriptions),
        candidate.fitness,
        time_diff))


def mutate(genes, items, maxWeight, maxVolume):
    fitness = get_fitness(genes)
    remWeight = maxWeight - fitness.totalWeight
    remVolume = maxVolume - fitness.totalVolume

    removing = len(genes) > 1 and random.randint(0, 10) == 0
    if removing:
        index = random.randrange(0, len(genes))
        item_q = genes[index]
        item = item_q.item
        remWeight += item.weight * item_q.quantity
        remVolume += item.volume * item_q.quantity
        del genes[index]

    adding = (remWeight > 0 or remVolume > 0) and \
        (len(genes) == 0 or
         (len(genes) < len(items) and random.randint(0, 100) == 0))
    if adding:
        new_gene = add_item(genes, items, remWeight, remVolume)
        if new_gene is not None:
            genes.append(new_gene)
            return genes

    index = random.randrange(0, len(genes))
    item_q = genes[index]
    item = item_q.item
    remWeight += item.weight * item_q.quantity
    remVolume += item.volume * item_q.quantity

    changeItem = len(genes) < len(items) and \
        random.randint(0, 4) == 0
    if changeItem:
        itema, itemb = random.sample(items, 2)
        item = itema if itema != item else itemb

    maxQuantity = max_quantity(item, remWeight, remVolume)
    if maxQuantity > 0:
        quantity = random.randint(1, maxQuantity)
        genes[index] = ItemQuantity(item, quantity)
    else:
        del genes[index]
    return genes


def create(items, maxWeight, maxVolume):
    genes = []
    remWeight, remVolume = maxWeight, maxVolume
    for i in range(random.randrange(1, len(items))):
        new_gene = add_item(genes, items, remWeight, remVolume)
        if new_gene is not None:
            genes.append(new_gene)
            remWeight -= new_gene.quantity * new_gene.item.weight
            remVolume -= new_gene.quantity * new_gene.item.volume
    return genes


def fill_knapsack(items, maxWeight, maxVolume, optimal):
    start_t = datetime.now()
    best = genetic.get_best(
        items, None, optimal,
        get_fitness=lambda genes: get_fitness(genes),
        display=lambda candidate:
            display(candidate, start_t),
        custom_mutation=lambda genes:
            mutate(genes, items, maxWeight, maxVolume),
        custom_create=lambda:
            create(items, maxWeight, maxVolume),
        max_age=50)
    return best


class KnapsackTests(unittest.TestCase):
    def test_cookies(self):
        items = [
            Resource("Flour", 1680, 0.265, 0.41),
            Resource("Butter", 1440, 0.5, 0.13),
            Resource("Sugar", 1840, 0.441, 0.29)
        ]
        maxWeight = 10
        maxVolume = 4
        optimal = get_fitness(
            [ItemQuantity(items[0], 1),
             ItemQuantity(items[1], 14),
             ItemQuantity(items[2], 6)])
        best = fill_knapsack(
            items, maxWeight, maxVolume, optimal)
        self.assertTrue(not optimal > best.fitness)


if __name__ == '__main__':
    unittest.main()
