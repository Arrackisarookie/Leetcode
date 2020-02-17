#
# 17. Letter Combinations of a Phone Number
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Notethat 1 does not map to any letters.
#
# Example:
#     Input: "23"
#     Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# Note:
#     Although the above answer is in lexicographical order, your answer could
#     be in any order you want.
#


class Solution(object):
    # 递归
    def letterCombinations(self, digits):
        """
        type digits: str
        rtype: List[str]
        """
        self.res = []
        if digits:
            self.backtrack('', digits)
        return self.res

    def backtrack(self, combination, next_digits):
        """
        type combination: str
        type next_digits: str
        rtype: List[str]
        """
        alphas = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        if not next_digits:
            self.res.append(combination)
        else:
            for a in alphas[next_digits[0]]:
                self.backtrack(combination + a, next_digits[1:])
