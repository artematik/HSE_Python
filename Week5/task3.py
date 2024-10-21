"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
