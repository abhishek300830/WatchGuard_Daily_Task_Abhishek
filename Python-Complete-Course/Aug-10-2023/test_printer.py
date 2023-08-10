from unittest import TestCase
from printer import Printer,PrinterError

class TestPrinter(TestCase):

    def setUp(self):
        self.printer = Printer(pages_per_s=2.0,capacity=300)

    def test_print_within_capacity(self):
        message = self.printer.print(25)
        self.assertEqual(f"Printed 25 Pages in 12.50 seconds.",message)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)
    
    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected ="Printed 10 Pages in 5.00 seconds."
        result = self.printer.print(pages)
        self.assertEqual(result,expected)
    
    def test_speed__always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0,capacity=300)
        pages = 11
        expected ="Printed 11 Pages in 3.67 seconds."
        result = fast_printer.print(pages)
        self.assertEqual(result,expected)
    
    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)
    
    def test_multiple_print_runs_ends_up_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)
    
        with self.assertRaises(PrinterError):
            self.printer.print(1)
    