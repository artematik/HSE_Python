"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return s

        start, end = 0, 0
        for i in range(len(s)):
            left, right = i, i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            max_1 = right - left - 1
            
            left, right = i, i + 1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            max_2 = right - left - 1
            max_len = max(max_1, max_2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
