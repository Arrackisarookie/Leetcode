#
# 13. Roman to Integer
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M
#
#    Symbols    Value
#
#       I           1
#       V           5
#       X          10
#       L          50
#       C         100
#       D         500
#       M        1000
#
# For example, two is written as II in Roman numeral, just two one's added
# together.
# Twelve is written as, XII, which is simply X + II. The number twenty seven is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, number four is written as
# IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six
# instances where subtraction is used:
#
#     - I can be placed before V and X to make 4 and 9.
#     - X can be placed before L and C to make 40 and 90.
#     - C can be placed before D and M to make 400 and 900.
#
# Given a roman numeral, convert it to an integer. Input is guaranteed to be
# within the range from 1 to 3999.
#
# Example 1:
#     Input: "III"
#     Output: 3
#
# Example 2:
#     Input: "IV"
#     Output: 4
#
# Example 3:
#     Input: "IX"
#     Output: 9
#
# Example 4:
#     Input: "LVIII"
#     Output: 58
#
# Example 5:
#     Input: "MCMXCIV"
#     Output: 1994
#


class Solution(object):
    # 遍历字符串始终累加，
    # 当前一字符对应数字比当前字符对应数字小时，
    # 结果减二倍前一字符对应数字
    def romanToInt(self, s):
        mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        res = 0
        front = mapping[s[0]] if s else 0
        for c in s:
            res += mapping[c]
            if front < mapping[c]:
                res -= 2 * front
            front = mapping[c]
        return res

    # 分为单个和两个，两种情况
    def romanToInt2(self, s):
        doubles = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        singles = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, i, length = 0, 0, len(s)
        while i < length:
            if i < length - 1 and s[i:i + 2] in doubles:
                res += doubles[s[i:i + 2]]
                i += 2
            else:
                res += singles[s[i]]
                i += 1
        return res
