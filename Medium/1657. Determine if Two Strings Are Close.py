from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        return sorted(count1.values()) == sorted(count2.values())


sol = Solution()

print(sol.closeStrings("abc", "bca"))
print(sol.closeStrings("cabbba", "abbccc"))
print(sol.closeStrings("cabbba", "aabbss"))