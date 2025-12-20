import numpy as np
from skimage.metrics import structural_similarity as ssim


def mse(a, b):
    return np.mean((a.astype(float) - b.astype(float)) ** 2)


def psnr(a, b):
    m = mse(a, b)
    if m == 0:
        return float("inf")
    return 10 * np.log10(255 * 255 / m)


def ssim_score(a, b):
    return ssim(a, b, data_range=255)