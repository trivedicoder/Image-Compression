import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from ea_compression import evolve
from metrics import evaluate_metrics
from baseline import baseline_resize
from visualize import show, plot

from gui import pick_images


def load_image(path):
    """
    Load single image from a given file path.
    """

    img = Image.open(path).convert("RGB")
    return np.array(img)


def main():
    """
    Main script that implements all core parts of the code.
    """

    # get images and check for selection
    paths = pick_images(multiple=True)
    if not paths:
        print("Selection failed, quitting program")
        return

    # loop through all images selected
    for path in paths:
        print(f"Applying EA to: {path}")

        original = load_image(path)

        ga, history = evolve(original)

        # Bilinear baseline reconstruction
        baseline = baseline_resize(original)

        # Compute metrics
        b_ssim, b_mse, b_psnr = evaluate_metrics(original, baseline)
        ea_ssim, ea_mse, ea_psnr = evaluate_metrics(original, ga)

        # Print results
        print("Bilinear Baseline:")
        print(f"SSIM: {b_ssim:.4f}, MSE: {b_mse:.2f}, PSNR: {b_psnr:.2f}")

        print("\nEA Result:")
        print(f"SSIM: {ea_ssim:.4f}, MSE: {ea_mse:.2f}, PSNR: {ea_psnr:.2f}")

        print("Printing is done")

        # Visualization
        show(original, baseline, ga)
        print("Plot is done")
        plot(history)


# run script
main()
