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

        if p and not q:
            return False

        if not p and q:
            return False

        if q.val != p.val:
            return False

        if not self.isSameTree(q.left, p.left):
            return False

        if not self.isSameTree(q.right, p.right):
            return False

        return True