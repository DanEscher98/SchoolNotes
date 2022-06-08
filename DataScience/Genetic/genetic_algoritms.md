---
author: Daniel Colin
title: Genetic Algorithms
---

## Fitness and Mutation Techniques

- Give partial credit in the fitness if possible
- The fitness function should return as fast as possible because we're
    going to call it potentially millions of times.
- Memetic Algorithms are capable of solving a wider range of problems
    than random-population-based *Genetic Algorithms* because they
    accelerate the search.

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

## Simulated Annealing

Simulated annealing (SA) is a probabilistic technique for
approximating the global optimum of a given function. Specifically, it
is a metaheuristic to approximate global optimization in a large
search space for an optimization problem. It is often used when the
search space is discrete (for example the traveling salesman problem,
the boolean satisfiability problem, protein structure prediction, and
job-shop scheduling). For problems where finding an approximate global
optimum is more important than finding a precise local optimum in a
fixed amount of time, simulated annealing may be preferable to exact
algorithms such as gradient descent or branch and bound. 

A metaheuristic is a higher-level procedure or heuristic designed to
find, generate, or select a heuristic (partial search algorithm) that
may provide a sufficiently good solution to an optimization problem,
especially with incomplete or imperfect information or limited
computation capacity. Metaheuristics sample a subset of
solutions which is otherwise too large to be completely enumerated or
otherwise explored.
