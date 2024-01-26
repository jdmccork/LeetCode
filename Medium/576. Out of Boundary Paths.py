from functools import cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def recurs(row, col, moves):
            if moves == -1:
                return 0
            if row == -1 or row == m or col == -1 or col == n:
                return 1
            
            newMoves = moves - 1

            mod = 10**9 + 7

            return recurs(row + 1, col, newMoves) % mod + recurs(row - 1, col, newMoves) % mod + recurs(row, col + 1, newMoves) % mod + recurs(row, col - 1, newMoves) % mod
        return recurs(startRow, startColumn, maxMove) % (10**9 + 7)