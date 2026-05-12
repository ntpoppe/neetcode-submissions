# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        stack = [root]
        while stack:
            entry = stack.pop()
            if self.dfs(entry, subRoot):
                return True

            if entry.right:
                stack.append(entry.right)
            
            if entry.left:
                stack.append(entry.left)

        return False

    def dfs(self, root1, root2):
        if not root1 and not root2:
            return True 

        if root1 and root2 and root1.val == root2.val:
            return self.dfs(root1.left, root2.left) \
               and self.dfs(root1.right, root2.right)
        else:
            return False
