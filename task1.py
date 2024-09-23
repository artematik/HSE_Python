"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        row = 0
        direction = 0

        for char in s:
            rows[row] += char
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = 0

            row += 1 if direction else -1

        return ''.join(rows)
