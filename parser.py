from parsers.parser_factory import convert_to_json_factory
from parsers.utils import (extract_args, validate_args,
                           get_file_name_without_extension)


def main():
    format, files = extract_args()
    validate_args(format, files)
    for file in files:
        try:
            to_json_parser = convert_to_json_factory(format, file)
        except ValueError as error:
            print(error)
            continue

        to_json_parser.write_to_file(
            get_file_name_without_extension(file) + ".json"
        )


if __name__ == "__main__":
    main()
