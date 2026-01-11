from tkinter import *
from tkinter import ttk
# loading Python Imaging Library
from PIL import ImageTk, Image

from os import remove, makedirs, listdir
from shutil import rmtree

from image_processor import render_frame
from video_processor import split_videofile, merge_frames

from argparse import ArgumentParser

def open_img(imagepath, panel: Label, size=(640, 360)):
    # Handle loading an imagefile to be displayed inside
    # a label passed to this function.
    # The image is sampled to match the given size input.
    img = Image.open(imagepath)
    img = img.resize(size, Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    # I dont understand why i have to add the image twich in here but tk breaks when i dont
    panel.image = img
    panel.configure(image=img)

def play_images(button:Button, root, image_folder, panel):
    button.config(state=DISABLED)
    for file in listdir(image_folder):
        output_image_path = render_frame(
            source_img_path=f"{image_folder}/{file}"
        )
        open_img(
            imagepath=output_image_path,
            panel=panel
        )
        root.update()
    button.config(state=ACTIVE)

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
    btn = Button(root, text ='open image', command = lambda: play_images(button=btn, root=root, image_folder="tmp/frames/", panel=panel))
    btn.grid(row = 1, columnspan = 4)
    root.mainloop()

def clean_cache():
    try:
        remove(
            "tmp/audio.m4a",
        )
    except FileNotFoundError:
        pass
    rmtree(
        "tmp/frames/",
        ignore_errors=True,
    )
    makedirs("tmp/frames/")

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='bad-apple-fontawesome',
        description=(
            'The aim of this project is to recreate the '
            'famous bad apple music video using icons '
            'from the fontawesome library.'
        ),
    )
    parser.add_argument(
        '-i', '--input',
        help="Choose the input file to be parsed",
        default="Bad-Apple.mp4"
    )
    parser.add_argument(
        '-rm', '--remove',
        help=(
            "Add this argument to clear out the created "
            "tmp folder to restart generation from the start."
        ),
        action='store_true'
    )
    parser.add_argument(
        '--headless',
        help=(
            "Add this parameter to skip rendering a gui "
            "and just perform the image processing "
            "directly using the arguments provided"
        ),
        action='store_true',
    )
    args = parser.parse_args()

    if args.remove:
        clean_cache()

    # TODO Call this on a button input by the user instead
    split_videofile(args.input)
    merge_frames()
    if not args.headless:
        main()
