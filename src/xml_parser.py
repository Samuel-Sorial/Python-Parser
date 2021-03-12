from collections import defaultdict


class XMLParser:
    def __init__(self, xml_root, heading):
        self.__xml_root = xml_root
        file_name = heading[heading.rfind('/')+1:]
        self.__heading = file_name

    def __append_to_neighbours(self, neighbours_dict, member_dict):
        for key, value in member_dict.items():
            neighbours_dict[key.lower()].append(value)

    def __flatten_children(self, child_dict, parent_dict):
        for key, value in child_dict.items():
            parent_dict[key] = value[0] if len(value) == 1 else value

    def __add_attributes(self, tree_dict, tree):
        for key, value in tree.attrib.items():
            tree_dict[key.lower()] = value

    def __convert_tree_to_dict(self, tree):
        # Parse XML tree to dict[string : dict || list]
        # Inspired from: https://stackoverflow.com/a/10076823/13089670
        children_dect = defaultdict(list)
        for child in list(tree):
            current_child_dict = self.__convert_tree_to_dict(child)
            self.__append_to_neighbours(children_dect, current_child_dict)

        tag = tree.tag.lower()
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
        print(xml_dict)
        return xml_dict
