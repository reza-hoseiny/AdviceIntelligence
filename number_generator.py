from math import sqrt
from itertools import count, islice

class NumberGenerator:
    def __init__(self, max_range = 1000):
        self.max_range = max_range
        self.fibonacci_series = None
        self.all_primes= None
        self._intersect = None
        self._sum_two_primes_numbers_iterator = None

    def _fill_fibonacci_series_all_primes(self):
        if self.fibonacci_series is None:
            self.fibonacci_series = self.generate_fibonacci_series(self.max_range)
        if self.all_primes is None:
            self.all_primes = self.primes_sieve_eratosthenes(self.max_range)

    def generate_prime_Fibonacci(self):
        self._fill_fibonacci_series_all_primes()
        # Extract elements from the numbers list for which the numbers are both prime  and in the Fibonacci sequence.
        self._intersect_numbers_iterator = filter(self.isPrime, self.fibonacci_series)
        return list(self._intersect_numbers_iterator)

    def generate_sum_two_primes_Fibonacci(self):
        self._fill_fibonacci_series_all_primes()
        # Extract elements from the Fibonacci sequence list for which the numbers are sum of two other primes
        self._sum_two_primes_numbers_iterator = filter(self._is_sum_of_two_prime, self.fibonacci_series)
        return list(self._sum_two_primes_numbers_iterator)

    def print_primeSplit(self):
        print("Fib\t\t\tPrim1\t\t\tPrim2\n----\t\t\t----\t\t\t----")
        if self._sum_two_primes_numbers_iterator is None:
            list_possible = self.generate_sum_two_primes_Fibonacci()
        # print(self._sum_two_primes_numbers_iterator)
        for num in list_possible:
            list = self._primeSplit(num)
            for item in list:
                if item[0] < item[1]:
                    print(num, "\t\t\t", item[0], "\t\t\t", item[1])

    # returns True if number is even
    def _check_even(self, number):
        if (number > 2) and (number % 2 == 0):
              return True

        return False

    # returns True if number is prime
    def isPrime(self, number):
        if number < 2:
            return False

        if self._check_even(number):
              return False

        if self.all_primes is not None:
            if number in self.all_primes:
                return True
        else: #if all_primes is None ie never called sieve_eratosthenes before
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

    def generate_fibonacci_series(self, max_range):
        fib_series = list(self._fib(max_range))
        return fib_series

    def _fib(self, max_range):
        """
        use generator for generating Fibonacci numbers.
        """
        a, b = 1, 1
        while (a <= max_range):
            yield a
            a, b = b, a + b

    def _is_sum_of_two_prime(self, input_number):
        for i in range(2,input_number//2+1):
            if(self.isPrime(i) and self.isPrime(input_number-i)):
                    return True # input_number can be expressed as sum of two prime numbers of i and input_number-i"
        return False

    def _primeSplit(self, input_number):
        output_list = []
        for i in range(2,input_number//2+1):
            if(self.isPrime(i) and self.isPrime(input_number-i)):
                output_list.append((i, input_number-i))
        return output_list
