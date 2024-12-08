"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        total_slices = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                count += 1
                total_slices += count
            else:
                count = 0

        return total_slices