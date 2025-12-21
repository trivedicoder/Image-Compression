import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from ea_compression import compress, evolve

import tkinter as tk
from tkinter import filedialog
import os

# function to select image


# def select_image(start_dir=None):
"""
    This function implements one of the advanced features, which is a GUI for selecting an image
    """

# root = tk.Tk()
# root.title("GUI for selecting image")

# if start_dir == None:
# get current working directory, so we know where images are
# start_dir = os.getcdw()

# return None


# LOAD IMAGE
# have to specify image path for now, but once GUI is implemented, we shouldn't need to
img = Image.open("Image-Compression/images/original/Peppers.jpg").convert("L")
target = np.array(img)

# COMPRESS
COMPRESSION_SETTINGS = {
    "low": 2,
    "medium": 4,
    "high": 8
}

# User-Defined compression level, which maps low, medium, and high to different compression levels.
compression_level = "high"
factor = COMPRESSION_SETTINGS[compression_level]
compressed = compress(target, factor)

# EVOLVE
best, history = evolve(target, compressed)

# from metrics import evaluate_metrics

# ssim_value, mse_value, psnr_value = evaluate_metrics(target, candidate)
# fitness = ssim_value
# history.append(ssim_value)
# metrics evaluation code in main.py would take the SSIM fitness value and story that in history, for our visualization code to use. IDK maybe it's more efficent


# SHOW RESULT

plt.figure(figsize=(6, 3))

plt.subplot(1, 2, 1)
plt.title("Target")
plt.imshow(target, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("EA Result")
plt.imshow(best, cmap="gray")
plt.axis("off")

plt.show()

# Baseline Comparison #

# Bilinear baseline reconstruction
baseline = baseline_reconstruct(compressed, target.shape)

# Compute metrics
b_ssim, b_mse, b_psnr = evaluate_metrics(target, baseline)
ea_ssim, ea_mse, ea_psnr = evaluate_metrics(target, best)

# Print results
print("Bilinear Baseline:")
print(f"SSIM: {b_ssim:.4f}, MSE: {b_mse:.2f}, PSNR: {b_psnr:.2f}")

print("\nEA Result:")
print(f"SSIM: {ea_ssim:.4f}, MSE: {ea_mse:.2f}, PSNR: {ea_psnr:.2f}")

# Visualization #
show(target, baseline, best)
plot(history)
