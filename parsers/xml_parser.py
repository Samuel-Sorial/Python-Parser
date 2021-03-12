from collections import defaultdict
from .utils import pascal_to_snake_case
import json


class XMLParser:
    def __init__(self, xml_root, heading):
        self.__xml_root = xml_root
        self.__heading = heading

    def __append_to_neighbours(self, neighbours_dict, member_dict):
        for key, value in member_dict.items():
            neighbours_dict[pascal_to_snake_case(key)].append(value)

    def __flatten_children(self, child_dict, parent_dict):
        for key, value in child_dict.items():
            parent_dict[key] = value[0] if len(value) == 1 else value

    def __add_attributes(self, tree_dict, tree):
        for key, value in tree.attrib.items():
            tree_dict[pascal_to_snake_case(key)] = value

    def __convert_tree_to_dict(self, tree):
        # Parse XML tree to dict[string : dict || list]
        # Inspired from: https://stackoverflow.com/a/10076823/13089670
        children_dect = defaultdict(list)
        for child in list(tree):
            current_child_dict = self.__convert_tree_to_dict(child)
            self.__append_to_neighbours(children_dect, current_child_dict)

        tag = pascal_to_snake_case(tree.tag)
        xml_dict = {tag: {}}
        self.__flatten_children(children_dect, xml_dict[tag])
        self.__add_attributes(xml_dict[tag], tree)

        if tree.text.strip():
            text = tree.text.strip()
            xml_dict[tag] = text
        return xml_dict

    def parse(self):
        xml_dict = self.__convert_tree_to_dict(self.__xml_root)
        xml_dict["file_name"] = f"xml/{self.__heading}"
        return xml_dict

    def write_to_file(self, file_name):
        parsed_dict = self.parse()
        with open(file_name, "w") as json_file:
            json.dump(parsed_dict, json_file)
