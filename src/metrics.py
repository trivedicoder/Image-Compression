"""
metrics.py

This module implements some of the quality metric calculations. (INCLUDE WHAT METHOD)
These metrics will be used to measure the effectiveness of our image compression.

Course: COSC 3P71
Date Created: 2025-12-14
Last Modified: 2025-12-20
"""
# Dylan Section - these metrics will be used to tell if our image compression was effective or not

# imports
# built MSE function from scikit-learn
from sklearn.metrics import mean_squared_error
import cv2


def evaluate_fitness(individual, original_image):
    """
    Fitness evaluation function that utilizes sklearn built-in MSE function calculation.
    This function is one of the core functions utilized in the compression algorithm.

    Parameters:
        individual (numpy array): Numpy array with RGB values
        image: Original image

    Returns:
        float: Mean Squared Error between compressed and original image
    """

    # generate image from numpy array
    image = decode_individual(individual)

    # give two numpy arrays
    MSE = mean_squared_error(image, original_image)

    return MSE


def decode_individual(individual):
    """
    Function used to decode a numpy array of RGB values and generate a candidate 
    image(200x120 pixels). Function also resizes candidate image(2000x1200 pixels) for comparison.

    Parameters:
        individual (numpy array): Numpy array with RGB value

        Returns:
            image: image after generating and resizing image
    """

    # APPLY DECODING ALGORITHM
    # ONCE IMAGES ARE REPRESENTED, WE CAN COMPLETE THIS PART.
