import os
import matplotlib.pyplot as plt


def show(original, baseline, ga, save_path=None):
    """
    Displays a side-by-side visual comparison of:
    1. The original image
    2. The baseline reconstruction
    3. The image produced by the genetic algorithm (GA)

    This visualization allows for qualitative comparison of perceptual
    image quality across methods. Optionally, the figure can be saved
    to disk for inclusion in reports or presentations.
    """

    # Create a figure with three subplots arranged horizontally
    plt.figure(figsize=(10, 4))

    # Display original image
    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(original)
    plt.axis("off")

    # Display baseline reconstruction
    plt.subplot(1, 3, 2)
    plt.title("Baseline")
    plt.imshow(baseline)
    plt.axis("off")

    # Display GA reconstruction
    plt.subplot(1, 3, 3)
    plt.title("GA Compressed")
    plt.imshow(ga)
    plt.axis("off")

    # Save figure to disk if a save path is provided.
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    # Render figure and release resources
    plt.show()
    plt.close()


def plot(history, save_path=None):
    """
    Plots the SSIM fitness values over generations during the evolutionary optimization process.

    This plot provides insight into the convergence behaviour of he genetic algorithm and highlights whether perceptual image quality improves over time.
    """

    # Create a line plot of SSIM over generations
    plt.figure()
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("SSIM")
    plt.title("SSIM Over Generations")

    # Save plot if requested,
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    # Display plot and clean up
    plt.show()
    plt.close()

