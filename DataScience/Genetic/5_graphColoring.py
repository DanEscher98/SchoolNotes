import datetime
import unittest
import csv
import genetic


def get_fitness(genes, rules, stateIndexLookup):
    rulesThatPass = sum(1 for rule in rules
                        if rule.IsValid(genes, stateIndexLookup))
    return rulesThatPass


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(
        ''.join(map(str, candidate.genes)),
        candidate.fitness, timeDiff))


def load_data(localFileName):
    """ expects: T D1 [D2 ... DN]
        where T is the record type
        and D1 .. DN are record-type appropriate data elements
    """
    rules = set()
    nodes = set()
    with open(localFileName, mode='r') as infile:
        content = infile.read().splitlines()
    for row in content:
        if row[0] == 'e':  # e aa bb, aa and bb are node ids
            nodeIds = row.split(' ')[1:3]
            rules.add(Rule(nodeIds[0], nodeIds[1]))
            nodes.add(nodeIds[0])
            nodes.add(nodeIds[1])
        elif row[0] == 'n':  # n aa ww, aa is a node id, ww is a weight
            nodeIds = row.split(' ')
            nodes.add(nodeIds[1])
    return rules, nodes


class Rule:
    def __init__(self, node, adjacent):
        if node < adjacent:
            node, adjacent = adjacent, node
        self.Node = node
        self.Adjacent = adjacent

    def __eq__(self, other):
        return self.Node == other.Node and self.Adjacent == other.Adjacent

    def __hash__(self):
        return hash(self.Node) * 397 ^ hash(self.Adjacent)

    def __str__(self):
        return self.Node + " -> " + self.Adjacent

    def IsValid(self, genes, nodeIndexLookup):
        index = nodeIndexLookup[self.Node]
        adjacentNodeIndex = nodeIndexLookup[self.Adjacent]

        return genes[index] != genes[adjacentNodeIndex]


class GraphColoringTests(unittest.TestCase):
    def test_states(self):
        self.color("adjacent_states.col",
                   ["Blue", "Green", "Red", "Yellow"])

    def color(self, file, colors):
        rules, nodes = load_data(file)
        optimalValue = len(rules)
        colorLookup = {color[0]: color for color in colors}
        geneset = list(colorLookup.keys())
        startTime = datetime.datetime.now()
        nodeIndexLookup = {key: index
                           for index, key in enumerate(sorted(nodes))}

        best = genetic.get_best(
            lambda candidate: display(candidate, startTime),
            lambda genes: get_fitness(genes, rules,
                                      nodeIndexLookup),
            len(nodes), optimalValue, geneset)
        self.assertTrue(not optimalValue > best.fitness)

        keys = sorted(nodes)
        for index in range(len(nodes)):
            print(keys[index] + " is " + colorLookup[best.genes[index]])


# Optional Functions
def convert_file(csv_file):
    """ expects: AA, BB;CC """
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile)
        states = {row[0]: row[1].split(';') for row in reader if row}
    output = []
    node_count = edge_count = 0

    for state, adjacents in states.items():
        node_count += 1
        for adjacent in adjacents:
            if adjacent == '':
                output.append("n {} 0".format(state))
            else:
                output.append("e {} {}".format(state,
                                               adjacent))
    with open('./adjacent_states.col', mode='w+') as outfile:
        print("p edge {} {}".format(node_count, edge_count),
              file=outfile)
        for line in sorted(output):
            print(line, file=outfile)


def build_rules(items):
    rulesAdded = {}
    for state, adjacent in items.items():
        for adjacentState in adjacent:
            if adjacentState == '':
                continue
            rule = Rule(state, adjacentState)
            if rule in rulesAdded:
                rulesAdded[rule] += 1
            else:
                rulesAdded[rule] = 1
    for k, v in rulesAdded.items():
        if v != 2:
            print("rule {} is not bidirectional".format(k))
    return rulesAdded.keys()


if __name__ == '__main__':
    unittest.main()
