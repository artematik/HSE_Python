"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/combination-sum/
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remaining: int, combo: List[int], start: int):
            if remaining == 0:
                results.append(list(combo))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(remaining - candidates[i], combo, i)
                combo.pop()

        backtrack(target, [], 0)
        return results
