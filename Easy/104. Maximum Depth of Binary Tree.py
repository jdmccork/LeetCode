# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:

        def recurs(node):
            if node == None:
                return 0

            return max(recurs(node.left), recurs(node.right)) + 1
        return recurs(root)