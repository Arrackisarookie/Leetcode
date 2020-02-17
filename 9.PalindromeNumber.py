#
# 9. Palindrome Number
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# same backward as forward.
#
# Example 1:
#     Input: 121
#     Output: True
#
# Example 2:
#     Input: -121
#     Output: False
#
# Example 1:
#     Input: 10
#     Output: False
#
# Follow up:
# Could you solve it without converting the integer to a string?
# HeHe..
# Absolutely not.


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     s = str(x)
    #     left, right = 0, len(s) - 1
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_num = 0
        while x > reverted_num:
            reverted_num = reverted_num * 10 + x % 10
            x //= 10

        # 处于中位的数字不影响回文，故当数字长度为奇数时，
        #   可以通过 revertedNumber/10 去除处于中位的数字。
        # 例如，当输入为 12321 时
        #   在 while 循环的末尾可以得到 x = 12，revertedNumber = 123，
        return x == reverted_num or x == reverted_num // 10
