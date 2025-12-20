import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio

def mse(a, b):
    return np.mean((a.astype(float) - b.astype(float)) ** 2)


def psnr(a, b):
    m = mse(a, b)
    if m == 0:
        return float("inf")
    return 10 * np.log10(255 * 255 / m)


def ssim_score(a, b):

    return ssim(a, b, data_range=255)

# This is my section here Dylan.T.Z 


def evaluate_metrics (orig, compress): 
    upscaled = cv2.resize

