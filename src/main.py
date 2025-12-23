import numpy as np

from PIL import Image
from ea_compression import evolve
from metrics import evaluate_metrics
from baseline import baseline_resize
from visualize import show, plot

from gui import pick_images, choose_compression, progresswindow
import os


def load_image(path):
    """
    Load single image from a given file path.
    """

    img = Image.open(path).convert("RGB")
    return np.array(img)


def main():
    """
    Main script that implements all core parts of the code.lol
    """

    # get images and check for selection
    paths = pick_images(multiple=True)
    if not paths:
        print("Selection failed, quitting program")
        return

    # create directories to save results
    project_root = os.path.dirname(os.path.dirname(__file__))

    compressed_dir = os.path.join(project_root, "results", "compressed")
    plots_dir = os.path.join(project_root, "results", "plots")

    os.makedirs(compressed_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

    # loop through all images selected
    for path in paths:
        print(f"Applying EA to: {path}")

        original = load_image(path)

        # let user pick compression level
        block_size = choose_compression()

        # get image file name without format (JPG)
        img_name = os.path.splitext(os.path.basename(path))[0]

        # generate some file names and paths
        comparison_path = os.path.join(
            compressed_dir, f"{img_name}_comparison.png")
        plot_path = os.path.join(plots_dir, f"{img_name}_ssim.png")
        metrics_path = os.path.join(
            project_root, "results", f"{img_name}_metrics.txt")

        update_progress, close_progress = progresswindow()          # create progress bar window

        ga, history = evolve(original, block_size=block_size, progress_callback=update_progress)   # orginal: 100 generations, block_size=4,  progress callback is updating the progress bar
        close_progress()                    # close the progress bar when done

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

        # save metrics to a text file
        with open(metrics_path, "w") as f:
            f.write("Bilinear Baseline:\n")
            f.write(
                f"SSIM: {b_ssim:.4f}, MSE: {b_mse:.2f}, PSNR: {b_psnr:.2f}\n\n")
            f.write("EA Result:\n")
            f.write(
                f"SSIM: {ea_ssim:.4f}, MSE: {ea_mse:.2f}, PSNR: {ea_psnr:.2f}\n")

        print("Printing is done")

        # Visualization
        show(original, baseline, ga, save_path=comparison_path)
        print("Plot is done")
        plot(history, save_path=plot_path)


# run script
main()