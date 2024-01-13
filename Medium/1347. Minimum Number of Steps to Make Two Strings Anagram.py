from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        tCount = Counter(t)


        intersection = (sCount & tCount)
        return len(s) - intersection.total()
