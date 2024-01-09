# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def recurs(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return recurs(node.left) + recurs(node.right)
        
        return recurs(root1) == recurs(root2)