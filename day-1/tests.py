import unittest
from module import Day1

with open('day-1/example_data.txt', 'r') as file:
    example_input = file.read()

class TestStringMethods(unittest.TestCase):
    def test_calculate_calibration_value(self):
        self.assertEqual(Day1.calculate_calibration_value(example_input.splitlines()[0]), 12)
        self.assertEqual(Day1.calculate_calibration_value(example_input.splitlines()[1]), 38)
        self.assertEqual(Day1.calculate_calibration_value(example_input.splitlines()[2]), 15)
        self.assertEqual(Day1.calculate_calibration_value(example_input.splitlines()[3]), 77)

    def test_sum_calibration_values(self):
        self.assertEqual(Day1.sum_calibration_values(example_input), 142)

    def test_calculate_input_data(self):
        with open('day-1/input_data.txt', 'r') as file:
            calibration_input = file.read()
        
        self.assertEqual(Day1.sum_calibration_values(calibration_input), 55090)

if __name__ == '__main__':
    unittest.main()


# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# 1 split multiline string into array of strings (new line character)
# 2 filter, remove non-numbers
# 3 analyze (Assume no number is 0, 1 integer, use as first and last, if more  more, conditional logic for both scenarios, >1)

