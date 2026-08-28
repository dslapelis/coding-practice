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

        # iterate through the string, from every char in the string
        for i in range(len(s)):
            curr_char = s[i]
            curr_longest = 1
            seen_char[curr_char] = 1

            for j in s[i+1:]:
                # if we havent yet seen the next char, add it to dict and bump curr_longest
                if seen_char.get(j) is None:
                    seen_char[j] = 1
                    curr_longest += 1
                else:
                    # if we have seen the next char, check if our current longest is > 
                    # total longest, reset seen_char, and reset curr_longest
                    longest = max(longest, curr_longest)
                    seen_char = {}
                    curr_longest = 0
                    break
            # if we get through all of the rest of the string without resetting, record 
            # longest and reset seen_char
            longest = max(longest, curr_longest)
            seen_char = {}

        return longest



if __name__ == "__main__":
    solution = Solution()
    for s in "abcabcbb", "bbbbb", "pwwkew":
        print(f"s={s!r} -> {solution.lengthOfLongestSubstring(s)}")
