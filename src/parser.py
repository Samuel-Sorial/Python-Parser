import argparse
import sys
import os


def extract_args():
    # Returns the command line arguments
    parser = argparse.ArgumentParser(
        description="Parse given files from a given format to JSON format")
    parser.add_argument("format", choices=[
        "csv", "xml"],
        help="The format of the given file(s)")

    parser.add_argument("files", nargs='+', help="File(s) to be parsed")
    arguments = parser.parse_args(sys.argv[1:])
    return arguments.format, arguments.files


def main():
    format, files = extract_args()
    # Validate these files
    # Parse each file
    print(format, files)


if __name__ == "__main__":
    main()
