from math import sqrt
from itertools import count, islice

class NumberGenerator:
    def __init__(self, max_range = 1000):
        self.max_range = max_range
        self.fibonacci_series = None
        self.all_primes= None
        self._intersect = None

    def generate_prime_Fibonacci(self):
        # Extract elements from the numbers list for which the numbers are both prime
        # and in the Fibonacci sequence.
        self.fibonacci_series = self.generate_fibonacci_series(self.max_range)
        self.all_primes = self.primes_sieve_eratosthenes()
        self._intersect_numbers_iterator = filter(self._check_is_prime, self.fibonacci_series)
        return list(self._intersect_numbers_iterator)


    # returns True if number is even
    def _check_even(self, number):
        if (number > 2) and (number % 2 == 0):
              return True

        return False

    # returns True if number is prime
    def _check_is_prime(self, number):
        if number < 2:
            return False

        if self._check_even(number):
              return False

        if number in self.all_primes:
            return True

        return False

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

    def generate_fibonacci_series(self, max_range):
        fib_series = list(self._fib(max_range))
        return fib_series

    def _fib(self, max_range):
        """
        use generator for generating Fibonacci numbers.
        """
        a, b = 1, 1
        while (a <= max_range):
            print(b)
            yield a
            a, b = b, a + b
