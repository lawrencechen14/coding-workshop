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
    return max(a, max(b, c)) - min(a, min(b, c))


# Your robot is at 0 on a number line. It decides to move n steps
# but there are a few constraints! If the step he is currently taking is a multiple
# of 3, then he will move 3 positions forward. If the step he is taking 
# is a multiple of 5, then he will move 10 positions back. Also, if the 
# step is a multiple of 15, then he will move 8 positions forward. If the step
# doesn't satisfy any of the above criteria, then simply move 1 position forward.
# Implement the function robot_stepper that will output the final
# position the robot will be at after n steps.
# Examples:
# 
#   >>> robot_stepper(1)
#   1
#   >>> robot_stepper(3)
#   5
#   >>> robot_stepper(10)
#   -6

def robot_stepper(n):
    sum = 0
    i = 1
    while (i < n + 1):
        if (i % 3 == 0 and i % 5 == 0):
            sum += 8
        elif (i % 3 == 0):
            sum += 3
        elif (i % 5 == 0):
            sum -= 10
        else:
            sum += 1
        i += 1
    return sum

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
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
