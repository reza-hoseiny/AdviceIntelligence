#!/usr/bin/env python
import unittest #Import unittest from the standard library of python
from number_generator import NumberGenerator
class TestNumberGeneratorMethods(unittest.TestCase):  #every test class must inherit from the TestCase class
    """
    This is the basic test class for the Task 1 class
    Any method which starts with ``test_`` will considered as a test case in the unittest frameowrk...
    """
    def setUp(self):
        self.name = 'A simple number_generator'
        self.max_range = 514229
        self.number_generator = NumberGenerator(self.max_range)

    def test_main(self):
        self.assertEqual(self.number_generator.generate_prime_Fibonacci(), [2, 3, 5, 13, 89, 233, 1597, 28657, 514229])


    def test_is_prime(self):
        self.assertEqual(self.number_generator._check_is_prime(1), False)
        self.assertEqual(self.number_generator._check_is_prime(2), True)
        self.assertEqual(self.number_generator._check_is_prime(3), True)
        self.assertEqual(self.number_generator._check_is_prime(5054), False)
        self.assertEqual(self.number_generator._check_is_prime(5), True)
        self.assertEqual(self.number_generator._check_is_prime(100), False)
        self.assertEqual(self.number_generator._check_is_prime(7919), True)
        self.assertEqual(self.number_generator._check_is_prime(999331), True)
        self.assertEqual(self.number_generator._check_is_prime(112909), True)
        self.assertEqual(self.number_generator._check_is_prime(2097593), True)
        self.assertEqual(self.number_generator._check_is_prime(87178291199), True)

    def test_primes_sieve_eratosthenes(self):
        self.assertEqual(self.number_generator.primes_sieve_eratosthenes(10), [2,3,5,7])
        self.assertEqual(self.number_generator.primes_sieve_eratosthenes(17), [2,3,5,7,11,13,17])
        self.assertEqual(self.number_generator.primes_sieve_eratosthenes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_fibonacci_series(self):
        self.assertEqual(self.number_generator.generate_fibonacci_series(10), [1, 1, 2, 3, 5, 8])
        self.assertEqual(self.number_generator.generate_fibonacci_series(609), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
        self.assertEqual(self.number_generator.generate_fibonacci_series(4181), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])

if __name__ == '__main__':
    unittest.main()
