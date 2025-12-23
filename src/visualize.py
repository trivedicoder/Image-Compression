import os
import matplotlib.pyplot as plt


def show(original, baseline, ga, save_path=None):
    """
    Function that show the original image, baseline compressed image, and our GA compressed image.
    If a save_path is given, save the comparison there.
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

    # save figure
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    plt.show()
    plt.close()


def plot(history, save_path=None):
    """
    Function that plots SSIM history.
    If a save_path is given, save the comparison there.
    """

    plt.figure()
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("SSIM")
    plt.title("SSIM Over Generations")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    plt.show()
    plt.close()