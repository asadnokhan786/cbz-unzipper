import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from zip import zip, zip_all


def test_zip_simple():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_dir = os.path.join(base_dir, 'sample-zips/zipped')
    unzip_dir = os.path.join(base_dir, 'sample-zips/unzipped/unzipped-files')

    
    test_zip = os.path.join(zip_dir, 'unzipped-files.cbz')

    zip(unzip_dir, zip_dir)

    assert(os.path.exists(test_zip))

    if os.path.exists(test_zip):
        os.remove(test_zip)

def test_zip_invalid():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_dir = os.path.join(base_dir, 'sample-zips/zipped')
    unzip_dir = os.path.join(base_dir, 'sample-zips/unzipped-invalid')


    with pytest.raises(FileNotFoundError):
        zip(unzip_dir, zip_dir)

def test_zip_all_simple():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_dir = os.path.join(base_dir, 'sample-zips/zipped')
    unzip_dir = os.path.join(base_dir, 'sample-zips/unzipped')

    
    test_zip = os.path.join(zip_dir, 'unzipped-files.cbz')
    test_zip_2 = os.path.join(zip_dir, 'unzipped-files-2.cbz')

    zip(unzip_dir, zip_dir)

    assert(os.path.exists(test_zip))

    if os.path.exists(test_zip):
        os.remove(test_zip)

    assert(os.path.exists(test_zip_2))

    if os.path.exists(test_zip_2):
        os.remove(test_zip_2)
