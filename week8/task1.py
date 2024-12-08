"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # множество для уникальных элементов
        i = 0  # left pointer
        max_len = 0

        for j in range(len(s)): #  right pointer
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1  # shift left pointer
            char_set.add(s[j])
            max_len = max(max_len, j-i+1)
        return max_len