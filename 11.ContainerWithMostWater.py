#
# 11. Container With Most Water
#
# Given n non-negative integer a1, a2, ..., an, where each represents a point
# at coordinate(i, ai).
#
# n vertical lines are drawn such that the two endpoints of line i is at
# (i, ai) and (i, 0).
#
# Find two lines, which together with x-axis forms a container, such that the
# container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                area = max(area, (right - left) * height[left])
                left += 1
            else:
                area = max(area, (right - left) * height[right])
                right -= 1
        return area
