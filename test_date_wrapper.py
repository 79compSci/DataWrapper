"""
Unit Test Suite for the Date Wrapper Class
Verifies behaviors, validation constraints, and property mutations.
"""

import unittest
from date_wrapper import Date


class TestDateWrapper(unittest.TestCase):
    """Test assertions targeting structural functionality of the Date class."""

    def test_valid_initialization(self):
        """Ensure valid dates are successfully stored and retrieved via properties."""
        d = Date(10, 24, 2026)
        self.assertEqual(d.month, 10)
        self.assertEqual(d.day, 24)
        self.assertEqual(d.year, 2026)

    def test_invalid_initialization(self):
        """Ensure out-of-bound dates throw a ValueError."""
        # Non-existent calendar days
        with self.assertRaises(ValueError):
            Date(2, 30, 2026)
        # Invalid month
        with self.assertRaises(ValueError):
            Date(13, 1, 2026)

    def test_property_mutations(self):
        """Ensure properties allow individual updates and throw errors if bad."""
        d = Date(5, 15, 2026)

        # Valid mutations
        d.month = 6
        self.assertEqual(d.month, 6)

        # Mutation resulting in an invalid date state (e.g. June 31st doesn't exist)
        with self.assertRaises(ValueError):
            d.day = 31

    def test_leap_year_detection(self):
        """Verify leap-year status using known leap and non-leap years."""
        leap_date = Date(1, 1, 2024)  # 2024 was a leap year
        non_leap_date = Date(1, 1, 2026)  # 2026 is not a leap year

        self.assertTrue(leap_date.is_leap_year)
        self.assertFalse(non_leap_date.is_leap_year)

    def test_days_in_month(self):
        """Verify handling of month lengths including leap year alterations."""
        d = Date(2, 1, 2026)  # Feb 2026 -> 28 days
        self.assertEqual(d.days_in_month, 28)

        d_leap = Date(2, 1, 2024)  # Feb 2024 -> 29 days
        self.assertEqual(d_leap.days_in_month, 29)

    def test_string_formatting(self):
        """Verify fallback string outputs."""
        d = Date(9, 20, 2026)
        self.assertEqual(str(d), "09/20/2026")


if __name__ == "__main__":
    unittest.main()
