class Solution:
    cache = dict()
    maximum = 1

    def lengthOfLIS(self, nums, i=-1):
        if i == -1:
            i = len(nums)
        
        current = 1

        if i in self.cache:
            return self.cache[i]

        if i == 0:
            self.cache[i] = current
            return current

        for j in range(i):
            res = self.lengthOfLIS(nums, j)
            if nums[j-1] > nums[i-1] and res +1 > current:
                current = res + 1

        self.maximum = max(self.maximum, current)
        self.cache[i] = current

        return current
    
sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]), sol.maximum)
sol.maximum = 0
print(sol.lengthOfLIS([0,1,0,3,2,3]), sol.maximum)
sol.maximum = 0
print(sol.lengthOfLIS([7,7,7,7,7,7,7]), sol.maximum)