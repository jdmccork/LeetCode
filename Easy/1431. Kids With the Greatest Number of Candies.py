class Solution:
    def kidsWithCandies(self, candies, extraCandies: int) -> [bool]:
        return [x + extraCandies >= max(candies) for x in candies]
    
sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3], 3))