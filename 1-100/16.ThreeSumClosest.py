#
# 16. Three Sum Closest
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
# Example:
#     Input: [-1, 2, 1, -4], 1
#     Output: [-1, 2, 1]
#


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])
        for i, num in enumerate(nums):
            start, end = i + 1, len(nums) - 1
            while start < end:
                tmp = num + nums[start] + nums[end]
                if abs(target - tmp) < abs(target - ans):
                    ans = tmp
                if tmp < target:
                    start += 1
                elif tmp > target:
                    end -= 1
                else:
                    return ans
        return ans
