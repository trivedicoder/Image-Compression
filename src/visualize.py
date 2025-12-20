import matplotlib.pyplot as plt


def show(target, baseline, best):
    plt.figure(figsize=(9, 3))

    plt.subplot(1, 3, 1)
    plt.title("Target")
    plt.imshow(target, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Baseline")
    plt.imshow(baseline, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("EA Result")
    plt.imshow(best, cmap="gray")
    plt.axis("off")

    plt.show()


def plot(history):
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("SSIM")
    plt.show()