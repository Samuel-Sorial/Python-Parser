from xml_parser import XMLParser
import xml.etree.ElementTree as ET


def convert_to_json_factory(format, file):
    if format == "xml":
        return XMLParser(ET.parse(file), file)
