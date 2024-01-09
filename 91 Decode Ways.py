from functools import lru_cache
class Solution(object):
    @lru_cache
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        if len(s) == 0:
            return 1

        if int(s[0]) == 0:
            return 0

        if len(s) == 1:
            return 1
        
        total += self.numDecodings(s[1:])
        if(int(s[0]) == 1 or (len(s) >= 2 and int(s[0]) == 2 and int(s[1]) <= 6)):
            total += self.numDecodings(s[2:])
        
        return total

test = Solution()
print(test.numDecodings("226"))