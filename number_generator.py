from math import sqrt
from itertools import count, islice

class NumberGenerator:
    def __init__(self, name="simple number generator"):
        pass

    def generate(self, max_range = 1000):
        # Extract elements from the numbers list for which check_even() returns True
        # even_numbers_iterator = filter(check_even, numbers)
        pass

    # returns True if number is even
    def check_even(self, number):
        if (number > 2) and (number % 2 == 0):
              return True

        return False

    # returns True if number is even
    def check_prime(self, number):
        if number < 2:
            return False

        if self.check_even(number):
              return False

        for i in islice(count(2), int(sqrt(number) - 1)):
            if number % i == 0:
                return False

        return True

    # returns True if number is even
    def check_in_Fibonacci(self, number):
        pass
