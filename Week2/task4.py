"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-search/
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] != word[index]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )

            board[r][c] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
