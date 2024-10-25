import os
import sys
from pathlib import Path
import zipfile
from PIL import Image
from logger import logger


# Zips a directory from unzip_dir to zip_dir with a filename that is the same as the folder name of unzip_dir
# Excludes files that are not valid image formats
def zip(unzip_dir, zip_dir):
    base_folder_name = os.path.basename(unzip_dir.rstrip('/'))
    zip_filename = f"{base_folder_name}.cbz"
    zip_path = os.path.join(zip_dir, zip_filename)

    os.makedirs(zip_dir, exist_ok=True)
    entries = os.listdir(unzip_dir)
    files = [entry for entry in entries if os.path.isfile(os.path.join(unzip_dir, entry))]
    logger.debug(f"Zipping to file path of {zip_path}")
    with zipfile.ZipFile(zip_path, 'x') as zip_file:
        for file in files:
            full_path = os.path.join(unzip_dir, file)
            if is_valid_image(full_path):
                full_path = os.path.join(unzip_dir, file)
                logger.debug(f"Zipping file: {full_path}")
                zip_file.write(full_path, os.path.basename(file))


# If a valid file is found in a directory, the entire directory is zipped
def zip_all(unzip_dir, zip_dir):
    entries = os.listdir(unzip_dir)
    files = [entry for entry in entries if os.path.isfile(os.path.join(unzip_dir, entry))]
    updated_files = valid_files(files, unzip_dir)
    directories = [entry for entry in entries if os.path.isdir(os.path.join(unzip_dir, entry))]
    if len(updated_files) > 0:
        logger.debug(f"Running zip function on unzip_dir: {unzip_dir} and zip_dir: {zip_dir}")
        parent_zip_dir_path = Path(zip_dir)
        parent_zip_dir = parent_zip_dir_path.parent
        zip(unzip_dir, parent_zip_dir)
    for directory in directories:
        subdir_unzip = os.path.join(unzip_dir, directory)
        subdir_zip = os.path.join(zip_dir, directory)
        logger.debug(f"Recursively running zip_all on unzip_dir: {subdir_unzip} and zip_dir: {zip_dir}")
        zip_all(subdir_unzip, subdir_zip)


# Determines if a given file is a valid image file
def is_valid_image(filename):
    try:
        img = Image.open(filename)
        img.verify()  # Check if it's a valid image
        return True
    except (IOError, SyntaxError) as e:
        return False

def valid_files(files, unzip_dir):
    updated_files = []
    for file in files:
        full_path = os.path.join(unzip_dir, file)
        if is_valid_image(full_path):
            logger.debug(f"The file {full_path} has been deemed valid image format")
            updated_files.append(full_path)
    return updated_files