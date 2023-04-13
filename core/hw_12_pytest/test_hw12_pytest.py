import pytest

from core.hw_3_hw_4.hw_3 import delete_space
from core.hw_3_hw_4.hw_4 import number_product, area_calculation, plus_in_range


class TestDelete:
    @pytest.mark.parametrize(
        "value,expected_value",
        [
            (" Hello", "Hello"),
            ("Hello ", "Hello"),
            (" Hello ", "Hello"),
            (11, "Error"),
            ("", ""),
            ("   ", ""),
        ],
    )
    def test_delete_space(self, value, expected_value):
        assert delete_space(value) == expected_value


class TestNumberProduct:
    @pytest.mark.parametrize(
        "value,expected_value", [
            (5, 120),
            ("string", "Error"),
            (1.1, "Error"),
            (-1, 1),
            (10, 3628800)
        ]
    )
    def test_number_product(self, value, expected_value):
        assert number_product(value) == expected_value


class TestAreaCalculation:
    @pytest.mark.parametrize(
        "first_value,second_value,result",
        [
            [1, 5, (4, 45, 3)],
            [1, 5, (4, 45, 3)],
            [1, 99, (1, 99, 1)],
            [1, 100, (1, 100, 1)],
            [1, 2, (16, 162, 5)],
            [-1, 2, "Error"],
            [0, 2, "Error"],
        ],
    )
    def test_area_calculation(self, first_value, second_value, result):
        res = area_calculation(first_value, second_value)
        assert res == result


class TestPlusInRange:
    @pytest.mark.parametrize(
        "first_value,second_value,result",
        [
            [1, 5, 15],
            [-1, 2, "Error"],
            [5, 1, 15],
            ["1", "5", "Error"],
            [1, "5", "Error"],
            [1.1, 5.5, "Error"],
        ],
    )
    def test_plus_in_range(self, first_value, second_value, result):
        res = plus_in_range(first_value, second_value)
        assert res == result
