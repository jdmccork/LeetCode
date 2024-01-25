from math import ceil

class Solution:
    def successfulPairs(self, spells: [int], potions: [int], success: int) -> [int]:
        m = len(potions)
        result = []
        def binSearch(low, high, target):
            while low <= high:
                current = (low + high) // 2
                if current == m:
                    return m
                match potions[current] > target:
                    case True:
                        high = current - 1
                    case False:
                        if potions[current] == target:
                            return current
                        low = current + 1
            return current
                

        for spell in spells:
            result.append(m - binSearch(0, len(potions), ceil(success / spell)))
        return result