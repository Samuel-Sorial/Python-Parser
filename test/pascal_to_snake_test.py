from src.utils import pascal_to_snake_case
import unittest


class PascalToSnakeCaseTest(unittest.TestCase):
    def test_without_space(self):
        snake = pascal_to_snake_case("SamuelSorial")
        self.assertEqual(snake, "samuel_sorial")

    def test_with_space(self):
        snake = pascal_to_snake_case(" SamuelSorial ")
        self.assertEqual(snake, "samuel_sorial")


if __name__ == '__main__':
    unittest.main()
