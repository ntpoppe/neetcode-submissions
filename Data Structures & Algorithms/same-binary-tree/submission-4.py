# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
            
        if not p or not q:
            return False

        return self.dfs(p, q)

    def dfs(self, p, q) -> bool:
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        if p.left or q.left:
            return self.dfs(p.left, q.left)
        if p.right or q.right:
            return self.dfs(p.right, q.right)
        
        return True