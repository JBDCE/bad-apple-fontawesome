from subprocess import run

def split_videofile(filepath):
    # Split of the audio file from the video to be able to reattach it later
    # TODO I need to figure out how to memorize the metadata.
    # Probably just reuse the source file maybe?
    run([
        'ffmpeg',
        '-i',
        filepath,
        '-vn',
        '-acodec',
        'copy',
        'tmp/out.m4a',
    ])



if __name__ == '__main__':
    split_videofile(filepath='Bad-Apple.mp4')