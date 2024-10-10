import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Specify input/output locations for unzipping files", exit_on_error=False)

    parser.add_argument('-i', '--input', required=True, type=str, help='Location of input folder')
    parser.add_argument('-o', '--output', required=True, type=str, help='Location of output folder')
    
    args = parser.parse_args()
    return args

def main():
    try:
        args = parse_arguments()
    except Exception as e:
        print(f"An unexpected error occurred during parsing: {e}")


if __name__ == "__main__":
    main()
