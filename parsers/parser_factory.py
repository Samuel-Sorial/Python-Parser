from .xml_parser import XMLParser
from .csv_parser import CSVParser
from .utils import get_file_name_from_path
import xml.etree.ElementTree as ET
import csv
import sys


def convert_to_json_factory(format, file):
    # Precondition: file already exists, file is in the given format
    # Instaniate the correct parser
    if format == "xml":
        file_name = get_file_name_from_path(file)
        try:
            root = ET.parse(file).getroot()
        except(ET.ParseError):
            raise ValueError(
                f"error: The file {file_name} is not correctly-formatted")
        return XMLParser(root, file_name)
    if format == "csv":
        csv_data = open(file)
        return CSVParser(csv.DictReader(csv_data),
                         get_file_name_from_path(file))
