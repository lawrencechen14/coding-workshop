# You are given built-in functions max(a, b) and min(a, b).
# max(a, b) returns the greater of a and b.
# Similarly, min(a, b) returns the smaller of a and b.
#
# Examples:
#
#   >>> min(1, 2)
#   1
#   >>> min(2, 1)
#   1
#   >>> max(3, -1)
#   3

# Return the statistical range of a set of three numbers.
# This is the greatest of a, b, and c minus the smallest of
# a, b, and c.
#
# Hint: the maximum of three numbers a, b, and c is:
#
#   max(a, max(b, c))

def range(a, b, c):
    """
    >>> range(4, 2, 1)  # 4 - 1
    3
    >>> range(3, -1, 2)  # 3 - (-1)
    4
    """
    # YOUR CODE HERE #


# Create a function is_leap_year(year) that determines whether
# the given year is a leap year.
#
# A year is a leap year if the year is divisible by four and
# the year is not divisible by 100. However, years divisible
# by 400 are leap years, and are an exception to the 100-year
# rule.
#
#
# Hint: "a % b" calculates the remainder of dividing a by b,
#       so "a % b == 0" is true if a is divisible by b.
#
# NOTE: Run "python -m doctest problems.py" to test.

def is_leap_year(year):
    """
    >>> is_leap_year(301)
    False
    >>> is_leap_year(304)
    True
    >>> is_leap_year(300)
    False
    >>> is_leap_year(400)
    True
    """
    # YOUR CODE HERE #
