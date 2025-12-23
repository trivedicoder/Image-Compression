from ea_compression import evolve
from baseline import baseline_resize
from metrics import ssim_score


def run(original):
    """
    Runs a complete experimental comparison between the baseline method and the evolutionary algorithm (EA) compression approach.
    
    This function:
    1. Generates a baseline reconstruction using traditional resizing.
    2. Evolves a compressed representation using a genetic algorithm.
    3. Evaluates both approaches using SSIM.
    4. Returns results for visualization and further analysis.
    
    """

    # Generate baseline reconstruction (e.g., bilinear resizing)
    baseline = baseline_resize(original)
    # Run evolutionary algorithm to obtain the best compressed image
    best, history = evolve(original)

    # Evaluate and report perceptual similarity using SSIM
    print("Baseline SSIM:", ssim_score(baseline, original))
    print("EA SSIM:", ssim_score(best, original))

    return baseline, best, history