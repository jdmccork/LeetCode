class Solution:
    def findDifference(self, nums1: [int], nums2: [int]) -> [[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        return [n1.difference(n2), n2.difference(n1)]