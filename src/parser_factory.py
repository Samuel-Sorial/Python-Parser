from xml_to_json import XMLToJson


def convert_to_json_factory(format, file):
    if format == "xml":
        return XMLToJson(file)
