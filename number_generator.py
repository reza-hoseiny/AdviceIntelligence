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
    def _check_even(self, number):
        if (number > 2) and (number % 2 == 0):
              return True

        return False

    # returns True if number is even
    def check_prime(self, number):
        if number < 2:
            return False

        if self._check_even(number):
              return False

        for i in islice(count(2), int(sqrt(number) - 1)):
            if number % i == 0:
                return False

        return True

    def primes_sieve_eratosthenes(self, max_range):
        """
        We use Sieve of Eratosthenes method for computing all prime numbers up to a given limit
        """
        limit = max_range+1
        not_prime_num = set()
        prime_nums = []

        for i in range(2, limit):
            if i in not_prime_num:
                continue

            for factor in range(i*2, limit, i):
                # we identify all the multiples of each discovered prime have been marked as composites
                not_prime_num.add(factor)

            prime_nums.append(i)    #the remaining unmarked numbers are primes

        return prime_nums

    # returns True if number is even
    def check_in_Fibonacci(self, number):
        pass
