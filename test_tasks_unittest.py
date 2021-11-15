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
        self.number_generator = NumberGenerator(self.name)

    def test_main(self):
        self.number_generator.generate(max_range=15)

    def test_is_prime(self):
        self.assertEqual(self.number_generator.check_prime(1), False)
        self.assertEqual(self.number_generator.check_prime(2), True)
        self.assertEqual(self.number_generator.check_prime(3), True)
        self.assertEqual(self.number_generator.check_prime(5054), False)
        self.assertEqual(self.number_generator.check_prime(5), True)
        self.assertEqual(self.number_generator.check_prime(100), False)
        self.assertEqual(self.number_generator.check_prime(7919), True)
        self.assertEqual(self.number_generator.check_prime(999331), True)
        self.assertEqual(self.number_generator.check_prime(112909), True)
        self.assertEqual(self.number_generator.check_prime(2097593), True)
        self.assertEqual(self.number_generator.check_prime(87178291199), True)

    def test_primes_sieve_eratosthenes(self):
        self.assertEqual(self.number_generator.primes_sieve_eratosthenes(10), [2,3,5,7])
        self.assertEqual(self.number_generator.primes_sieve_eratosthenes(17), [2,3,5,7,11,13,17])
        self.assertEqual(self.number_generator.primes_sieve_eratosthenes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == '__main__':
    unittest.main()
