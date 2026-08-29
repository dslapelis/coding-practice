from math import prod

import pytest

from product_except_self.solution import Solution


def products_of(nums):
    """Call the solution and assert it returned a list of the right shape."""
    result = Solution().productExceptSelf(nums)
    assert isinstance(result, list), f"expected a list of {len(nums)} products, got {result!r}"
    assert len(result) == len(nums), f"expected {len(nums)} products, got {len(result)}"
    assert all(isinstance(x, int) for x in result), f"expected ints, got {result!r}"
    return result


def expected_for(nums):
    """The answer, computed the slow way: one product per index."""
    return [prod(nums[:i] + nums[i + 1 :]) for i in range(len(nums))]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_examples(nums, expected):
    assert products_of(nums) == expected


def test_minimum_length():
    assert products_of([2, 3]) == [3, 2]
    assert products_of([0, 7]) == [7, 0]


def test_negatives():
    assert products_of([-2, -3, -4]) == [12, 8, 6]
    assert products_of([-1, 2, -3, 4]) == [-24, 12, -8, 6]


def test_single_zero():
    """Every index but the zero's is 0; the zero's is the product of the rest."""
    assert products_of([4, 0, 2, 5]) == [0, 40, 0, 0]


def test_zero_at_both_ends():
    assert products_of([0, 3, 4, 0]) == [0, 0, 0, 0]


def test_two_zeroes_make_everything_zero():
    assert products_of([1, 0, 3, 0, 5]) == [0, 0, 0, 0, 0]


def test_all_zeroes():
    assert products_of([0, 0, 0]) == [0, 0, 0]


def test_ones_leave_the_rest_alone():
    assert products_of([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert products_of([1, 1, 5, 1]) == [5, 5, 1, 5]


def test_duplicates_that_are_not_special():
    nums = [3, 3, 3, 3, 3]
    assert products_of(nums) == expected_for(nums)


def test_answer_differs_at_both_ends():
    nums = [7, 1, 1, 1, 9]
    assert products_of(nums) == [9, 63, 63, 63, 7]


def test_constraint_bounds_on_values():
    nums = [-30, 30, -30, 30, 1]
    assert products_of(nums) == expected_for(nums)


def test_stays_within_a_32_bit_answer():
    """|answer| climbs to just under 2^31 - values the problem still allows."""
    nums = [2] * 30 + [1]
    result = products_of(nums)
    assert result == expected_for(nums)
    assert max(abs(x) for x in result) < 2**31


def test_input_is_not_mutated():
    nums = [1, 2, 3, 4]
    products_of(nums)
    assert nums == [1, 2, 3, 4]


def test_large_input_is_fast():
    """10^5 elements - a product recomputed per index is ~10^10 multiplications."""
    n = 10**5
    nums = [1] * n
    nums[0] = 2
    nums[n // 2] = 3
    nums[-1] = 5

    result = products_of(nums)
    assert result[0] == 15
    assert result[n // 2] == 10
    assert result[-1] == 6
    assert result[1] == 30
    assert result[n - 2] == 30


def test_large_input_with_a_zero():
    n = 10**5
    nums = [1] * n
    nums[7] = 0
    nums[-3] = 4

    result = products_of(nums)
    assert result[7] == 4
    assert result[-3] == 0
    assert result[0] == 0
    assert sum(result) == 4
