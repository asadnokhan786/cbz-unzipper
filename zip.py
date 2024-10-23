import os
import sys
import zipfile
import imghdr


# Zips a directory from unzip_dir to zip_dir with a filename that is the same as the folder name of unzip_dir
# Excludes files that are not valid image formats
def zip(unzip_dir, zip_dir):
    base_folder_name = os.path.basename(unzip_dir.rstrip('/'))
    zip_filename = f"{base_folder_name}.cbz"
    zip_path = os.path.join(zip_dir, zip_filename)

    os.makedirs(zip_dir, exist_ok=True)
    entries = os.listdir(unzip_dir)
    files = [entry for entry in entries if os.path.isfile(os.path.join(unzip_dir, entry))]
    with zipfile.ZipFile(zip_path, 'x') as zip_file:
        for file in files:
            full_path = os.path.join(unzip_dir, file)
            if is_valid_image(full_path):
                full_path = os.path.join(unzip_dir, file)
                zip_file.write(full_path, os.path.basename(file))


# If a valid file is found in a directory, the entire directory is zipped
def zip_all(unzip_dir, zip_dir):
    entries = os.listdir(unzip_dir)
    files = [entry for entry in entries if os.path.isfile(os.path.join(unzip_dir, entry))]
    updated_files = valid_files(files, unzip_dir)
    directories = [entry for entry in entries if os.path.isdir(os.path.join(unzip_dir, entry))]
    if len(updated_files) > 0:
        zip(unzip_dir, zip_dir)
    for directory in directories:
        subdir_unzip = os.path.join(unzip_dir, directory)
        zip_all(subdir_unzip, zip_dir)


# Determines if a given file is a valid image file
def is_valid_image(file_path):
    valid_formats = {'jpeg', 'png', 'webp', 'bmp', 'gif', 'tiff'}
    image_type = imghdr.what(file_path)
    return image_type in valid_formats

def valid_files(files, unzip_dir):
    updated_files = []
    for file in files:
        full_path = os.path.join(unzip_dir, file)
        if is_valid_image(full_path):
            updated_files.append(full_path)
    return updated_files