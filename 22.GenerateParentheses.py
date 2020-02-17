#
# 22. Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
# Example:
#     Input: 3
#     Output: [
#               "((()))",
#               "(()())",
#               "(())()",
#               "()(())",
#               "()()()",
#             ]
#


class Solution(object):
    # 回溯
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        if n > 0:
            self.backtrack('', 0, 0, n)
        return self.res

    def backtrack(self, combination, opened, closed, n):
        """
        :type combination: str
        :type opened: int
        :type closed: int
        :type n: int
        """
        if len(combination) == n * 2:
            self.res.append(combination)
        else:
            if opened < n:
                self.backtrack(combination + '(', opened + 1, closed, n)
            if closed < opened:
                self.backtrack(combination + ')', opened, closed + 1, n)
