# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = self.dfs(root, 1)

        return maxDepth

    def dfs(self, node, curDepth):
        if not node:
            return curDepth

        leftMax, rightMax = curDepth, curDepth
        if node.left:
            leftMax = self.dfs(node.left, curDepth + 1)
        if node.right:
            rightMax = self.dfs(node.right, curDepth + 1)

        return max(leftMax, rightMax)