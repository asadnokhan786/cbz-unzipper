import sys
import os
import pytest
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unzip import unzip, unzip_all

def test_unzip_simple():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_path = os.path.join(base_dir, 'sample-files/zipped/test.cbz')
    unzip_dir = os.path.join(base_dir, 'sample-files/unzipped')
    test_file = os.path.join(unzip_dir, 'test/test.txt')

    unzip(zip_path, unzip_dir)
    assert os.path.exists(test_file)
    
    if os.path.exists(unzip_dir):
        shutil.rmtree(unzip_dir)

def test_unzip_invalid_src():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_path = os.path.join(base_dir, 'sample-files/zipped/invalid.zip')
    unzip_dir = os.path.join(base_dir, 'sample-files/unzipped')

    with pytest.raises(FileNotFoundError):
        unzip(zip_path, unzip_dir)

def test_unzip_non_zip_file():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_path = os.path.join(base_dir, 'sample-files/zipped/not-a-zip.txt')
    unzip_dir = os.path.join(base_dir, 'sample-files/unzipped')

    with pytest.raises(Exception):
        unzip(zip_path, unzip_dir)
    


def test_unzip_all_simple():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_path = os.path.join(base_dir, 'sample-files/zipped')
    unzip_dir = os.path.join(base_dir, 'sample-files/unzipped')
    text_file_1 = os.path.join(unzip_dir, 'test/test.txt')
    text_file_2 = os.path.join(unzip_dir, 'test2/text2.txt')
    text_file_3 = os.path.join(unzip_dir, 'test2/text3.txt')
    text_file_4 = os.path.join(unzip_dir, 'subdir/test3/text3.txt')

    unzip_all(zip_path, unzip_dir)

    assert os.path.exists(text_file_1)
    assert os.path.exists(text_file_2)
    assert os.path.exists(text_file_3)
    assert os.path.exists(text_file_4)

    if os.path.exists(unzip_dir):
        shutil.rmtree(unzip_dir)

    
