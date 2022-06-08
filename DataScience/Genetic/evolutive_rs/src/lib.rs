struct Chromosome<G, F> {
    genes: G,
    fitness: F,
    mutations: u64,
    age: u64,
}

impl Chromosome<G, F> {
    fn new() -> Self {
        Chromosome {

        }
    }
    fn mutate(self, get_fitness: Fn(G) -> F, mutation: Fn(G) -> G) -> Self {
        Chromosome {
            genes: mutation(self.genes),
            fitness: get_fitness(self.genes),
            mutations: self.mutations + 1,
            age: self.age + 1
        }
    }
}

struct Species<G, T> {
    gene_set: Option<G>,
    lenght: u64,
    optimal: F,
    max_age: Option<i64>,
    custom_mutation: Option<Fn()
}

// clear
trait Species<F, G> {
    fn new(gen_set: Option<G>, lenght: u64, optimal: F, max_age: Option<i64>) -> Species<G, T>;
    fn get_fitness<F>(self) -> F;
}

fn get_best(specie: Species<F, G>) {
    match specie.
}

trait Fitness<F> {}
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
