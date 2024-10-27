import unittest

from lesson_09.homeworks import multiplication_table1, reverse_string
from lesson_09.homeworks import arithmetic_average


class TestMultiplicationTable(unittest.TestCase):
    def test_multiplication_table_3(self):  # <25
        expected_output = [
            "3x1=3",
            "3x2=6",
            "3x3=9",
            "3x4=12",
            "3x5=15",
            "3x6=18",
            "3x7=21",
            "3x8=24"
        ]
        self.assertEqual(multiplication_table1(3), expected_output)

    def test_multiplication_table_5(self):  # 25
        expected_output = [
            "5x1=5",
            "5x2=10",
            "5x3=15",
            "5x4=20",
            "5x5=25"
        ]
        self.assertEqual(multiplication_table1(5), expected_output)

    def test_multiplication_table_10(self):
        self.assertEqual(multiplication_table1(26), [])


class TestArithmeticAverage(unittest.TestCase):
    def test_non_empty_list(self):
        self.assertEqual(arithmetic_average([10, 10, 10, 10, 10]), 10)

    def test_empty_list(self):
        self.assertEqual(arithmetic_average([]), 'The list is empty')

    def test_single_element(self):
        self.assertEqual(arithmetic_average([10]), 10)

    def test_negative_elements_list(self):
        self.assertEqual(arithmetic_average([-10, -15, -20]), -15)


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        expected_text = 'dlroW olleH'
        self.assertEqual(reverse_string('Hello World'), expected_text)

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_numbers_and_symbols(self):
        self.assertEqual(reverse_string('1234!'), "!4321")


if __name__ == "__main__":
    unittest.main(verbosity=2)
