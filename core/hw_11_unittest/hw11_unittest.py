import unittest

from core.hw_3_hw_4.hw_3 import delete_space
from core.hw_3_hw_4.hw_4 import number_product, area_calculation, plus_in_range


class TestFac(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(number_product(5), 120, "N != 120")

    def test_n_is_int(self):
        self.assertIsInstance(number_product(1), int, "Data is not integer")

    def test_n_is_float(self):
        self.assertIsInstance(number_product(2), float, "Data can't be a float")

    def test_n_is_str(self):
        self.assertIsInstance(number_product("2"), str, "Data can't be a string")


class TestDeleteSpace(unittest.TestCase):
    def test_delete_space_at_the_beginning(self):
        self.assertEqual(delete_space(" Hello"), "Hello", "data is not string")

    def test_delete_space_at_the_end(self):
        self.assertEqual(delete_space("Hello "), "Hello", "data is not string")

    def test_delete_space_at_the_beginning_and_end(self):
        self.assertEqual(delete_space(" Hello "), "Hello", "data is not string")

    def test_delete_space_at_the_beginning_int(self):
        self.assertEqual(delete_space(int(" 11")), "11", "Data can't be a int")

    def test_delete_space_at_the_end_int(self):
        self.assertEqual(delete_space(int("11 ")), "11", "Data can't be a int")


# Find the sum of all integers from A to B inclusive


class TestSumIntegers(unittest.TestCase):
    def test_value_b_more_a(self):
        self.assertEqual(plus_in_range(1, 5), 15, "A more then B")

    def test_negative_values(self):
        self.assertEqual(plus_in_range(-1, 2), "Error", "Some value is < 0")

    def test_return_int(self):
        self.assertIsInstance(plus_in_range(1, 2), int, "Returned data is not integer")

    def test_value_a_more_b(self):
        self.assertEqual(
            plus_in_range(5, 1), 15, "First value can't be more then second value"
        )

    def test_string_value(self):
        self.assertEqual(plus_in_range("1", "5"), "15", "Values can't be a string")

    def test_float_value(self):
        self.assertEqual(plus_in_range(1.1, 5.5), 16.0, "Values can't be a float")


class TestArea(unittest.TestCase):
    def test_value_int(self):
        self.assertEqual(
            area_calculation(1, 2), (16, 162, 5), "Expected result != actual result"
        )

    @unittest.expectedFailure
    def test_first_val_is_negative(self):
        self.assertEqual(
            area_calculation(-1, 2), (-1, 2, 1), "Bug: first value is can't be negative"
        )

    @unittest.expectedFailure
    def test_first_val_is_zero(self):
        self.assertEqual(
            area_calculation(0, 2), (0, 2, 1), "Bug: first value is can't be zero"
        )

    @unittest.skip("Bug: Infinite loop")
    def test_second_val_is_zero(self):
        self.assertEqual(
            area_calculation(1, 0),
            (1, 0, 1),
            "Bug: second value is can't be zero. Infinite loop",
        )

    def test_second_val_is_negative(self):
        self.assertEqual(
            area_calculation(1, -2), (1, -2, 1), "Second value is can't be negative"
        )
