from parser_factory import convert_to_json_factory
from utils import extract_args, validate_args


def main():
    format, files = extract_args()
    validate_args(format, files)
    for file in files:
        parser = convert_to_json_factory(format, file)
        parsed_dict = parser.parse()
        print(parsed_dict)


if __name__ == "__main__":
    main()
