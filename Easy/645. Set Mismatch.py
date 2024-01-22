class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        t = set()
        for n in nums:
            if n in t:
                dup = n
            t.add(n)

        missing = set(range(1, max(nums))) - t

        if len(missing) == 0:
            missing = {max(nums) + 1}

        return [dup, list(missing)[0]]