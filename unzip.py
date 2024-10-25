import sys
import os
import zipfile
from logger import logger


# Unzips a file from src to dst with a folder name of the file name from src
def unzip(src, dst):
    file_name_with_ext = os.path.basename(src)
    file_name = os.path.splitext(file_name_with_ext)[0]
    dst_path = os.path.join(dst, file_name)

    if os.path.basename(src).startswith("._"):
        logger.debug(f"Found a mac os bullshit zip file that we just gonan ignore at {src}")
        return

    # Check if the destination directory exists
    if os.path.exists(dst_path):
        logger.debug(f"Destination directory {dst_path} already exists. Skipping unzipping.")
    else:
        logger.debug(f"Unzipping contents of {src} to {dst_path}")
        os.makedirs(dst_path, exist_ok=True)
        
        if os.path.exists(src) == False:
            logger.error(f"The file: {src} does not appear to exist, exiting unzipping process now")
            return
        with zipfile.ZipFile(src, 'r') as zip_ref:
            try:
                zip_ref.extractall(dst_path)
                logger.debug(f"Successfully unzipped contents of {src} to {dst_path}")
            except Exception as e:
                logger.error(f"Error unzipping {src}: {e}")

# Unzips all files from src to dst recursively
def unzip_all(zip_dir, unzip_dir):
    logger.debug("Running unzip all")
    entries = os.listdir(zip_dir)
    directories = [entry for entry in entries if os.path.isdir(os.path.join(zip_dir, entry))]
    files = [entry for entry in entries if os.path.isfile(os.path.join(zip_dir, entry))]

    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in ['.cbz', '.zip', '.rar']:
            file_path = os.path.join(zip_dir, file)
            logger.debug(f"Now running unzip on {file_path} to {unzip_dir}")
            unzip(file_path, unzip_dir)

    for subdir in directories:
        subdir_zip = os.path.join(zip_dir, subdir)
        subdir_unzip = os.path.join(unzip_dir, subdir)
        logger.debug(f"Now recursively running unzip_all on {subdir_zip} to {subdir_unzip}")
        unzip_all(subdir_zip, subdir_unzip)
