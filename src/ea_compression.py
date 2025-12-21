import numpy as np
import random
from skimage.transform import resize
from metrics import ssim_score


# ============================
# PARAMETERS (from PDF)
# ============================
COMP_W = 200  # Compressed width
COMP_H = 120  # Compressed height
BLOCK = 5     # Block size
BX = COMP_W // BLOCK  # Blocks in x
BY = COMP_H // BLOCK  # Blocks in y
GENES = BX * BY * 3   # Total genes in chromosome


# ============================
# CHROMOSOME → IMAGE
# ============================
def decode(chrom):
    """
    Convert chromosome to compressed image
    """
    small = np.zeros((COMP_H, COMP_W, 3), dtype=np.uint8)

    idx = 0
    for y in range(BY):
        for x in range(BX):
            r = chrom[idx]
            g = chrom[idx + 1]
            b = chrom[idx + 2]
            small[
                y*BLOCK:(y+1)*BLOCK,
                x*BLOCK:(x+1)*BLOCK
            ] = [r, g, b]
            idx += 3

    return small


# ============================
# FITNESS (SSIM)
# ============================
def fitness(chrom, original):
    """
    Fitness function: SSIM between original and reconstructed image
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
    Start population near block-average image
    """
    # Downsample original image
    small = resize(
        original,
        (COMP_H, COMP_W, 3),
        preserve_range=True,
        anti_aliasing=False
    ).astype(np.uint8)

    # Build base chromosome
    base = []
    for by in range(BY):
        for bx in range(BX):
            block = small[
                by*BLOCK:(by+1)*BLOCK,
                bx*BLOCK:(bx+1)*BLOCK
            ]
            r = int(np.mean(block[:, :, 0]))
            g = int(np.mean(block[:, :, 1]))
            b = int(np.mean(block[:, :, 2]))
            base.extend([r, g, b])
    base = np.array(base, dtype=np.uint8)

    # Create population with small noise
    population = []
    for _ in range(pop_size):
        individual = base + np.random.randint(-5, 6, size=GENES)
        individual = np.clip(individual, 0, 255)
        population.append(individual.astype(np.uint8))
    return population


# ============================
# GENETIC ALGORITHM
# ============================
def evolve(original, generations=50, pop_size=30, mutation_rate=0.01):
    population = init_population(original, pop_size)

    for gen in range(generations):
        # Evaluate fitness
        scores = [fitness(ind, original) for ind in population]

        # Select best individuals
        sorted_indices = np.argsort(scores)[::-1]
        population = [population[i] for i in sorted_indices[:pop_size//2]]

        # Create new individuals through crossover and mutation
        new_population = population.copy()
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(population, 2)
            crossover_point = random.randint(0, GENES - 1)
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))

            # Mutation
            for i in range(GENES):
                if random.random() < mutation_rate:
                    child[i] = random.randint(0, 255)

            new_population.append(child.astype(np.uint8))

        population = new_population

        # Print best score of the generation
        best_score = max(scores)
        print(f"Generation {gen + 1}: Best SSIM = {best_score:.4f}")

    # Return the best individual from the final population
    final_scores = [fitness(ind, original) for ind in population]
    best_index = np.argmax(final_scores)
    return decode(population[best_index])