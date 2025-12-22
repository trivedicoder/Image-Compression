from skimage.transform import resize
import numpy as np


def baseline_resize(original):
    """
    Function to resize original image into a smaller image.
    """

    small = resize(
        original,
        (120, 200, 3),
        preserve_range=True,
        anti_aliasing=False
    )
    return small.astype(np.uint8)
