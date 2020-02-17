#
# 977. Squares of a Sorted Array
#
# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.
#
# Example 1:
# Input: [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
#
# Example 2:
# Input: [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]
import collections


class Solution:
    def sortedSquares(self, A):
        answer = collections.deque()
        le, ri = 0, len(A) - 1

        while le <= ri:
            left, right = abs(A[le]), abs(A[ri])
            if left > right:
                answer.appendleft(left * left)
                le += 1
            else:
                answer.appendleft(right * right)
                ri -= 1

        return list(answer)


s = Solution()
a = [-4, -1, 0, 3, 10]
print(s.sortedSquares(a))
