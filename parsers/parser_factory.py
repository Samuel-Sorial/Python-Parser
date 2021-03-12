from .xml_parser import XMLParser
from .csv_parser import CSVParser
from .utils import get_file_name_from_path
import xml.etree.ElementTree as ET
import csv


def convert_to_json_factory(format, file):
    if format == "xml":
        return XMLParser(ET.parse(file).getroot(),
                         get_file_name_from_path(file))
    if format == "csv":
        csv_data = open(file)
        return CSVParser(csv.DictReader(csv_data),
                         get_file_name_from_path(file))
