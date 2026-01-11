from subprocess import run

def split_videofile(input_filepath):
    # Split of the audio file from the video to be able to reattach it later
    # TODO I need to figure out how to memorize the metadata.
    # Probably just reuse the source file maybe?
    run([
        'ffmpeg',
        '-i', input_filepath,
        '-vn',
        '-acodec', 'copy',
        'tmp/audio.m4a',
    ])
    # Separate the video file into individual frames numbering them accordingly
    run([
        'ffmpeg',
        '-i', input_filepath,
        'tmp/frames/%04d.png',
    ])
    return

def merge_frames():
    # TODO Figure out why the output video seeems slowed down the Video
    # claims to be at the right frame rate but i get a noticable audio and video desync

    # the split and processed picture files back into an output moviefile
    run([
        'ffmpeg',
        '-i', 'tmp/outframes/%04d.png',  # Add the frames separated
        '-i', 'tmp/audio.m4a',  # The audio file separated
        '-c:v', 'libx264',  # Videocodec
        '-c:a', 'copy', # Audo Codec
        '-r', '30/1',  # Framerate  TODO This value might change for a new input file
        '-pix_fmt', 'yuv420p',  # Pixel format  TODO Figure out if this might change as well
        '-shortest',  # Some audio padding parameter no clue yet
        'out.mp4',  # TODO Add the option to rename this or give it a better filename
    ])
    return

if __name__ == '__main__':
    split_videofile(input_filepath='Bad-Apple.mp4')