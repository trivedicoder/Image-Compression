import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio


def ssim_score(a, b):
    """
    Compute the Structural Similarity Index Measure (SSIM) score between two images.

    SSIM is a perceptual metric that measures similarity based on luminance, contrast, and structural information. 
    Making it more aligned with human visual perception than pixel-wise error metrics.
    """
    return ssim(a, b, channel_axis=2, data_range=255)


def evaluate_metrics(orig, compress):
    """
    A function that upscales the compressed image and evaluates image quality using metrics such as SSIM, MSE, and PSNR.lol
    """

    # Upscale image to match original resolution
    upscaled = cv2.resize(
        compress,
        (orig.shape[1], orig.shape[0]),
        interpolation=cv2.INTER_CUBIC  # Interpolation
    )

    # Compute perceptual and error-based metrics
    ssim_value = ssim(orig, upscaled, channel_axis=2, data_range=255)
    mse_value = mean_squared_error(orig, upscaled)
    psnr_value = peak_signal_noise_ratio(orig, upscaled, data_range=255)
    return ssim_value, mse_value, psnr_value

# We implemented image quality evaluation metrics (SSIM, MSE, and PSNR) in a standalone module using scikit-image to promote modularity and reuse across experiments.

# SSIM was selected as the primary fitness function for the evolutionary algorithm because it better captures perceptual image quality compared to traditional pixel-wise error measures.

# MSE and PSNR were computed alongside SSIM for evaluation and baseline comparison purposes, but were not used directly in the optimization objective.
