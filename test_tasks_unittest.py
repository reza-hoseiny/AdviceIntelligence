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

if __name__ == '__main__':
    unittest.main()
