import unittest


# Find the product of all numbers from 0 to N
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class TestFac(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(factorial(5), 120, "120")

    def test_n_is_int(self):
        self.assertIsInstance(factorial(1), int, "True")

    def test_n_is_float(self):
        self.assertIsInstance(factorial(2), float, "Failed")

    def test_n_is_str(self):
        self.assertIsInstance(factorial(2), str, "Failed")


# Function Remove spaces at the beginning and end of a string
def delete_space(string):
    if type(string) == str:
        return f"{string}".strip()
    else:
        return f"something wrong {string}"


class TestDeleteSpace(unittest.TestCase):
    def test_delete_space_at_the_beginning(self):
        self.assertEqual(delete_space(" Hello"), "Hello", "True")

    def test_delete_space_at_the_end(self):
        self.assertEqual(delete_space("Hello "), "Hello", "True")

    def test_delete_space_at_the_beginning_and_end(self):
        self.assertEqual(delete_space(" Hello "), "Hello", "True")

    def test_delete_space_at_the_beginning_int(self):
        self.assertEqual(delete_space(int(" 11")), "11", "Wrong data")

    def test_delete_space_at_the_end_int(self):
        self.assertEqual(delete_space(int("11 ")), "11", "Wrong data")


# Find the sum of all integers from A to B inclusive
def sum_integers(a, b):
    total = 0
    if type(a) == str or type(b) == str:
        return a + b
    else:
        try:
            if a > b:
                a, b = b, a

            for i in range(a, b + 1):
                total += i
        except:
            raise TypeError("Type is not integer or string")

    return total


class TestSumIntegers(unittest.TestCase):
    def test_value_b_more_a(self):
        self.assertEqual(sum_integers(1, 5), 15, "Passed")

    def test_return_int(self):
        self.assertIsInstance(sum_integers(1, 2), int, "Passed")

    def test_value_a_more_b(self):
        self.assertEqual(sum_integers(5, 1), 15, "Failed")

    def test_string_value(self):
        self.assertEqual(sum_integers("1", "5"), "15", "Failed")

    def test_float_value(self):
        self.assertEqual(sum_integers(1.1, 5.5), 16.0, "Failed")


# Function of find years for s1 less than 10 percent of s2
def area_calculation(s_one, s_two):
    if type(s_one) and type(s_two) == int:
        year = 1
        while s_one > 0.1 * s_two:
            s_one *= 2
            s_two *= 3
            year += 1
        print(f"First area: {s_one}")
        print(f"Second area: {s_two}")
        print(f"In {year} year")
        return s_one, s_two, year
    else:
        return "Error"


class TestArea(unittest.TestCase):
    def test_value_int_positive(self):
        self.assertEqual(area_calculation(1, 2), (16, 162, 5), "Passed")
        self.assertEqual(area_calculation(-1, 2), (-1, 2, 1), "Bug")
        self.assertEqual(area_calculation(0, 2), (0, 2, 1), "Bug")

    def test_value_int_negative(self):
        self.assertEqual(area_calculation(1, -2), "Error")
        self.assertEqual(area_calculation(1, 0), "Error")
