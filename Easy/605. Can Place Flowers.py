class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        total = 0
        i=0
        while i < len(flowerbed) and total < n:
            if flowerbed[i] == 1:
                i += 2
                continue

            if i+1 != len(flowerbed) and flowerbed[i + 1] == 1:
                i += 3
            else:
                total += 1
                i += 2

        return total >= n

sol = Solution()
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
print(sol.canPlaceFlowers(flowerbed = [1,0,1,0,0], n = 2))
print(sol.canPlaceFlowers(flowerbed = [0], n = 1))