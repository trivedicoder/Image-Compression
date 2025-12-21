import numpy as np
import random
from metrics import evaluate_metrics
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize


# --------------------
# SIMPLE COMPRESSION
# --------------------
def compress(image, factor):
    """
    Downsample image by taking every factor-th pixel
    """
    return image[::factor, ::factor]


# --------------------
# BASELINE
# --------------------
def baseline_reconstruct(compressed, original_shape):
    return resize(
        compressed,
        original_shape,
        preserve_range=True,
        anti_aliasing=False
    ).astype(np.uint8)


# --------------------
# MUTATION
# --------------------
def mutate(image, rate=0.02):
    out = image.copy()
    h, w = out.shape

    for i in range(h):
        for j in range(w):
            if random.random() < rate:
                out[i, j] = random.randint(0, 255)

    return out


# --------------------
# EVOLUTION
# --------------------
def evolve(target, compressed, generations=30, pop_size=20):
    baseline = baseline_reconstruct(compressed, target.shape)

    population = [mutate(baseline, 0.01) for _ in range(pop_size)]
    history = []

    for g in range(generations):
        scores = [
            ssim(ind, target, data_range=255)
            for ind in population
        ]

        best_index = scores.index(max(scores))
        best = population[best_index]
        history.append(scores[best_index])

        print(f"Gen {g+1}: SSIM = {scores[best_index]:.4f}")

        new_population = [best]  # elitism

        while len(new_population) < pop_size:
            parent = random.choice(population)
            child = mutate(parent)
            new_population.append(child)

        population = new_population

    return best, history
