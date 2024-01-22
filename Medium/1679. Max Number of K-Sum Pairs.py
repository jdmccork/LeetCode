class Solution:
    def maxOperations(self, nums: [int], k: int) -> int:
        sortedNums = sorted(nums)

        start = 0
        end = len(sortedNums) - 1
        ops = 0

        while start < end:
            if sortedNums[start] + sortedNums[end] > k:
                end -= 1
            elif sortedNums[start] + sortedNums[end] < k:
                start += 1
            else:
                ops += 1
                start += 1
                end -= 1
        return ops
