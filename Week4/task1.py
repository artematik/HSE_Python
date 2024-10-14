"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 0

        for num in nums:
            if unique_count < 2 or num != nums[unique_count - 2]:
                nums[unique_count] = num
                unique_count += 1

        return unique_count
