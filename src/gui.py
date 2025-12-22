import tkinter as tk
from tkinter import filedialog, messagebox


def pick_images(multiple: True):
    """
    Function that implements a GUI (advanced feature 1). This GUI is a file picker. 
    It supports multiple files, which is also considered an advanced feature.
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


def choose_compression():
    """
    Function that implements another GUI. The GUI allows user to select compression
    level for each image (low, medium, or high).
    """

    # map levels to block size
    levels = {"low": 2, "medium": 4, "high": 5}

    root = tk.Tk()
    root.title("Compression Setting")

    # default value in case user hits ok button without selecting anything
    choice = tk.StringVar(value="medium")

    tk.Label(root, text="Choose compression setting:").pack()

    # show level buttons
    for level in levels:
        tk.Radiobutton(
            root,
            text=f"{level}",
            variable=choice,
            value=level
        ).pack()

    result = {"block": levels["medium"]}

    # change compression level and get rid of GUI after user hits ok
    def on_ok():
        result["block"] = levels[choice.get()]
        root.destroy()

    tk.Button(root, text="OK", command=on_ok).pack()

    root.mainloop()
    return result["block"]
