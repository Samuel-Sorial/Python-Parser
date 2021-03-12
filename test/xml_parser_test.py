from src.xml_parser import XMLParser
import unittest
import xml.etree.ElementTree as ET


class TestParser(unittest.TestCase):
    def test_source_name_with_empty(self):
        xml_tree = ET.fromstring(
            '<?xml version="1.0" encoding="UTF-8"?><Transaction> </Transaction>')
        file_name = "transaction"
        parser = XMLParser(xml_tree, file_name)
        curr_dict = parser.parse()
        self.assertDictEqual(
            curr_dict, {"file_name": f"xml/{file_name}", "transaction": {}})

    def test_nested_without_attributes(self):
        xml_tree = ET.fromstring(
            '<?xml version="1.0" encoding="UTF-8"?><Transaction> <Date>18/1/1998</Date> <Name> <First>Samuel</First><Last>Sorial</Last></Name> </Transaction>')
        file_name = "transaction"
        parser = XMLParser(xml_tree, file_name)
        curr_dict = parser.parse()
        self.assertDictEqual(
            curr_dict, {"file_name": f"xml/{file_name}", "transaction":
                        {"date": "18/1/1998", "name": {"first": "Samuel",
                                                       "last": "Sorial"}}})

    def test_nested_with_attributes(self):
        xml_tree = ET.fromstring(
            '<?xml version="1.0" encoding="UTF-8"?><Transaction id="1234"> <Date>18/1/1998</Date> <Name> <First>Samuel</First><Last>Sorial</Last></Name> </Transaction>')
        file_name = "transaction"
        parser = XMLParser(xml_tree, file_name)
        curr_dict = parser.parse()
        self.assertDictEqual(
            curr_dict, {"file_name": f"xml/{file_name}", "transaction":
                        {"id": "1234", "date": "18/1/1998", "name": {"first":
                                                                     "Samuel", "last": "Sorial"}}})


if __name__ == '__main__':
    unittest.main()
