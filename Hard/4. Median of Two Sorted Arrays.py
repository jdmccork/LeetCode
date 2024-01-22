# Fast solution
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1 + len2
        odd = length % 2 == 1
        comb = []

        i1 = 0
        i2 = 0

        while len(comb) < (length // 2 + 1):
            if i1 >= len1:
                comb += nums2[i2:(length // 2 + 1) - len1]
                break
            if i2 >= len2:
                comb += nums1[i1:(length // 2 + 1) - len2]
                break
            comb.append(min(nums1[i1], nums2[i2]))
            if comb[-1] == nums1[i1]:
                i1 += 1
            else:
                i2 += 1

        if odd:
            return comb[-1]
        else:
            return (comb[-2] + comb[-1]) / 2
        

# Space solution
# class Solution:
#     def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
#         l1, l2 = len(nums1), len(nums2)
#         i1, i2 = 0, 0

#         if l1 == 0:
#             median = nums2[0]
#         elif l2 == 0:
#             median = nums1[0]
#         else:
#             median = min(nums1[0], nums2[0])

#         while i1 + i2 < ((l1+l2) // 2) + 1:
#             if i2 >= l2 or nums1[i1] < nums2[i2]:
#                 medianComb = (median + nums1[i1]) / 2
#                 median = nums1[i1]
#                 i1 += 1
#             else:
#                 medianComb = (median + nums2[i2]) / 2
#                 median = nums2[i2]
#                 i2 += 1

#         if l1 + l2 % 2 == 1:
#             return median
#         else:
#             return medianComb