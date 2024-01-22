from functools import cache
class Solution:
    def minFallingPathSum(self, matrix: [[int]]) -> int:
        length, colLength = len(matrix), len(matrix[-1])
        @cache
        def recurs(row, col):
            if row == length:
                return 0
            if col == colLength:
                return float('inf')
            if col == -1:
                return float('inf')
            
            return matrix[row][col] + min(recurs(row + 1, col - 1), recurs(row + 1, col), recurs(row + 1, col + 1))
        
        return min([recurs(0, i) for i in range(length)])