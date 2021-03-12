from src.utils import pascal_to_snake_case, get_file_name_without_extension
import unittest


class PascalToSnakeCaseTest(unittest.TestCase):
    def test_without_space(self):
        snake = pascal_to_snake_case("SamuelSorial")

        self.assertEqual(snake, "samuel_sorial")

    def test_with_space(self):
        snake = pascal_to_snake_case(" SamuelSorial ")

        self.assertEqual(snake, "samuel_sorial")


class GetFileNameWithoutExtension(unittest.TestCase):
    def test_without_path(self):
        first_file = get_file_name_without_extension("samuel.xml")
        second_file = get_file_name_without_extension("samuel.csv")
        third_file = get_file_name_without_extension("Samuel.csv")

        self.assertEqual(first_file, "samuel")
        self.assertEqual(second_file, "samuel")
        self.assertEqual(third_file, "Samuel")

    def test_with_path(self):
        first_file = get_file_name_without_extension("./data/xml/samuel.xml")
        second_file = get_file_name_without_extension("./data/csv/samuel.csv")
        third_file = get_file_name_without_extension("./data/csv/Samuel.csv")

        self.assertEqual(first_file, "samuel")
        self.assertEqual(second_file, "samuel")
        self.assertEqual(third_file, "Samuel")


if __name__ == '__main__':
    unittest.main()
