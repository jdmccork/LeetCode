# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        def recurs(node):
            total = 0

            if node == None:
                return total

            if node.val >= low and node.val <= high:
                total += node.val
            total += recurs(node.left) + recurs(node.right)
            return total
        
        current = root
        while current is not None and current.val not in range(low, high + 1):
            if current.val < low:
                current = current.right
            else:
                current = current.left

        return recurs(current)
            
