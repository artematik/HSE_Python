"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = [""]

        for digit in digits:
            letters = chars[digit]
            modified_ans = []

            for combination in ans:
                for letter in letters:
                    modified_ans.append(combination + letter)

            ans = modified_ans

        return ans
