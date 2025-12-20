"""
main.py

This module is the main execution script, where everything comes together: 
parameter controlling, running experiment, running main algorithm, etc.

Course: COSC 3P71
Date Created: 2025-12-14
Last Modified: 2025-12-19
"""

import cv2

# TESTING CV PYTHON IMAGES
# loading image
img = cv2.imread("Image-Compression/images/original/Peppers.jpg")

# showing image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
