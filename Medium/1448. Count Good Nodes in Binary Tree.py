# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0

    def goodNodes(self, root) -> int:
        self.recurs(root)
        return self.total
    
    def recurs(self, node):
        if node == None:
            return float('inf')
        if (result := max(self.recurs(node.left), self.recurs(node.right))) > node.val:
            print(node.val)
            self.total += 1
        return min(result, node.val)