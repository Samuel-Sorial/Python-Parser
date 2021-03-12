from parsers.parser_factory import convert_to_json_factory
from parsers.utils import (extract_args, validate_file,
                           get_file_name_without_extension)


def main():
    format, files = extract_args()
    valid_files = []
    for file in files:
        try:
            validate_file(file, format)
            valid_files.append(file)
        except Exception as error:
            print(error)
            continue
    for file in valid_files:
        try:
            to_json_parser = convert_to_json_factory(format, file)
        except Exception as error:
            print(error)
            continue

        to_json_parser.write_to_file(
            get_file_name_without_extension(file) + ".json"
        )


if __name__ == "__main__":
    main()
