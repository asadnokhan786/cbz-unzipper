import sys
import os
import zipfile


def unzip(src, dst):
    with zipfile.ZipFile(src, 'r') as zip_ref:
        zip_ref.extractall(dst)

def unzip_all(src, dst):
    for root, dirs, files in os.walk(src):
        for file in files:
            file_path = os.path.join(root, file)
            unzip(file_path, dst)
        for dir in dirs:
            subdir_src = os.path.join(root, dir)
            subdir_dst = os.path.join(dst, dir)
            unzip_all(subdir_src, subdir_dst)