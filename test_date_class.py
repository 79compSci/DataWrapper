import unittest
from date_class import Date


class TestDateConstructorAndProperties(unittest.TestCase):
    """Test Date construction and read-only properties."""

    def test_default_constructor(self):
        test_date = Date()
        self.assertEqual((test_date.month, test_date.day, test_date.year), (1, 1, 1900))

    def test_valid_date(self):
        test_date = Date(12, 25, 2021)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (12, 25, 2021))

    def test_leap_day(self):
        test_date = Date(2, 29, 2024)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (2, 29, 2024))

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            Date(13, 1, 2021)

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            Date(4, 31, 2021)

    def test_invalid_leap_day(self):
        with self.assertRaises(ValueError):
            Date(2, 29, 2023)

    def test_zero_month(self):
        with self.assertRaises(ValueError):
            Date(0, 1, 2021)

    def test_zero_day(self):
        with self.assertRaises(ValueError):
            Date(1, 0, 2021)

    def test_properties_are_read_only(self):
        test_date = Date(12, 25, 2021)
        with self.assertRaises(AttributeError):
            test_date.month = 1
        with self.assertRaises(AttributeError):
            test_date.day = 1
        with self.assertRaises(AttributeError):
            test_date.year = 2000


class TestSetDate(unittest.TestCase):
    """Test replacing the stored date."""

    def test_set_date(self):
        test_date = Date()
        test_date.set_date(12, 25, 2021)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (12, 25, 2021))

    def test_set_date_leap_day(self):
        test_date = Date()
        test_date.set_date(2, 29, 2024)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (2, 29, 2024))

    def test_set_date_invalid(self):
        test_date = Date(12, 25, 2021)
        with self.assertRaises(ValueError):
            test_date.set_date(2, 29, 2023)

    def test_set_date_preserves_original_on_failure(self):
        test_date = Date(12, 25, 2021)
        with self.assertRaises(ValueError):
            test_date.set_date(4, 31, 2022)
        self.assertEqual((test_date.month, test_date.day, test_date.year), (12, 25, 2021))


class TestLeapYear(unittest.TestCase):
    """Test leap-year methods."""

    def test_instance_leap_year_true(self):
        self.assertTrue(Date(1, 1, 2024).is_leap_year())

    def test_instance_leap_year_false(self):
        self.assertFalse(Date(1, 1, 2023).is_leap_year())

    def test_century_leap_year(self):
        self.assertTrue(Date.is_year_leap(2000))

    def test_century_non_leap_year(self):
        self.assertFalse(Date.is_year_leap(1900))

    def test_static_leap_year(self):
        self.assertTrue(Date.is_year_leap(2024))

    def test_static_non_leap_year(self):
        self.assertFalse(Date.is_year_leap(2023))


class TestLastDay(unittest.TestCase):
    """Test last-day-of-month methods."""

    def test_instance_last_day_31_day_month(self):
        self.assertEqual(Date(7, 1, 2021).last_day(), 31)

    def test_instance_last_day_30_day_month(self):
        self.assertEqual(Date(9, 1, 2021).last_day(), 30)

    def test_instance_last_day_february_non_leap(self):
        self.assertEqual(Date(2, 1, 2023).last_day(), 28)

    def test_instance_last_day_february_leap(self):
        self.assertEqual(Date(2, 1, 2024).last_day(), 29)

    def test_static_last_day(self):
        self.assertEqual(Date.last_day_of_month(7, 2021), 31)
        self.assertEqual(Date.last_day_of_month(9, 2021), 30)
        self.assertEqual(Date.last_day_of_month(2, 2024), 29)
        self.assertEqual(Date.last_day_of_month(2, 2023), 28)

    def test_static_invalid_month(self):
        with self.assertRaises(ValueError):
            Date.last_day_of_month(13, 2021)


class TestFormatting(unittest.TestCase):
    """Test date string formatting methods."""

    def setUp(self):
        self.test_date = Date(12, 25, 2021)

    def test_numeric_string(self):
        self.assertEqual(self.test_date.to_numeric_string(), "12/25/2021")

    def test_month_first_string(self):
        self.assertEqual(self.test_date.to_month_first_string(), "December 25, 2021")

    def test_day_first_string(self):
        self.assertEqual(self.test_date.to_day_first_string(), "25 December 2021")


if __name__ == "__main__":
    unittest.main()
