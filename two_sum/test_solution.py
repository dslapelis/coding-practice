import pytest

from two_sum.solution import Solution


def check(nums, target):
    """Assert the returned indices are a valid answer and return them sorted."""
    result = Solution().twoSum(nums, target)
    assert result is not None and len(result) == 2, f"expected two indices, got {result!r}"
    i, j = result
    assert i != j, "the same element may not be used twice"
    assert 0 <= i < len(nums) and 0 <= j < len(nums), "indices out of range"
    assert nums[i] + nums[j] == target
    return sorted((i, j))


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_examples(nums, target, expected):
    assert check(nums, target) == expected


def test_minimum_length():
    assert check([1, 2], 3) == [0, 1]


def test_negative_numbers():
    assert check([-3, 4, 3, 90], 0) == [0, 2]


def test_negative_target():
    assert check([-1, -2, -3, -4], -7) == [2, 3]


def test_answer_at_the_ends():
    assert check([5, 1, 1, 1, 6], 11) == [0, 4]


def test_duplicates_that_are_not_the_answer():
    assert check([4, 4, 2, 7], 9) == [2, 3]


def test_zeroes():
    assert check([0, 4, 0], 0) == [0, 2]


def test_constraint_bounds():
    assert check([-(10**9), 10**9, 5], 0) == [0, 1]
    assert check([10**9, 10**9 - 1, 1], 10**9) == [1, 2]


def test_large_input_is_fast():
    """10^4 elements, answer at the very end - too slow for a naive O(n^2) scan."""
    nums = list(range(10**4))
    target = nums[-1] + nums[-2]
    assert check(nums, target) == [len(nums) - 2, len(nums) - 1]
