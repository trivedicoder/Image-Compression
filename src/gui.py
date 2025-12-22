import tkinter as tk
from tkinter import filedialog, messagebox


def pick_images(multiple: True):
    """
    Function that implements GUI (advanced feature 1). 
    GUI supports multiple files, which is also considered an advanced feature.
    """

    root = tk.Tk()

    # select multiple images
    if multiple:
        paths = filedialog.askopenfilenames(
            title="Select image(s)",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff *.webp")]
        )

        if paths:
            selected = list(paths)
        else:
            selected = []

    # select only one image
    else:

        path = filedialog.askopenfilename(
            title="Select image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff *.webp")]
        )

        if path:
            selected = [path]
        else:
            selected = []

    root.destroy()  # get rid of GUI

    # if image selection failed, display message to user
    if not selected:
        messagebox.showinfo("Selection failed", "No image was selected. ")

    return selected
