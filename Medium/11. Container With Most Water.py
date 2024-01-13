class Solution:
    def maxArea(self, height: [int]) -> int:
        start = 0
        end = len(height) - 1

        area = 0

        while start < end:
            if (t:= min(height[start], height[end]) * (end - start)) > area:
                area = t
            if height[start] > height[end]:
                end += 1
            else:
                start += 1
        return area