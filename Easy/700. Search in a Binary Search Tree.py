# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val: int):
        node = root
        while node:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.left
            else:
                return node