import os
import sys
import zipfile
import imghdr


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


def zip_all(unzip_dir, zip_dir):
    base_folder_name = os.path.basename(unzip_dir.rstrip('/'))

    entries = os.listdir(unzip_dir)
    files = [entry for entry in entries if os.path.isfilse(os.path.join(unzip_dir, entry))]
    directories = [entry for entry in entries if os.path.isdir(os.path.join(unzip_dir, entry))]


def is_valid_image(file_path):
    valid_formats = {'jpeg', 'png', 'webp', 'bmp', 'gif', 'tiff'}
    image_type = imghdr.what(file_path)
    return image_type in valid_formats