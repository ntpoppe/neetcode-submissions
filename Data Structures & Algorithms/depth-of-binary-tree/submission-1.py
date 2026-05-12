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
            if not top.left and not top.right:
                max_depth = max(max_depth, depth)
                continue

            if top.right:
                stack.append((top.right, depth + 1))
            if top.left:
                stack.append((top.left, depth + 1))
            

        return max_depth
            