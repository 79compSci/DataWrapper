from datetime import date, timedelta
import calendar


class Date:
    """Represent a validated calendar date using datetime.date.

    Invalid dates raise ValueError. The month, day, and year are available
    through read-only properties. Date objects support signed subtraction,
    one-day increment and decrement, customized string output, and
    construction from user input.
    """

    def __init__(self, month: int = 1, day: int = 1, year: int = 1900) -> None:
        """Initialize a Date object with a valid month, day, and year."""
        self.__date = date(year, month, day)

    @property
    def month(self) -> int:
        """Return the stored month."""
        return self.__date.month

    @property
    def day(self) -> int:
        """Return the stored day of the month."""
        return self.__date.day

    @property
    def year(self) -> int:
        """Return the stored year."""
        return self.__date.year

    def set_date(self, month: int, day: int, year: int) -> None:
        """Replace the complete stored date, raising ValueError if invalid."""
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
        """Return the date formatted as MM/DD/YYYY."""
        return self.__date.strftime("%m/%d/%Y")

    def to_month_first_string(self) -> str:
        """Return the date formatted as Month D, YYYY."""
        return f"{self.__date:%B} {self.day}, {self.year}"

    def to_day_first_string(self) -> str:
        """Return the date formatted as DD Month YYYY."""
        return self.__date.strftime("%d %B %Y")

    def __sub__(self, other: object) -> int:
        """Return the signed day difference between two Date objects.

        Returns NotImplemented when the right operand is not a Date.
        """
        if not isinstance(other, Date):
            return NotImplemented
        return (self.__date - other.__date).days

    def increment(self) -> "Date":
        """Increase this object by one day, modify it, and return self."""
        self.__date += timedelta(days=1)
        return self

    def decrement(self) -> "Date":
        """Decrease this object by one day, modify it, and return self."""
        self.__date -= timedelta(days=1)
        return self

    def __str__(self) -> str:
        """Return the date formatted as Month D, YYYY."""
        return self.to_month_first_string()

    @classmethod
    def from_input(cls) -> "Date":
        """Create a Date from prompted month, day, and year input.

        The method prompts for all three date components, returns a new
        instance of cls, and allows ValueError to propagate for nonnumeric
        input or an invalid calendar date.
        """
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        year = int(input("Enter year: "))
        return cls(month, day, year)
