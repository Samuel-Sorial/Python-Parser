import csv
from utils import pascal_to_snake_case


class CSVParser:
    def __init__(self, csv_dict_reader, heading):
        self.__dict_reader = csv_dict_reader
        self.__heading = heading

    def parse(self):
        for line in self.__dict_reader:

            print(line.items())
