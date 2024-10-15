import argparse
import os
from unzip import unzip_all


def main():
    parser = argparse.ArgumentParser(prog='cbz-unzipper-cli',
                                     description='cbz-unzipper cli')
    parser.add_argument('--src', type=str, help='Source file path')
    parser.add_argument('--dst', type=str, help='Destination file path')

    args = parser.parse_args()

    base_dir = os.path.abspath(os.path.dirname(__file__))
    src = os.path.join(base_dir, args.src)
    dst = os.path.join(base_dir, args.dst)

    if not os.path.isdir(src):
        raise ValueError(f"{src} is NOT a valid source path")
    
    unzip_all(src, dst)


if __name__ == '__main__':
    main()