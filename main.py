import argparse
import os
from unzip import unzip_all


def main():
    parser = argparse.ArgumentParser(prog='cbz-unzipper CLI',
                                     description='cbz-unzipper CLI is a command line interface program implemented in python\
                                                  aimed at unzipping/zipping files in mass safely and reliably to the user\'s specific needs')
    parser.add_argument('--src', '-s', required='true', type=str, help='Source file path, required')
    parser.add_argument('--dst', '-d', required='true', type=str, help='Destination file path, required')

    args = parser.parse_args()

    base_dir = os.path.abspath(os.path.dirname(__file__))
    src = os.path.join(base_dir, args.src)
    dst = os.path.join(base_dir, args.dst)

    if not os.path.isdir(src):
        raise ValueError(f"{src} is NOT a valid source path")
    
    unzip_all(src, dst)


if __name__ == '__main__':
    main()