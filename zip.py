import os
import sys
import zipfile


def zip(unzip_dir, zip_dir):
    base_folder_name = os.path.basename(unzip_dir.rstrip('/'))
    zip_filename = f"{base_folder_name}.cbz"
    zip_path = os.path.join(zip_dir, zip_filename)

    entries = os.listdir(unzip_dir)
    files = [entry for entry in entries if os.path.isfile(os.path.join(unzip_dir, entry))]
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for file in files:
            full_path = os.path.join(unzip_dir, file)
            zip_file.write(full_path, os.path.basename(file))


def zip_all(src, dst):
    pass