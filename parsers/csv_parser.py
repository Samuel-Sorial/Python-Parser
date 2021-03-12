import csv
from .utils import pascal_to_snake_case
import json


class CSVParser:
    def __init__(self, csv_dict_reader, heading):
        self.__dict_reader = csv_dict_reader
        self.__heading = heading

    def __filter_nulls(self, dict_list):
        filtered_list = []
        for current_dict in dict_list:
            filtered_list.append({key: value for key,
                                  value in current_dict.items()
                                  if key is not None and value is not None})

        return filtered_list

    def parse(self):
        self.__dict_reader.fieldnames = [pascal_to_snake_case(
            field) for field in self.__dict_reader.fieldnames]

        return self.__filter_nulls(list(self.__dict_reader))

    def write_to_file(self, file_name):
        csv_list = self.parse()
        with open(file_name, "w") as json_file:
            json.dump(csv_list, json_file)
