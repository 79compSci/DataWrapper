import unittest
from date_class import date_class


class TestDateConstructorAndProperties(unittest.TestCase):
    """Test Date construction and read-only properties."""

    def test_default_constructor(self):
        """The default date should be January 1, 1900."""
        test_date = date_class()

        self.assertEqual(test_date.month, 1)
        self.assertEqual(test_date.day, 1)
        self.assertEqual(test_date.year, 1900)

    def test_valid_date(self):
        """A valid date should store the correct components."""
        test_date = date_class()

        self.assertEqual(test_date.month, 12)
        self.assertEqual(test_date.day, 25)
        self.assertEqual(test_date.year, 2021)

    def test_leap_day(self):
        """February 29 should be accepted during a leap year."""
        test_date = date_class()

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 29)
        self.assertEqual(test_date.year, 2024)

    def test_invalid_month(self):
        """An invalid month should raise ValueError."""
        with self.assertRaises(ValueError):
            date_class()

    def test_invalid_day(self):
        """An invalid day should raise ValueError."""
        with self.assertRaises(ValueError):
            date_class()

    def test_invalid_leap_day(self):
        """February 29 should be rejected during a non-leap year."""
        with self.assertRaises(ValueError):
            date_class()

    def test_zero_month(self):
        """A month of zero should raise ValueError."""
        with self.assertRaises(ValueError):
            date_class()

    def test_zero_day(self):
        """A day of zero should raise ValueError."""
        with self.assertRaises(ValueError):
            date_class()


class TestSetDate(unittest.TestCase):
    """Test replacing the stored date."""

    def test_set_date(self):
        """set_date should replace the entire stored date."""
        test_date = date_class()

        test_date.set_date(12, 25, 2021)

        self.assertEqual(test_date.month, 12)
        self.assertEqual(test_date.day, 25)
        self.assertEqual(test_date.year, 2021)

    def test_set_date_leap_day(self):
        """set_date should accept a valid leap day."""
        test_date = date_class()

        test_date.set_date(2, 29, 2024)

        self.assertEqual(test_date.month, 2)
        self.assertEqual(test_date.day, 29)
        self.assertEqual(test_date.year, 2024)

    def test_set_date_invalid(self):
        """An invalid replacement date should raise ValueError."""
        test_date = date_class()

        with self.assertRaises(ValueError):
            test_date.set_date(2, 29, 2023)

    def test_set_date_preserves_original_on_failure(self):
        """A failed replacement should leave the original date unchanged."""
        test_date = date_class()

        with self.assertRaises(ValueError):
            test_date.set_date(4, 31, 2022)

        self.assertEqual(test_date.month, 12)
        self.assertEqual(test_date.day, 25)
        self.assertEqual(test_date.year, 2021)


class TestLeapYear(unittest.TestCase):
    """Test leap-year methods."""

    def test_instance_leap_year_true(self):
        """The instance method should identify a leap year."""
        test_date = date_class()

        self.assertTrue(test_date.is_leap_year())

    def test_instance_leap_year_false(self):
        """The instance method should identify a non-leap year."""
        test_date = date_class()

        self.assertFalse(test_date.is_leap_year())

    def test_century_leap_year(self):
        """A century year divisible by 400 should be a leap year."""
        self.assertTrue(date_class.is_year_leap(2000))

    def test_century_non_leap_year(self):
        """A century year not divisible by 400 should not be a leap year."""
        self.assertFalse(date_class.is_year_leap(1900))

    def test_static_leap_year(self):
        """The static method should correctly identify a normal leap year."""
        self.assertTrue(date_class.is_year_leap(2024))

    def test_static_non_leap_year(self):
        """The static method should correctly identify a non-leap year."""
        self.assertFalse(date_class.is_year_leap(2023))


class TestLastDay(unittest.TestCase):
    """Test last-day-of-month methods."""

    def test_instance_last_day_31_day_month(self):
        """The instance method should return 31 for a 31-day month."""
        test_date = date_class()

        self.assertEqual(test_date.last_day(), 31)

    def test_instance_last_day_30_day_month(self):
        """The instance method should return 30 for a 30-day month."""
        test_date = date_class()

        self.assertEqual(test_date.last_day(), 30)

    def test_instance_last_day_february_non_leap(self):
        """February should have 28 days in a non-leap year."""
        test_date = date_class()

        self.assertEqual(test_date.last_day(), 28)

    def test_instance_last_day_february_leap(self):
        """February should have 29 days in a leap year."""
        test_date = date_class()

        self.assertEqual(test_date.last_day(), 29)

    def test_static_last_day(self):
        """The static method should return the correct month length."""
        self.assertEqual(date_class.last_day_of_month(7, 2021), 31)
        self.assertEqual(date_class.last_day_of_month(9, 2021), 30)
        self.assertEqual(date_class.last_day_of_month(2, 2024), 29)
        self.assertEqual(date_class.last_day_of_month(2, 2023), 28)

    def test_static_invalid_month(self):
        """An invalid month should raise ValueError."""
        with self.assertRaises(ValueError):
            date_class.last_day_of_month(13, 2021)


class TestFormatting(unittest.TestCase):
    """Test date string formatting methods."""

    def setup(self):
        """Create a date used by the formatting tests."""
        self.test_date = date_class()

    def test_numeric_string(self):
        """The numeric format should be MM/DD/YYYY."""
        self.assertEqual(
            self.test_date.to_numeric_string(),
            "12/25/2021"
        )

    def test_month_first_string(self):
        """The month-first format should include the full month name."""
        self.assertEqual(
            self.test_date.to_month_first_string(),
            "December 25, 2021"
        )

    def test_day_first_string(self):
        """The day-first format should include the full month name."""
        self.assertEqual(
            self.test_date.to_day_first_string(),
            "25 December 2021"
        )


if __name__ == "__main__":
    unittest.main()
