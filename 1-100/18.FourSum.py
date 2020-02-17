#
# 18. Four Sum
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target ? Find all unique
# quadruplets in the array which gives the sum of target.
#
# Note:
#     The solution set must not contain duplicate quadruplets.
#
# Example:
#     Input: [1, 0, -1, 0, -2, 2], 0
#     Output: [
#                 [-1,  0, 0, 1],
#                 [-2, -1, 1, 2],
#                 [-2,  0, 0, 2],
#             ]
#


class Solution(object):
    def fourSum(self, nums, target):
        """
        type nums: List[int]
        type targets: int
        rtype: List[List[int]]
        """
        res = []
        nums.sort()
        left, length = 0, len(nums)
        while left < length - 3:
            lmid = left + 1
            while lmid < length - 2:
                rmid, right = lmid + 1, length - 1
                while rmid < right:
                    tmp = nums[left] + nums[lmid] + nums[rmid] + nums[right]
                    if tmp < target:
                        rmid += 1
                        while rmid < right and nums[rmid] == nums[rmid - 1]:
                            rmid += 1
                    elif tmp > target:
                        right -= 1
                        while rmid < right and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        res.append([nums[left], nums[lmid], nums[rmid], nums[right]])
                        right -= 1
                        while rmid < right and nums[right] == nums[right + 1]:
                            right -= 1
                        rmid += 1
                        while rmid < right and nums[rmid] == nums[rmid - 1]:
                            rmid += 1
                lmid += 1
                while lmid < length - 2 and nums[lmid] == nums[lmid - 1]:
                    lmid += 1
            left += 1
            while left < length - 3 and nums[left] == nums[left - 1]:
                left += 1
        return res
