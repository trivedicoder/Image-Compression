from ea_compression import compress, evolve
from baseline import baseline_reconstruct
from metrics import ssim_score


def run_experiment(image):
    compressed = compress(image)
    baseline = baseline_reconstruct(compressed, image.shape)

    best, history = evolve(image, compressed)

    print("Baseline SSIM:", ssim_score(baseline, image))
    print("EA SSIM:", ssim_score(best, image))