---
author: Daniel Colin
title: Genetic Algorithms
---

## Fitness Techniques

- Give partial credit in the fitness if possible
- The fitness function should return as fast as possible because we're
    going to call it potentially millions of times.

## Glossary

- **Genotype**: is the way the parts of the problem are encoded so
    they can be manipulated by the genetic algorithm
- **Phenotype**: is how the decoded genes are used in solving the
    problem.
- The **fitness function** evaluates the Phenotype in the context of
    the problem being solved to return a fitness value to the
    algorithm.

## Algorithm

```haskell
data Fitness = Fitness Int
    deriving (Show, Eq)

data Chromosome a = G [a] Fitness
```

```python
# Basic implementation
generate_parent(length, geneset) -> Chromosome
mutate(parent, geneset) -> Chromosome:
    """Change one gene from parent by a random one from genes."""

# Main Loop
parent = generate_parent(length, geneset)
while optimal_fitness > fitness(parent):
    child = mutate(child, geneset)
    if not fitness(child) > fitness(parent):
        parent = child
```


