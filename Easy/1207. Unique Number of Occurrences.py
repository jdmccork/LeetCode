from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        count = Counter(arr)
        return len(count.values()) == len(set(count.values()))