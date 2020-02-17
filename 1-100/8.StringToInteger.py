#
# 8. String to Integer (atoi)
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace character as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional character after those that from the integer
# number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#     Only the space character ' ' is considered as whitespace character.
#
#     Assume we are dealing with an environment which could only store integers
#     within the 32-bit signed integer range: [-2^31, 2^31 - 1]. If the
#     numerical value is out if the range of representable values,
#     INT_MAX (2^31 - 1) or INT_MIN (-2^31) is returned.
#
# Example 1:
#     Input: '42'
#     Output: 42
#
# Example 2:
#     Input: '    -42'
#     Output: -42
#
# Example 3:
#     Input: '4139 with words'
#     Output: 4139
#
# Example 4:
#     Input: 'words and 987'
#     Output: 0
#
# Example 5:
#     Input: '-91283472332'
#     Output: -2147483648
#
# Attention:
#     +-2


class Solution:
    def myAtoi(self, s: str) -> int:
        sign, res = 1, 0
        s = s.lstrip()
        if s and s[0] == '-':
            sign = -1
        if s and (s[0] == '+' or s[0] == '-'):
            s = s[1:]

        for c in s:
            if not c.isdigit():
                break
            res = res * 10 + int(c)
        res = max(min(res * sign, 2 ** 31 - 1), -2 ** 31)
        return res
