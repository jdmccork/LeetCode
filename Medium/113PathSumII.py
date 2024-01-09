# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum, path=None):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        if path == None:
            path = []
        paths = []

        if (root.left == None and root.right == None) and root.val == targetSum:
            path.append(root.val)
            return [path]

        paths += self.pathSum(
            root.left, targetSum - root.val, path + [root.val]
        )  # Left
        paths += self.pathSum(
            root.right, targetSum - root.val, path + [root.val]
        )  # Right

        return paths