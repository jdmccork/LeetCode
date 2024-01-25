from functools import cache
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def recurs(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            return recurs(n-1) + recurs(n-2) + recurs(n-3)
        return recurs(n)