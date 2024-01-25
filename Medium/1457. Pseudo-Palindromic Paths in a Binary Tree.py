# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def checkPalin(c):
            print(c)
            odds = 0
            for num in c:
                if num % 2 == 1:
                    odds += 1
            if odds < 2:
                return 1
            else:
                return 0
            
        def recurs(d, node):
            total = 0
            c = d.copy()
            if node == None:
                return 0
            c[node.val - 1] += 1
            if node.left == None and node.right == None:
                return checkPalin(c)
            
            total += recurs(c, node.left)
            total += recurs(c, node.right)

            return total

        return recurs([0] * 9, root)