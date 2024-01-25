# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache


class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        @cache
        def recurs(node, currentSum):
            if node == None:
                return 0


        return recurs(root, 0)
