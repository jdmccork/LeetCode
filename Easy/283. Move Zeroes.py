class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        count = 0
        while i < length - count:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count += 1
            else:
                i += 1