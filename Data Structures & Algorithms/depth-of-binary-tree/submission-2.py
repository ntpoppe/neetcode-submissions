# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        if not root:
            return max_depth
        
        stack = [(root, 1)]
        while stack:
            top, depth = stack.pop()
            if top:
                max_depth = max(max_depth, depth)
                stack.append((top.right, depth + 1))
                stack.append((top.left, depth + 1))
            
        return max_depth
            