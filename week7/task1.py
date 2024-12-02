"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0

        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in char_count:
            if char_count[char] < k:
                return max(
                    self.longestSubstring(substring, k) for substring in s.split(char)
                )

        return len(s)