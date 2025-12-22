# Image Compression using Genetic Algorithms

## Overview
This project implements an image compression algorithm using an evolutionary algorithm approach.
Images are compressed using block-based encoding, and the algorithm evolves the compressed
representation to increase visual similarity as much as possible after reconstruction.

## Installation Instructions

### Clone the repository

run the following commands on the terminal:

1) git clone https://github.com/trivedicoder/Image-Compression.git
2) cd Image-Compression 

##  Dependencies and requirements

required libraries:
    - numpy
    - tkinter
    - matplotlib
    - scikit-image
    - pillow
    - opencv-python

to install libraries, just run the following command on the terminal:

pip install numpy pillow matplotlib scikit-image opencv-python

## How to run the code

Assuming you are in the project's root directory, run this command on terminal:

python src/main.py

1) A GUI will open and let you select image files (multiple files supported).
2) After selecting images, another GUI will open and you will be asked to select a compression rate (low, medium, or high).
    - Must select compression rate for each image.
3) After that, the evolutionary algorithm will run on each selected image.
4) Results are printed to the console.
5) Output images and plots are displayed.

## File Structure
''' bash
Image-Compression/
│
├── images/
│   └── original/          # Input images
│
├── results/
│    └── compressed/       # Comparison charts
│    └── plots/            # Plots generated
│
├── src/
│   ├── main.py            # Main script
│   ├── ea_compression.py  # Genetic Algorithm implementation
│   ├── baseline.py        # Baseline bilinear compression
│   ├── metrics.py         # SSIM, MSE, PSNR metrics
│   ├── visualize.py       # Image display and plotting
│   └── gui.py             # GUI file picker and compression selector
│
├── README.md              # Project documentation
├── .gitignore
'''