import re
import argparse
import sys
import os

# Compile the pattern to improve performance
# Inspired by: https://stackoverflow.com/a/1176023/13089670
pattern = re.compile(r'(?<!^)(?=[A-Z])')


def pascal_to_snake_case(text):
    text = text.strip()
    return pattern.sub('_', text).lower()


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


def get_file_name_without_extension(file_name):
    # Returns file name without the .extension
    # file.xml -> file
    file_without_path = file_name[file_name.rfind('/') + 1:]
    return file_without_path[: file_without_path.find('.')]
