import os
import matplotlib.pyplot as plt


def show(original, baseline, ga):
    """
    Function that displays the original image, baseline compressed image, and our GA compressed image
    """
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(original)
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Baseline")
    plt.imshow(baseline)
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("GA Compressed")
    plt.imshow(ga)
    plt.axis("off")

    plt.show()


def plot(history):
    """
    Function that creates a chart saves it to figures
    """

    # Creating a NEW chart in the NEW folder CALLED "figures" to track the SSIM
    os.makedirs("figures", exist_ok=True)

    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("SSIM")
    plt.title("SSIM Over Generations")
    plt.savefig("figures/ssim_plot.png")

    plt.show()
