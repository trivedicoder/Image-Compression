"""
compression.py

This module is the main compression algorithm implementation. It's a mixed
approach that uses an evolutionary block-based approach.

Course: COSC 3P71
Date Created: 2025-12-14
Last Modified: 2025-12-19
"""

"""
LEAVING THIS PSEUDO CODE FROM SLIDES FOR REFERENCE. JUST FOR NOW.

A General Simple GA

BEGIN
    i=0 set generation number to zero
    initpopulation P(0) INITIALIZE usually random population of individuals representing candidate solution
    evaluate P(0) EVALUATE fitness of all initial individuals of population
    
    while (not done) do test for termination criterion (time, fitness, etc)
    begin
        i = i + 1 increase the generation number
        select P(i) from SELECT a sub-population for offspring
        P(i-1) reproduction
        recombine P(i) RECOMBINE the genes of pairs of selected parents
        mutate P(i) MUTATED perturb the mated population (i.e., resulting
        offspring)
        evaluate P(i) EVALUATE the new individuals
    end
END
"""

"""
IMAGE REPRESENTATION NOTES:

image encoding: (that's what I think should happen/idea)
    an 'image' will be a numpy array of RGB numbers (0-255)


"""


# DEFINE CONSTANTS-----------------------------------------------------------------------
import metrics
WIDTH = 200  # image px width
HEIGHT = 120  # image px height

# 3 RGB values for each block (3 x 375 = 1175 values per array)
CHROM_LEN = 1125

BLOCK_SIZE = 8       # 8x8 pixel blocks
WIDTH_BLOCKS = 25    # (200 / 8 = 25)
HEIGHT_BLOCKS = 15   # (120 / 8 = 15)

# GA parameters, probably don't need to change cx and mut rates, but i will leave it here
CROSS_RATE = 0.9
MUT_RATE = 0.1
MAX_GEN = 50
POP_SIZE = 100


# IMPLEMENT GA ALGORITHM------------------------------------------------------------------
def genetic_algorithm():
    """
    This is the main block-based GA.

    Returns:
        not too sure yet
    """
    # generate random population, initial population
    population = generate_population()
    fitness_values = [0] * len(population)
    gen_num = 0

    # compute fitness of initial population
    for chromosome in population:
        fitness = metrics.evaluate_fitness(chromosome)
        fitness_values.append(fitness)

    while (gen_num < MAX_GEN):
        # increase generation number
        gen_num += 1

        # select from population
        new_population = tournament_selection(population)

        # reproduce population
        new_population = crossover_method(new_population)

        # mutate population
        new_population = mutation_method(new_population)

        # evaluate fitness of new individuals
        new_fitness = metrics.evaluate_fitness(new_population)


def generate_population():
    """
    Helper function that generates an initial population of random values. 
    Each chromosome is a numpy array of size 1125, which contains R, G, and B
    values between [0-255].

    Parameters:
        FILL THIS

    Returns:
        FILL THIS 
    """

    # each block get initialized with random R,G, and B channels

    return None


def tournament_selection():
    return None


def crossover_method():
    return None


def mutation_method():
    return None
