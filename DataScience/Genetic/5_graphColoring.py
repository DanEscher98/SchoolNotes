import unittest
import datetime
import genetic
import csv
import json

class graphColoring(unittest.TestCase):
    def test(self):
        states = load_data("us_adjstates.csv")
        rules = build_rules(states)
        optimal_value = len(rules)
        state_index_lookup = { key: index for index, key in
                              enumerate(sorted(states)) }

        colors = ["Yellow", "Red", "Green", "Blue"]
        color_lookup = { color[0]: color for color in colors }
        genset = list(color_lookup.keys())

def load_data(local_filename):
    with open(local_filename, mode='r') as file:
        render = csv.reader(file)
        lookup = {
            row[0]: row[1].split(';') for row in render if row}
    return lookup

class Rule:
    Node = None
    Adjacent = None

    def __init__(self, node, adjacent):
        if node < adjacent:
            node, adjacent = adjacent, node
        self.Node = node
        self.Adjacent = adjacent

    def __eq__(self, other):
        return self.Node == other.Node and \
            self.Adjacent == other.Adjacent

    def __hash__(self):
        return hash(self.Node) * 397 ^ hash(self.Adjacent)

    def __str__(self):
        return self.Node + " -> " + self.Adjacent

def build_rules(items):
    rules_added = {}
    for state, adjacent in items.items():
        for adjacent_state in adjacent:
            if adjacent_state == '': continue
            rule = Rule(state, adjacent_state)
            if rule in rules_added:
                rules_added[rule] += 1
            else:
                rules_added[rule] = 1

    for k, v in rules_added.items():
        if v != 2:
            print(f"rule {k} is not bidirectional")

    return rules_added.keys()
