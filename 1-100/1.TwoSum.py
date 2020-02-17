class Solution:
    def twoSum(self, nums, target):

        # for i, c in enumerate(nums):
        #     if target - c in nums and c * 2 != target:
        #         return [i, nums.index(target - c)]
        # return []
        # Time - O(n^2) 1200ms
        # Space - O(1)

        # num_to_index = {}
        # for i, c in enumerate(nums):
        #     num_to_index[c] = i
        # for i, c in enumerate(nums):
        #     j = num_to_index.get(target - c)
        #     if j is not None and j != i:
        #         return [i, num_to_index[target - c]]
        # return []
        # Time - O(n) 64ms
        # Space - O(n)

        num_to_index = {}
        for i, c in enumerate(nums):
            if target - c in num_to_index:
                return [num_to_index[target - c], i]
            num_to_index[c] = i
        return []
        # Time O(n) 60ms
