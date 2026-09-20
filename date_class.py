from datetime import date
import calendar


class Date:
    """Represent a validated calendar date using datetime.date.

    Invalid dates raise ValueError. The month, day, and year are
    available through read-only properties.
    """

    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        """Initialize a Date object.

        Args:
            month: The month from 1 through 12.
            day: The valid day for the specified month and year.
            year: The calendar year.

        Raises:
            ValueError: If the supplied values do not represent a valid date.
        """
        self.__date = date(year, month, day)

    @property
    def month(self) -> int:
        """Return the month of the stored date.

        Returns:
            The month as an integer from 1 through 12.
        """
        return self.__date.month

    @property
    def day(self) -> int:
        """Return the day of the stored date.

        Returns:
            The day of the month as an integer.
        """
        return self.__date.day

    @property
    def year(self) -> int:
        """Return the year of the stored date.

        Returns:
            The four-digit calendar year.
        """
        return self.__date.year

    def set_date(self, month: int, day: int, year: int) -> None:
        """Replace the stored date.

        Args:
            month: The new month from 1 through 12.
            day: The valid day for the specified month and year.
            year: The new calendar year.

        Raises:
            ValueError: If the supplied values do not represent a valid date.
        """
        new_date = date(year, month, day)
        self.__date = new_date

    def is_leap_year(self) -> bool:
        """Determine whether the stored year is a leap year.

        Returns:
            True if the stored year is a leap year; otherwise False.
        """
        return calendar.isleap(self.year)

    @staticmethod
    def is_year_leap(year: int) -> bool:
        """Determine whether a supplied year is a leap year.

        Args:
            year: The calendar year to check.

        Returns:
            True if the year is a leap year; otherwise False.
        """
        return calendar.isleap(year)

    def last_day(self) -> int:
        """Return the last valid day of the stored month.

        Returns:
            The final day number in the stored month.
        """
        return calendar.monthrange(self.year, self.month)[1]

    @staticmethod
    def last_day_of_month(month: int, year: int) -> int:
        """Return the last valid day of a specified month and year.

        Args:
            month: The month from 1 through 12.
            year: The calendar year.

        Returns:
            The final day number in the specified month.

        Raises:
            ValueError: If the month is outside the valid range.
        """
        return calendar.monthrange(year, month)[1]

    def to_numeric_string(self) -> str:
        """Return the date in numeric month/day/year format.

        Returns:
            The date formatted as MM/DD/YYYY.
        """
        return self.__date.strftime("%m/%d/%Y")

    def to_month_first_string(self) -> str:
        """Return the date with the month name first.

        Returns:
            The date formatted as Month DD, YYYY.
        """
        return self.__date.strftime("%B %d, %Y")

    def to_day_first_string(self) -> str:
        """Return the date with the day first.

        Returns:
            The date formatted as DD Month YYYY.
        """
        return self.__date.strftime("%d %B %Y")


def date_class():
    return None