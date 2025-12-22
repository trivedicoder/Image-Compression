import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio


def ssim_score(a, b):
    """
    Compute Structural similarity index measure (SSIM) score.
    """
    return ssim(a, b, channel_axis=2, data_range=255)


def evaluate_metrics(orig, compress):
    """
    Function that upscales the compressed image and computes metrics such as SSIM, MSE, PSNR.
    """

    # upscale image
    upscaled = cv2.resize(
        compress,
        (orig.shape[1], orig.shape[0]),
        interpolation=cv2.INTER_CUBIC  # Interpolation
    )

    ssim_value = ssim(orig, upscaled, channel_axis=2, data_range=255)
    mse_value = mean_squared_error(orig, upscaled)
    psnr_value = peak_signal_noise_ratio(orig, upscaled, data_range=255)
    return ssim_value, mse_value, psnr_value

# We implemented image quality evaluation metrics (SSIM, MSE, PSNR) in a standalone module (metrics.py) using scikit-image.
# These metrics were integrated into the fitness function of the AI compression algorithm and used to track optimization performance over successive generations.”

# We used SSIM as the primary fitness function because it more closely reflects perceptual image quality.
# MSE and PSNR were computed alongside SSIM for evaluation and baseline comparison but were not used directly in the optimization objective
