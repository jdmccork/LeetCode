from collections import defaultdict
class Solution:
    def findWinners(self, matches: [[int]]) -> [[int]]:
        zero = defaultdict()
        one = defaultdict()
        other = defaultdict()

        for match in matches:
            win, lose = match
            if win not in other and win not in one:
                zero[win] = True
            
            if lose not in other:
                if lose in zero:
                    zero.pop(lose)
                if lose in one:
                    one.pop(lose)
                    other[lose] = True
                else:
                    one[lose] = True
        return [sorted(zero.keys()), sorted(one.keys())]

sol = Solution()
print(sol.findWinners(matches = [[1,2],[2,1]]))