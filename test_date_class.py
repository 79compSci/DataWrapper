import unittest
from unittest.mock import patch

from date_class import Date


class TestPartOneFeatures(unittest.TestCase):
    """Regression tests for the Part 1 Date behavior."""

    def test_default_constructor(self):
        test_date = Date()
        self.assertEqual((test_date.month, test_date.day, test_date.year), (1, 1, 1900))

    def test_valid_date(self):
        test_date = Date(12, 25, 2021)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (12, 25, 2021))

    def test_leap_day(self):
        test_date = Date(2, 29, 2024)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (2, 29, 2024))

    def test_invalid_dates(self):
        for values in [(13, 1, 2021), (4, 31, 2021), (2, 29, 2023), (0, 1, 2021), (1, 0, 2021)]:
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    Date(*values)

    def test_set_date_and_failure_preserves_original(self):
        test_date = Date(12, 25, 2021)
        test_date.set_date(2, 29, 2024)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (2, 29, 2024))
        with self.assertRaises(ValueError):
            test_date.set_date(4, 31, 2022)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (2, 29, 2024))

    def test_leap_year_methods(self):
        self.assertTrue(Date(1, 1, 2024).is_leap_year())
        self.assertFalse(Date(1, 1, 2023).is_leap_year())
        self.assertTrue(Date.is_year_leap(2000))
        self.assertFalse(Date.is_year_leap(1900))

    def test_last_day_methods(self):
        self.assertEqual(Date(2, 1, 2024).last_day(), 29)
        self.assertEqual(Date(2, 1, 2023).last_day(), 28)
        self.assertEqual(Date.last_day_of_month(9, 2021), 30)
        with self.assertRaises(ValueError):
            Date.last_day_of_month(13, 2021)

    def test_formatting_methods(self):
        test_date = Date(12, 25, 2021)
        self.assertEqual(test_date.to_numeric_string(), "12/25/2021")
        self.assertEqual(test_date.to_month_first_string(), "December 25, 2021")
        self.assertEqual(test_date.to_day_first_string(), "25 December 2021")


class TestSubtraction(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(Date(4, 18, 2014) - Date(4, 10, 2014), 8)

    def test_negative_difference(self):
        self.assertEqual(Date(4, 10, 2014) - Date(4, 18, 2014), -8)

    def test_equal_dates(self):
        self.assertEqual(Date(6, 15, 2020) - Date(6, 15, 2020), 0)

    def test_different_months(self):
        self.assertEqual(Date(5, 1, 2021) - Date(4, 30, 2021), 1)

    def test_different_years(self):
        self.assertEqual(Date(1, 1, 2022) - Date(12, 31, 2021), 1)

    def test_range_containing_leap_day(self):
        self.assertEqual(Date(3, 1, 2024) - Date(2, 28, 2024), 2)

    def test_unsupported_operand_raises_type_error(self):
        with self.assertRaises(TypeError):
            _ = Date(4, 18, 2014) - 10

    def test_second_assignment_example(self):
        self.assertEqual(Date(2, 2, 2006) - Date(11, 10, 2003), 815)


class TestIncrement(unittest.TestCase):
    def check_increment(self, start, expected):
        test_date = Date(*start)
        returned_value = test_date.increment()
        self.assertIs(returned_value, test_date)
        self.assertEqual((test_date.month, test_date.day, test_date.year), expected)

    def test_normal_increment(self):
        self.check_increment((4, 18, 2018), (4, 19, 2018))

    def test_april_30_to_may_1(self):
        self.check_increment((4, 30, 2018), (5, 1, 2018))

    def test_january_31_to_february_1(self):
        self.check_increment((1, 31, 2018), (2, 1, 2018))

    def test_february_28_non_leap(self):
        self.check_increment((2, 28, 2019), (3, 1, 2019))

    def test_february_28_leap(self):
        self.check_increment((2, 28, 2020), (2, 29, 2020))

    def test_february_29_to_march_1(self):
        self.check_increment((2, 29, 2020), (3, 1, 2020))

    def test_december_31_to_january_1(self):
        self.check_increment((12, 31, 2020), (1, 1, 2021))


class TestDecrement(unittest.TestCase):
    def check_decrement(self, start, expected):
        test_date = Date(*start)
        returned_value = test_date.decrement()
        self.assertIs(returned_value, test_date)
        self.assertEqual((test_date.month, test_date.day, test_date.year), expected)

    def test_normal_decrement(self):
        self.check_decrement((4, 18, 2018), (4, 17, 2018))

    def test_may_1_to_april_30(self):
        self.check_decrement((5, 1, 2018), (4, 30, 2018))

    def test_march_1_non_leap(self):
        self.check_decrement((3, 1, 2019), (2, 28, 2019))

    def test_march_1_leap(self):
        self.check_decrement((3, 1, 2020), (2, 29, 2020))

    def test_january_1_to_previous_year(self):
        self.check_decrement((1, 1, 2021), (12, 31, 2020))


class TestString(unittest.TestCase):
    def test_required_string(self):
        self.assertEqual(str(Date(4, 18, 2018)), "April 18, 2018")

    def test_single_digit_day(self):
        self.assertEqual(str(Date(4, 8, 2018)), "April 8, 2018")

    def test_leap_day(self):
        self.assertEqual(str(Date(2, 29, 2020)), "February 29, 2020")

    def test_year_boundary(self):
        self.assertEqual(str(Date(1, 1, 2021)), "January 1, 2021")


class TestFromInput(unittest.TestCase):
    @patch("builtins.input", side_effect=["4", "18", "2018"])
    def test_from_input_creates_date(self, mock_input):
        result = Date.from_input()
        self.assertEqual((result.month, result.day, result.year), (4, 18, 2018))
        self.assertEqual(mock_input.call_count, 3)

    @patch("builtins.input", side_effect=["April", "18", "2018"])
    def test_from_input_nonnumeric(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["13", "18", "2018"])
    def test_from_input_invalid_month(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["4", "31", "2018"])
    def test_from_input_invalid_day(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()

    @patch("builtins.input", side_effect=["2", "29", "2019"])
    def test_from_input_invalid_leap_day(self, mock_input):
        with self.assertRaises(ValueError):
            Date.from_input()


if __name__ == "__main__":
    unittest.main()
