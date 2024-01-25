# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        def recurs(node, most):
            if node == None:
                return 0
            
            if most > node.val:
                total = 0
            else:
                most = node.val
                total = 1
            
            total += recurs(node.left, most) + recurs(node.right, most)
            return total
        
        return recurs(root, root.val) 