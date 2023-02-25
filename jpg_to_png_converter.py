import sys
import os
from PIL import Image


def convert(source, destination):
    '''
    Converts all .jpg files in a source directory to .png. These are saved to a
    destination directory. Non-jpeg files in the source directory are ignored.
    :param source: directory containing jpeg files.
    :param destination: may or may not already exist.
    :return: True, if successful
    '''
    # Quite robust, but somewhat bloated with try-except statements. There is possibly
    # a better way to do this, but it seems silly to make functions that execute
    # built-in functions with only error handling added.
    try:
        os.makedirs(destination, exist_ok=True)
    except OSError as err:
        print(f"Directory '{destination}' could not be created: {err}")
        return err
    try:
        source_contents = os.listdir(source)
    except OSError as err:
        print(f"Directory '{source}' does not exist: {err}")
    try:
        for file in source_contents:
            if file.endswith(".jpg"):
                img = Image.open(f"{source}/{file}")
            else:
                continue
            file = file.replace("jpg", "png")
            img.save(f"{destination}/{file}")
            return True
        return err
    except IOError as err:
        return err

source_dir = sys.argv[1]
destination_dir = sys.argv[2]
convert(source_dir, destination_dir)