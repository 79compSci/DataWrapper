from datetime import date
import calendar


class Date:
    """Represent a validated calendar date using datetime.date.

    Invalid dates raise ValueError. The month, day, and year are
    available through read-only properties.
    """

    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        """Initialize a Date object."""
        self.__date = date(year, month, day)

    @property
    def month(self) -> int:
        """Return the month of the stored date."""
        return self.__date.month

    @property
    def day(self) -> int:
        """Return the day of the stored date."""
        return self.__date.day

    @property
    def year(self) -> int:
        """Return the year of the stored date."""
        return self.__date.year

    def set_date(self, month: int, day: int, year: int) -> None:
        """Replace the stored date with a complete validated date."""
        new_date = date(year, month, day)
        self.__date = new_date

    def is_leap_year(self) -> bool:
        """Return True when the stored year is a leap year."""
        return calendar.isleap(self.year)

    @staticmethod
    def is_year_leap(year: int) -> bool:
        """Return True when the supplied year is a leap year."""
        return calendar.isleap(year)

    def last_day(self) -> int:
        """Return the last valid day of the stored month."""
        return calendar.monthrange(self.year, self.month)[1]

    @staticmethod
    def last_day_of_month(month: int, year: int) -> int:
        """Return the last valid day of a specified month and year."""
        return calendar.monthrange(year, month)[1]

    def to_numeric_string(self) -> str:
        """Return the date in MM/DD/YYYY format."""
        return self.__date.strftime("%m/%d/%Y")

    def to_month_first_string(self) -> str:
        """Return the date in Month DD, YYYY format."""
        return self.__date.strftime("%B %d, %Y")

    def to_day_first_string(self) -> str:
        """Return the date in DD Month YYYY format."""
        return self.__date.strftime("%d %B %Y")
