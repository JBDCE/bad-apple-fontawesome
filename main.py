from os import remove, makedirs
from shutil import rmtree

def main():
    pass

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
    clean_cache()
    main()