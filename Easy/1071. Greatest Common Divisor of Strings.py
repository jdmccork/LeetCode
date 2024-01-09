import math
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        else:
            return str1[:math.gcd(len(str1), len(str2))]


sol = Solution()

print(sol.gcdOfStrings("ABC", "ABC"))