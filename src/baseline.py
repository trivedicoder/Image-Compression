import numpy as np
from skimage.transform import resize


def baseline_reconstruct(compressed, original_shape):
    """
    Baseline = resize compressed image back to original size
    """
    rec = resize(
        compressed,
        original_shape,
        preserve_range=True,
        anti_aliasing=False
    )
    return rec.astype(np.uint8)