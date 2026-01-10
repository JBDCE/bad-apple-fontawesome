from subprocess import run

def split_videofile(input_filepath):
    # Split of the audio file from the video to be able to reattach it later
    # TODO I need to figure out how to memorize the metadata.
    # Probably just reuse the source file maybe?
    run([
        'ffmpeg',
        '-i',
        input_filepath,
        '-vn',
        '-acodec',
        'copy',
        'tmp/out.m4a',
    ])

    run([
        'ffmpeg',
        '-i',
        input_filepath,
        'tmp/frames/%04d.png',
    ])

def merge_frames():
    # TODO here another ffmpeg run is used to merge
    # the split and processed picture files back into an output moviefile
    pass

if __name__ == '__main__':
    split_videofile(input_filepath='Bad-Apple.mp4')