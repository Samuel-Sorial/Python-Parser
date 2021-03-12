from xml_to_json import XMLToJson
import xml.etree.ElementTree as ET


def convert_to_json_factory(format, file):
    if format == "xml":
        return XMLToJson(ET.parse(file), file)
