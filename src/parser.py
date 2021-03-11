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


def validate_args(files):
    # Checks if any file doesn't exist and terminate!!
    errors = []
    for file in files:
        if not os.path.exists(file):
            errors.append(f"error: The file {file} doesn't exist")
    if len(errors) > 0:
        print(*errors)
        sys.exit(1)


def main():
    format, files = extract_args()
    validate_args(files)
    # Validate these files
    # Parse each file
    print(format, files)


if __name__ == "__main__":
    main()
