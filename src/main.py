import numpy as np
from PIL import Image

from ea_compression import compress, evolve


# LOAD IMAGE
img = Image.open("image.png").convert("L")
target = np.array(img)

# COMPRESS
compressed = compress(target)

# EVOLVE
best, history = evolve(target, compressed)

# SHOW RESULT
import matplotlib.pyplot as plt

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