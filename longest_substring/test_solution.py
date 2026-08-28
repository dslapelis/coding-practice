import string

import pytest

from longest_substring.solution import Solution


def length_of(s):
    """Call the solution and assert it returned something int-shaped."""
    result = Solution().lengthOfLongestSubstring(s)
    assert isinstance(result, int), f"expected an int, got {result!r}"
    assert 0 <= result <= len(s), f"{result} is not a possible length for a {len(s)}-char string"
    return result


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_examples(s, expected):
    assert length_of(s) == expected


def test_empty_string():
    assert length_of("") == 0


def test_single_character():
    assert length_of("a") == 1


def test_all_unique():
    assert length_of("abcdef") == 6


def test_all_identical():
    assert length_of("aaaaaaaa") == 1


def test_answer_at_the_start():
    assert length_of("abcdeaaaa") == 5


def test_answer_at_the_end():
    assert length_of("aaaaabcde") == 5


@pytest.mark.parametrize("s, expected", [("abba", 2), ("dvdf", 3), ("tmmzuxt", 5)])
def test_repeat_outside_the_current_window(s, expected):
    """The duplicate is behind the window's left edge and must not drag it backwards."""
    assert length_of(s) == expected


def test_spaces_digits_and_symbols():
    assert length_of("a b!c#1 2") == 7
    assert length_of("   ") == 1


def test_case_is_significant():
    assert length_of("aA") == 2


def test_long_run_between_two_duplicates():
    assert length_of("z" + string.ascii_lowercase[:-1] + "z") == 26


def test_constraint_bounds():
    """5 * 10^4 characters, the stated maximum."""
    assert length_of("a" * 50_000) == 1

    alphabet = (string.ascii_letters + string.digits + string.punctuation)[:90]
    s = (alphabet * (50_000 // len(alphabet) + 1))[:50_000]
    assert length_of(s) == len(alphabet)


def test_large_input_is_fast():
    """A 90-char window sliding over 5 * 10^4 characters, answer at the very end.

    Re-scanning the window on every character is ~4.5M operations here; a solution
    that never looks backwards does 5 * 10^4.
    """
    alphabet = (string.ascii_letters + string.digits + string.punctuation)[:90]
    filler = (alphabet[:89] * (50_000 // 89 + 1))[: 50_000 - len(alphabet)]
    assert length_of(filler + alphabet) == len(alphabet)
