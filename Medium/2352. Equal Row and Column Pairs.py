import numpy as np
from collections import Counter

class Solution:
    def equalPairs(self, grid: [[int]]) -> int:
        npGrid = np.array(grid)
        rows = Counter(str(l) for l in npGrid)
        total = 0
        
        for i in range(len(grid)):
            column = str(npGrid[:, i])
            if column in rows:
                total += rows[column]
        return total
        