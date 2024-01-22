from functools import cache

class Solution:
    def rob(self, nums: [int]) -> int:
        length = len(nums)

        @cache
        def recurs(index):
            if index >= length:
                return 0
            if index == length - 1:
                return nums[index]
            
            return max(nums[index] + recurs(index + 2), nums[index + 1] + recurs(index + 3))

        return recurs(0)