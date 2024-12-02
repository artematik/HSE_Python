"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/max-consecutive-ones-iii/
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, max_length = 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length