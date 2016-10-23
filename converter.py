#!/usr/bin/python3

"""
converter, due 10/16: Write a program that converts areas from acres to square miles and vice versa. Use the Test Driven method (write the tests first) and accept only positive real numbers.
"""

import unittest


class test_Converter(unittest.TestCase):
    def test_toMiles(self):
        self.assertAlmostEqual(Converter.toMiles(25), 9.65255, places=5)
        self.assertAlmostEqual(Converter.toMiles(41.4398), 16, places=5)
        with self.assertRaises(TypeError):
            Converter.toMiles('20')
        with self.assertRaises(DegreeException):
            Converter.toMiles(0)
        with self.assertRaises(DegreeException):
            Converter.toMiles(-5)
        with self.assertRaises(TypeError):
            Converter.toMiles(5j)
            
    def test_toKM(self):
        self.assertAlmostEqual(Converter.toKM(1), 2.58999, places=5)
        self.assertAlmostEqual(Converter.toKM(3.86102), 10, places=5)
        with self.assertRaises(TypeError):
            Converter.toKM('20')
        with self.assertRaises(DegreeException):
            Converter.toKM(0)
        with self.assertRaises(DegreeException):
            Converter.toKM(-5)
        with self.assertRaises(TypeError):
            Converter.toKM(15j)
            

class DegreeException(Exception):
    pass


class Converter():
    def checkPositiveNum(area):
        if area <= 0:
            raise DegreeException("Area has to be a positive number")
    
    def toMiles(area):
        Converter.checkPositiveNum(area)
        return area / 2.58998811
        
    def toKM(area):
        Converter.checkPositiveNum(area)
        return area * 2.58998811



unittest.main(verbosity=2)