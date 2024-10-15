import os
import subprocess
import pytest
import shutil


def test_main_simple():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    src_path = os.path.join(base_dir, "sample-files/zipped")
    dst_path = os.path.join(base_dir, "sample-files/unzipped")

    text_file_1 = os.path.join(dst_path, 'test/test.txt')
    text_file_2 = os.path.join(dst_path, 'test2/text2.txt')
    text_file_3 = os.path.join(dst_path, 'test2/text3.txt')
    text_file_4 = os.path.join(dst_path, 'subdir/test3/text3.txt')

    result = subprocess.run(['python', 'main.py', '--src', src_path, '--dst', dst_path], capture_output=True, text=True)

    assert result.returncode == 0

    assert os.path.exists(text_file_1)
    assert os.path.exists(text_file_2)
    assert os.path.exists(text_file_3)
    assert os.path.exists(text_file_4)

    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)

def test_main_invalid_src():
    base_dir = base_dir = os.path.abspath(os.path.dirname(__file__))
    src_path = os.path.join(base_dir, "sample-files-no-exist/zipped")
    dst_path = os.path.join(base_dir, "sample-files/unzipped")

    result = subprocess.run(['python', 'main.py', '--src', src_path, '--dst', dst_path], capture_output=True, text=True)

    assert result.returncode != 0
    assert src_path + " is NOT a valid source path" in result.stderr
