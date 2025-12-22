import numpy as np
import random
from skimage.transform import resize
from metrics import ssim_score


# ============================
# PARAMETERS
# ============================
COMP_W = 200
COMP_H = 120
BLOCK = 5

BX = COMP_W // BLOCK
BY = COMP_H // BLOCK
GENES = BX * BY * 3


# ============================
# DECODE CHROMOSOME → IMAGE
# ============================
def decode(chrom):
    """
    Helper for fitness function. Actual decoding logic.
    """
    img = np.zeros((COMP_H, COMP_W, 3), dtype=np.uint8)
    idx = 0

    for y in range(BY):
        for x in range(BX):
            img[
                y*BLOCK:(y+1)*BLOCK,
                x*BLOCK:(x+1)*BLOCK
            ] = chrom[idx:idx+3]
            idx += 3

    return img


# ============================
# FITNESS FUNCTION (SSIM)
# ============================
def fitness(chrom, original):
    """
    Fitness function that decodes a chromosome into a picture and evaluates its fitness.
    """
    compressed = decode(chrom)

    reconstructed = resize(
        compressed,
        original.shape,
        preserve_range=True,
        anti_aliasing=False
    ).astype(np.uint8)

    return ssim_score(original, reconstructed)


# ============================
# INITIAL POPULATION
# ============================
def init_population(original, pop_size):
    """
    Function that creates an initial population.
    """
    small = resize(
        original,
        (COMP_H, COMP_W, 3),
        preserve_range=True,
        anti_aliasing=False
    ).astype(np.uint8)

    base = []
    for y in range(BY):
        for x in range(BX):
            block = small[
                y*BLOCK:(y+1)*BLOCK,
                x*BLOCK:(x+1)*BLOCK
            ]
            base.extend(block.mean(axis=(0, 1)).astype(int))

    base = np.array(base, dtype=np.uint8)

    population = []
    for _ in range(pop_size):
        noise = np.random.randint(-5, 6, GENES)
        individual = np.clip(base + noise, 0, 255)
        population.append(individual.astype(np.uint8))

    return population


# ============================
# GENETIC ALGORITHM
# ============================
def evolve(original, generations=50, pop_size=30, mutation_rate=0.01):
    """
    Implementation of our Genetic Algorithm.
    """
    population = init_population(original, pop_size)
    history = []

    for gen in range(generations):
        scores = [fitness(ind, original) for ind in population]

        # Save best score
        best_score = max(scores)
        history.append(best_score)

        print(f"Generation {gen + 1}: Best SSIM = {best_score:.4f}")

        # Selection (top 50%)
        sorted_idx = np.argsort(scores)[::-1]
        survivors = [population[i] for i in sorted_idx[:pop_size // 2]]

        # Reproduction
        new_population = survivors.copy()
        while len(new_population) < pop_size:
            p1, p2 = random.sample(survivors, 2)
            cp = random.randint(0, GENES - 1)

            child = np.concatenate((p1[:cp], p2[cp:]))

            # Mutation
            for i in range(GENES):
                if random.random() < mutation_rate:
                    child[i] = random.randint(0, 255)

            new_population.append(child.astype(np.uint8))

        population = new_population

    # Final best individual
    final_scores = [fitness(ind, original) for ind in population]
    best_idx = np.argmax(final_scores)

    return decode(population[best_idx]), history
