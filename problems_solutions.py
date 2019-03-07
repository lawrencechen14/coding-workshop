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
    """
    >>> robot_stepper(1)
    1
    >>> robot_stepper(3)
    5
    >>> robot_stepper(10)
    -6
    """
    total = 0
    i = 1
    while (i < n + 1):
        if (i % 3 == 0 and i % 5 == 0):
            total += 8
        elif (i % 3 == 0):
            total += 3
        elif (i % 5 == 0):
            total -= 10
        else:
            total += 1
        i += 1
    return total

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


# Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the
# following mathematical puzzle.
#
# Pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Continue this process until n is 1.
# The number n will travel up and down but eventually end at 1 (at least for all
# numbers that have ever been tried -- nobody has ever proved that the sequence
# will terminate). Analogously, a hailstone travels up and down in the atmosphere
# before eventually landing on earth.
#
# This sequence of values of n is often called a Hailstone sequence. Write a
# function that takes a single argument with formal parameter name n, prints out
# the hailstone sequence starting at n, and returns the number of steps in the
# sequence:

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2      # Integer division prevents "1.0" output
        else:
            n = 3 * n + 1
        length = length + 1
    print(n)                # n is now 1
    return length
