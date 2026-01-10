# loading Python Imaging Library
from PIL import ImageTk, Image
from pathlib import Path

def _get_framenumber(filepath):
    framenumber = Path(filepath).stem
    return framenumber

def render_frame(source_img_path):
    # Open the image in the filepath
    img = Image.open(source_img_path)
    framenumber = _get_framenumber(source_img_path)

    # Do things to the pixels in the image
    output_image = img

    # Write it to a new output file
    output_img_path = f"tmp/outframes/{framenumber}.png"
    output_image.save(output_img_path)
    return source_img_path

if __name__ == '__main__':
    render_frame('tmp/frames/0064.png')
