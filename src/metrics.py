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

# Structural similarity index measure
def ssim_score(a, b):

    return ssim(a, b, data_range=255)

# This is my section here Dylan.T.Z 

def evaluate_metrics (orig, compress): 
    upscaled = cv2.resize {
        compress, 
        (orig.shape[1], orig.shape[0]),
        interpolation=cv2.INTER_CUBIC # Interpolation 
     }

ssim_value = ssim(orig, upscaled, channel_axis=2)
mse_value = mean_squared_error(orig, upscaled)
psnr_value = peak_signal_noise_ratio(orig, upscaled, data_range=255)
return ssim_value, mse_value, psnr_value
    
# We implemented image quality evaluation metrics (SSIM, MSE, PSNR) in a standalone module (metrics.py) using scikit-image. 
# These metrics were integrated into the fitness function of the AI compression algorithm and used to track optimization performance over successive generations.”



