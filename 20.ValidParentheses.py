#
# 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '[', ']', '{', '}',
# determine if the input string is valid.
#
# An input string is valid if:
#     1. Open brackets must be closed by the same type of brackets.
#     2. Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
#     Input: "()"
#     Output: true
#
# Example 2:
#     Input: "()[]{}"
#     Output: true
#
# Example 3:
#     Input: "(]"
#     Output: false
#
# Example 4:
#     Input: "([)]"
#     Output: false
#
# Example 5:
#     Input: "{[]}"
#     Output: true
#


class Solution(object):
    def isValid(self, s):
        """
        type s: str
        rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in mapping:
                top = stack.pop() if stack else '#'
                if mapping[c] != top:
                    return False
            else:
                stack.append(c)

        return not stack
