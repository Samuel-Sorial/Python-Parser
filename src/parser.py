from parser_factory import convert_to_json_factory
from utils import extract_args, validate_args, get_file_name_without_extension
import json


def main():
    format, files = extract_args()
    validate_args(format, files)
    for file in files:
        parser = convert_to_json_factory(format, file)
        parsed_dict = parser.parse()
        output_name = get_file_name_without_extension(file)
        with open(f"{output_name}.json", "w") as json_file:
            json.dump(parsed_dict, json_file)


if __name__ == "__main__":
    main()
