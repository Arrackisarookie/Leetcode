#
# 15. Three Sum
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0 ? Find all unique triplets in the array which gives the
# sum of zero.
#
# Note:
#     The solution set must not contain duplicate triplets.
#
# Example:
#     Input: [-1, 0, 1, 2, -1, -4]
#     Output: [[-1, 0, 1], [-1, -1, 2]]
#


class Solution(object):
    # 排序 + 双指针
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        i, length = 0, len(nums)
        while i < length:
            j, k = i + 1, length - 1
            while j < k:
                triple = nums[i] + nums[j] + nums[k]
                if triple == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif triple > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while i < length - 2 and nums[i] == nums[i - 1]:
                i += 1
        return results

    # 哈希表记录数字出现次数 + 分正负 + 减法，判断差是否出现
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        num_times = {}
        negs, poss = [], []

        for n in nums:
            num_times[n] = num_times.get(n, 0) + 1
        for n in num_times:
            if n < 0:
                negs.append(n)
            else:
                poss.append(n)

        if num_times.get(0, 0) >= 3:
            results.append([0, 0, 0])

        for neg in negs:
            for pos in poss:
                diff = 0 - neg - pos
                if diff in num_times:
                    if diff in (neg, pos) and num_times.get(diff) > 1:
                        results.append(neg, pos, diff)
                    elif diff < neg or diff > pos:
                        results.append(neg, pos, diff)
        return results
