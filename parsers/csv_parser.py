import csv
from .utils import pascal_to_snake_case
import json


class CSVParser:
    def __init__(self, csv_dict_reader, heading):
        self.__dict_reader = csv_dict_reader
        self.__heading = heading

    def parse(self):
        self.__dict_reader.fieldnames = [pascal_to_snake_case(
            field) for field in self.__dict_reader.fieldnames]

        return list(self.__dict_reader)

    def write_to_file(self, file_name):
        csv_list = self.parse()
        with open(file_name, "w") as json_file:
            json.dump(csv_list, json_file)
