class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        length = len(nums)
        result = [1] * length
        total = 1
        for i in range(length):
            result[i] *= total
