
import numpy as np
import random
from skimage.transform import resize
from metrics import ssim_score


# ============================
# PARAMETERS
# ============================
# Dimensions of the compressed image
# These define the search space of the genetic algorithm
COMP_W = 200
COMP_H = 120


# ============================
# DECODE CHROMOSOME → IMAGE
# ============================
def decode(chrom, block_size, bx, by):
    """
    Helper for fitness function. Actual decoding logic.

    Decodes a chromosome into a compressed RGB image.

    Each chromosome stores average RGB values for fixed-size blocks. 
    The decoding process reconstructs a low-resolution image by filling each block with its corresponding RGB gene values.
    """

    # Initialize compressed image
    img = np.zeros((COMP_H, COMP_W, 3), dtype=np.uint8)
    idx = 0 # Pointer 

    # Fill block with its corresponding RGB values
    for y in range(by):
        for x in range(bx):
            img[
                y*block_size:(y+1)*block_size,
                x*block_size:(x+1)*block_size
            ] = chrom[idx:idx+3]
            idx += 3

    return img


# ============================
# FITNESS FUNCTION (SSIM)
# ============================
def fitness(chrom, original, block_size, bx, by):
    """
    A fitness function that decodes a chromosome into a picture and evaluates its fitness.

    The chromosome is decoded into a compressed image, resized back to the original resolution, and evaluated using SSIM.
    SSIM is used as the fitness measure because it correlates better with human visual perception than pixel-wise error metrics.
    """

    # Decode chromosome into compressed image
    compressed = decode(chrom, block_size, bx, by)

    # Resize compressed image back to original resolution
    reconstructed = resize(
        compressed,
        original.shape,
        preserve_range=True,
        anti_aliasing=False
    ).astype(np.uint8)

    # Compute SSIM fitness score -> Closer to 1 the better
    return ssim_score(original, reconstructed)


# ============================
# INITIAL POPULATION
# ============================
def init_population(original, pop_size, block_size, bx, by, genes):
    """
    Function that creates an initial population.

    The base chromosome is created by computing the mean colour of each block in a downsampled version of the original image.
    Slight random noise is added to introduce diversity.
    """

    # Downsample original image to compressed resolution
    small = resize(
        original,
        (COMP_H, COMP_W, 3),
        preserve_range=True,
        anti_aliasing=False
    ).astype(np.uint8)

    # Create base chromosome from block averages
    base = []
    for y in range(by):
        for x in range(bx):
            block = small[
                y*block_size:(y+1)*block_size,
                x*block_size:(x+1)*block_size
            ]
            base.extend(block.mean(axis=(0, 1)).astype(int))

    base = np.array(base, dtype=np.uint8)

    # Generate population by adding small random noise
    population = []
    for _ in range(pop_size):
        noise = np.random.randint(-5, 6, genes)
        individual = np.clip(base + noise, 0, 255)
        population.append(individual.astype(np.uint8))

    return population


# ============================
# GENETIC ALGORITHM
# ============================
def evolve(original, generations=50, pop_size=30, mutation_rate=0.01, block_size=4, progress_callback=None):
    """
    Implementation of our Genetic Algorithm. Evolve compressed image representations. 
    
    The algorithm uses:
    - SSIM as the fitness function
    - Truncation selection (top 50%)
    - Single-point crossover
    - Random mutation
    
    """

    # Compute chromosome dimensions
    bx = COMP_W // block_size
    by = COMP_H // block_size
    genes = bx * by * 3 # RGB values per block

    # Initialize population
    population = init_population(original, pop_size, block_size, bx, by, genes)
    history = []

    # Evolution loop
    for gen in range(generations):

        # Evaluate fitness of population
        scores = [fitness(ind, original, block_size, bx, by)
                  for ind in population]

        # Save best score
        best_score = max(scores)
        history.append(best_score)

        print(f"Generation {gen + 1}: Best SSIM = {best_score:.4f}")

        # Update progress callback
        if progress_callback:
            percent = int((gen + 1) / generations * 100)
            progress_callback(percent, f"Generation {gen + 1} / {generations}") # Update progress bar

        # Selection (keep top 50%)
        sorted_idx = np.argsort(scores)[::-1]
        survivors = [population[i] for i in sorted_idx[:pop_size // 2]]

        # Reproduction
        new_population = survivors.copy()
        while len(new_population) < pop_size:
            p1, p2 = random.sample(survivors, 2)
            cp = random.randint(0, genes - 1)

            # Single-point crossover
            child = np.concatenate((p1[:cp], p2[cp:]))

            # Mutation
            for i in range(genes):
                if random.random() < mutation_rate:
                    child[i] = random.randint(0, 255)

            new_population.append(child.astype(np.uint8))

        population = new_population

    #  # Select final best individual
    final_scores = [fitness(ind, original, block_size, bx, by)
                    for ind in population]
    best_idx = np.argmax(final_scores)

    return decode(population[best_idx], block_size, bx, by), history
