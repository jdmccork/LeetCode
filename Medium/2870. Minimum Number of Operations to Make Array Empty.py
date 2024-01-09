import collections

class Solution:
    def minOperations(self, nums):
        count = collections.Counter(nums)
        total = 0
        for i in count.values():
            if i == 1:
                return -1
            if i % 3 == 1:
                if (i - 4) % 3 == 0:
                    total += ((i - 4) // 3) + 2
                else:
                    return -1
            else:
                total += i//3 + ((i%3) // 2)
                
        return total

sol = Solution()

print(sol.minOperations([2,1,2,2,3,3]))
# print(sol.minOperations([19,19,19,19,19,19,19,19,19,19,19,19,19]))