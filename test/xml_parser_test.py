from src.xml_parser import XMLParser
import unittest
import xml.etree.ElementTree as ET


class TestParser(unittest.TestCase):
    def test_success_parser(self):
        xml_tree = ET.fromstring(
            '<?xml version="1.0" encoding="UTF-8"?><Transaction> </Transaction>')
        file_name = "transaction"
        parser = XMLParser(xml_tree, file_name)
        curr_dict = parser.parse()
        self.assertDictEqual(
            curr_dict, {"file_name": f"xml/{file_name}", "transaction": {}})


if __name__ == '__main__':
    unittest.main()
