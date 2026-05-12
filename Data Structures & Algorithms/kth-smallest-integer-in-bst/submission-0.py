# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # left 2i
        # right 2i + 1
        vals = []
        def dfs(node):
            if node:
                vals.append((node.val))
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        vals.sort()
        val = vals[k - 1]
        return val



