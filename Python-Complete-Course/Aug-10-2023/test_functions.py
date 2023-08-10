from unittest import TestCase
from functions import divide, multiply

class TestFunctions(TestCase):
    def test_divide_result(self):
        divident = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(divident,divisor),expected_result,delta=0.0001)
    
    def test_divide_negative(self):
        divident = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(divident,divisor),expected_result,delta=0.0001)

    def test_divide_divident_zero(self):
        divident = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(divident,divisor),expected_result)

    def test_divide_error_on_zero(self):
        with self.assertRaises(ValueError):
            divide(25,0)
    
    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()
    
    def test_multiply_single_value(self):
        expected= 17
        self.assertEqual(multiply(expected),expected)
    
    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected),expected)
    
    def test_multiply_result(self):
        inputs = (4,5)
        expected =20
        self.assertEqual(multiply(*inputs),expected)

    def test_multiply_result_with_zer0(self):
        inputs = (4,5,0)
        expected =0
        self.assertEqual(multiply(*inputs),expected)
    
    def test_multiply_negative(self):
        inputs = (4,-5)
        expected =-20
        self.assertEqual(multiply(*inputs),expected)
    
    def test_multiply_floats(self):
        inputs = (4.0,5)
        expected =20.0
        self.assertEqual(multiply(*inputs),expected)