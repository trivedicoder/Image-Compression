import os
import matplotlib.pyplot as plt


def show(original,baseline, ga):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(original)
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Baseline")
    plt.imshow(baseline)
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("GA Compressed")
    plt.imshow(ga)
    plt.axis("off")

    plt.show()

def plot(history):
    os.makedirs("figures", exist_ok=True)# Creating a NEW chart in the NEW folder CALLED "figures" to track the SSIM
   
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("SSIM")
    plt.title("SSIM Over Generations")
    plt.savefig("figures/ssim_plot.png")
    
    plt.show()



    #Lol lmao

