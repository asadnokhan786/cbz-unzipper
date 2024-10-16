import sys
import os
import pytest
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from zip import zip, zip_all
from unzip import unzip, unzip_all


def test_zip_simple():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_dir = os.path.join(base_dir, 'sample-zips/zipped')
    unzip_dir = os.path.join(base_dir, 'sample-zips/unzipped/unzipped-files')

    
    test_zip = os.path.join(zip_dir, 'unzipped-files.cbz')

    zip(unzip_dir, zip_dir)

    assert(os.path.exists(test_zip))

    if os.path.exists(test_zip):
        os.remove(test_zip)

def test_zip_valid_file_zipping():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_dir = os.path.join(base_dir, 'sample-zips/zipped/more-unzipped')
    unzip_dir = os.path.join(base_dir, 'sample-zips/unzipped/more-unzipped/unzipped-files-2')

    
    test_zip = os.path.join(zip_dir, 'unzipped-files-2.cbz')

    zip(unzip_dir, zip_dir)

    assert(os.path.exists(test_zip))

    if os.path.exists(test_zip):
        test_zip_unzip_dir = os.path.join(zip_dir, 'unzipped-files-2-unzipped')
        unzip(test_zip, test_zip_unzip_dir)
        should_not_zip_file = os.path.join(test_zip_unzip_dir, 'unzipped-files-2/004.txt')
        assert(not os.path.exists(should_not_zip_file))

    if os.path.exists(zip_dir):
        shutil.rmtree(zip_dir)
    

def test_zip_invalid_path():
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
    test_zip_2 = os.path.join(zip_dir, 'more-unzipped/unzipped-files-2.cbz')
    test_zip_3 = os.path.join(zip_dir, 'more-unzipped/unzipped-files-3.cbz')

    zip_all(unzip_dir, zip_dir)

    assert(os.path.exists(test_zip))
    assert(os.path.exists(test_zip_2))
    assert(os.path.exists(test_zip_3))

    if os.path.exists(test_zip_2):
        shutil.rmtree(zip_dir)
