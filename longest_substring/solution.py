"""Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate
characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a
    substring.

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # recording the longest substring we have across runs
        longest = 0

        # recording the chars we have seen this turn
        seen_char: dict[str, int] = {}

        left = 0
        for index, value in enumerate(s):
            # breakpoint()
            if seen_char.get(value) is None:
                seen_char[value] = index
                longest = max(index - left + 1, longest)
            else:
                if seen_char[value] < left:
                    longest = max(index - left + 1, longest)
                    continue
                left = seen_char[value] + 1
                seen_char[value] = index
                longest = max(index - left + 1, longest)
        return longest



if __name__ == "__main__":
    solution = Solution()
    for s in "abcabcbb", "bbbbb", "pwwkew":
        print(f"s={s!r} -> {solution.lengthOfLongestSubstring(s)}")
