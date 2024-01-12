# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def findNode(node):
            if node is None:
                return None
            if node.val == start:
                return (node, 0)
            else:
                left = findNode(node.left)
                right = findNode(node.right)
                if left != None:
                    return (left[0], left[1] + 1)
                elif right != None:
                    return (right[0], right[1] + 1)
        
        def depth(node):
            if node is None:
                return 0
            else:
                return max(depth(node.left), depth(node.right)) + 1
            
        targetNode, nodeDepth = findNode(root)

        return max(depth(targetNode.left))