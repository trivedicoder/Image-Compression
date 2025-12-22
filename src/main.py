import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from ea_compression import evolve
from metrics import evaluate_metrics
from baseline import baseline_resize
from visualize import show, plot

# LOAD IMAGE
print("Loading image")
img = Image.open("/Users/aryamac/Desktop/Image-Compression/images/original/Peppers.jpg").convert("RGB")
original = np.array(img)

ga, history = evolve(original)
baseline = baseline_resize(original)

show(original,baseline, ga)

print("Starting the Bilinear Baseline ")
    # Baseline Comparison # 

# Bilinear baseline reconstruction
baseline = baseline_resize(original)

# Compute metrics
b_ssim, b_mse, b_psnr = evaluate_metrics(original, baseline)
ea_ssim, ea_mse, ea_psnr = evaluate_metrics(original, ga)

# Print results
print("Bilinear Baseline:")
print(f"SSIM: {b_ssim:.4f}, MSE: {b_mse:.2f}, PSNR: {b_psnr:.2f}")

print("\nEA Result:")
print(f"SSIM: {ea_ssim:.4f}, MSE: {ea_mse:.2f}, PSNR: {ea_psnr:.2f}")

print("Printing is done")

# Visualization #
show(original, baseline, ga)
print("Plot is done")
plot(history)
#Lol
