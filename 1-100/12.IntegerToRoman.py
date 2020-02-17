#
# 12. Integer to Roman
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
# together. Twelve is written as XII, which is simply X + II. The number twenty
# seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six
# instances where substraction is used:
#     - I can be placed before V and X to make 4 and 9.
#     - X can be placed before L and C to make 40 and 90.
#     - C can be placed before D and M to make 400 and 900.
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999
#
# Example 1:
#     Input: 3
#     Output: "III"
#
# Example 2:
#     Input: 4
#     Output: "IV"
#
# Example 3:
#     Input: 9
#     Output: "IX"
#
# Example 4:
#     Input: 58
#     Output: "LVIII"
#
# Example 5:
#     Input: 1994
#     Output: "MCMXCIV"
#


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapping = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        nums = []
        for integer, roman in mapping:
            while num >= integer:
                nums.append(roman)
                num -= integer
        return ''.join(nums)
