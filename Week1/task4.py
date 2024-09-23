"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if s == "":
            return 0

        sign = 1
        index = 0

        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        res = 0

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if res > (2**31 - 1) // 10 or (res == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
            
            res = res * 10 + digit
            index += 1

        return sign * res
