# tests/calculator_test.py

import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase): # NEW
    def test_add(self):
        self.assertEqual(7, add(2,5)) 
        self.assertEqual(7, add(5,2)) 
        self.assertEqual(0, add(0,0))
        self.assertEqual(1, add(1,0)) 
        self.assertEqual(1, add(0,1)) 
        self.assertEqual(-1, add(0,-1))
        self.assertEqual(0.25, add(0.125,0.125))

    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))   
        self.assertEqual(0, subtract(1, 1))   
        self.assertEqual(0, subtract(0, 0))   
        self.assertEqual(-1, subtract(0, 1))   
        self.assertEqual(-2, subtract(-1, 1))   
        self.assertEqual(-2, subtract(4, 6))   
        self.assertEqual(1, subtract(0, -1))
        self.assertEqual(1.5, subtract(1, -0.5))    

    def test_multiply(self):
        self.assertEqual(0, multiply(0, 0))   
        self.assertEqual(0, multiply(1, 0))   
        self.assertEqual(1, multiply(1, 1))   
        self.assertEqual(-1, multiply(1, -1))   
        self.assertEqual(-2, multiply(-1, 2))   
        self.assertEqual(2, multiply(-2, -1))   
        self.assertEqual(0, multiply(0, -1))  
        self.assertEqual(2.5, multiply(0.5, 5)) 
        self.assertEqual(2.5, multiply(10, 0.25))  

    def test_divide(self):
        self.assertEqual(1, divide(1, 1))   
        self.assertEqual(-1, divide(1, -1))   
        self.assertEqual(10, divide(10, 1))   
        self.assertEqual(-2, divide(-10, 5))   
        self.assertEqual(10, divide(2.5, 0.25))   
        self.assertEqual(-100, divide(25, -0.25))  
        #self.assertRaises(ZeroDivisionError, divide(0, 0))   
         