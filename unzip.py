import sys
import os
import zipfile


# Unzips a file from src to dst with a folder name of the file name from src
def unzip(src, dst):
    with zipfile.ZipFile(src, 'r') as zip_ref:
        file_name_with_ext = os.path.basename(src)
        file_name = os.path.splitext(file_name_with_ext)[0]
        dst_path = os.path.join(dst, file_name)
        zip_ref.extractall(dst_path)

# Unzips all files from src to dst recursively
def unzip_all(src, dst):
    for root, dirs, files in os.walk(src):
        if root != src:
            break
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in ['.cbz', '.zip', '.rar']:
                file_path = os.path.join(root, file)
                unzip(file_path, dst)
        for sub_dir in dirs:
            subdir_src = os.path.join(root, sub_dir)
            subdir_dst = os.path.join(dst, sub_dir)
            unzip_all(subdir_src, subdir_dst)