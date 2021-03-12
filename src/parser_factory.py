from xml_parser import XMLParser
from utils import get_file_name_from_path
import xml.etree.ElementTree as ET


def convert_to_json_factory(format, file):
    if format == "xml":
        return XMLParser(ET.parse(file).getroot(),
                         get_file_name_from_path(file))
