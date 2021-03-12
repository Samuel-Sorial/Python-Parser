from collections import defaultdict
import xml.etree.ElementTree as ET
import pprint

pp = pprint.PrettyPrinter(width=41, compact=True)


class XMLToJson:
    def __init__(self, file):
        self.file = file

    def __append_to_neighbours(self, neighbours_dict, member_dict):
        # TODO
        pass

    def __flatten_children(self, child_dict, parent_dict):
        # TODO
        pass

    def __add_attributes(self, tree_dict, tree):
        # TODO
        pass

    def __convert_tree_to_dict(self, tree):
        children_dect = defaultdict(list)
        for child in tree.getchildren():
            current_child_dict = self.__convert_tree_to_dict(child)
            self.__append_to_neighbours(children_dect, current_child_dict)

        xml_dict = {tree.tag: {}}
        self.__flatten_children(children_dect, xml_dict[tree.tag])
        self.__add_attributes(xml_dict[tree.tag], tree)

        if tree.text.strip():
            text = tree.text.strip()
            xml_dict[tree.tag] = text
        return xml_dict

    def parse(self):
        root = ET.parse(self.file).getroot()
        pp.pprint(self.__convert_tree_to_dict(root))


def get_parser(format, file):
    if format == "xml":
        return XMLToJson(file)
