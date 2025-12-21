import numpy as np
from PIL import Image
from ea_compression import evolve
from baseline import baseline_resize
from visualize import show


img = Image.open("/Users/aryamac/Desktop/Image-Compression/images/original/Peppers.jpg").convert("RGB")
original = np.array(img)

ga = evolve(original)
baseline = baseline_resize(original)

show(original,baseline, ga)


    # Baseline Comparison #
#
# # Bilinear baseline reconstruction
# baseline = baseline_reconstruct(compressed, target.shape)

# # Compute metrics
# b_ssim, b_mse, b_psnr = evaluate_metrics(target, baseline)
# ea_ssim, ea_mse, ea_psnr = evaluate_metrics(target, best)
#
# # Print results
# print("Bilinear Baseline:")
# print(f"SSIM: {b_ssim:.4f}, MSE: {b_mse:.2f}, PSNR: {b_psnr:.2f}")
#
# print("\nEA Result:")
# print(f"SSIM: {ea_ssim:.4f}, MSE: {ea_mse:.2f}, PSNR: {ea_psnr:.2f}")
#
# # Visualization #
# show(target, baseline, best)
# plot(history)
