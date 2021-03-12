import argparse
import sys
import os
from parser_factory import convert_to_json_factory


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


def validate_args(format, files):
    # if any file doesn't exist or is not with given format terminate!!
    errors = []
    format_len = len(format)
    for file in files:
        if not os.path.exists(file):
            errors.append(f"error: The file {file} doesn't exist")
            continue

        if file[-format_len:] != format:
            errors.append(f"error: The file {file} is not a {format} file!!")

    if len(errors) > 0:
        print(*errors)
        sys.exit(1)


def main():
    format, files = extract_args()
    validate_args(format, files)
    # Parse each file
    for file in files:
        parser = convert_to_json_factory(format, file)
        parser.parse()


if __name__ == "__main__":
    main()
