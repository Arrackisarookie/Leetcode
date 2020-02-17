class Solution:
    def twoSum(self, nums, target):

        # 1. two sum 中的全部适用但都没有用到有序这一特性

        # 双指针

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            two_sum = nums[lo] + nums[hi]
            if two_sum > target:
                hi -= 1
            elif two_sum < target:
                lo += 1
            else:
                return [lo, hi]
        return []
        # Time - O(n)
        # Space - O(1)
