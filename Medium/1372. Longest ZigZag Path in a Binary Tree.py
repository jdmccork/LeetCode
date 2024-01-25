# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root) -> int:
        def recurs(node, left, length):
            if node == None:
                return length
            
            if left:
                zig = max(recurs(node.right, True, length + 1), recurs(node.left, False, 0))
            else:
                zig = max(recurs(node.left, True, length + 1), recurs(node.right, False, 0))

            return zig

        return recurs(root, True, 0)