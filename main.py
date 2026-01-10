from tkinter import *
from tkinter import ttk
# loading Python Imaging Library
from PIL import ImageTk, Image

from os import remove, makedirs, listdir
from shutil import rmtree

from image_processor import render_frame

def open_img(imagepath, panel: Label):
    # opens the image
    img = Image.open(imagepath)
    
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((640, 360), Image.LANCZOS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # set the image as img
    panel.image = img
    panel.configure(image=img)

def play_images(root, image_folder, panel):
    for file in listdir(image_folder):
        output_image_path = render_frame(
            source_img_path=f"{image_folder}/{file}"
        )
        open_img(
            imagepath=output_image_path,
            panel=panel
        )
        root.update()

def main():
    # Create a window
    root = Tk()

    # Set Title as Image Loader
    root.title("Image Loader")

    # Set the resolution of window
    root.geometry("1280x720+640+360")

    # Allow Window to be resizable
    root.resizable(width = True, height = True)

    # create a label
    panel = Label(root)
    panel.grid(row = 2)

    # Create a button and place it into the window using grid layout
    btn = Button(root, text ='open image', command = lambda: play_images(root=root, image_folder="tmp/frames/", panel=panel))
    btn.grid(row = 1, columnspan = 4)
    root.mainloop()

def clean_cache():
    try:
        remove(
            "tmp/out.m4a",
        )
    except FileNotFoundError:
        pass
    rmtree(
        "tmp/frames/",
        ignore_errors=True,
    )
    makedirs("tmp/frames/")

if __name__ == '__main__':
    # clean_cache()
    main()