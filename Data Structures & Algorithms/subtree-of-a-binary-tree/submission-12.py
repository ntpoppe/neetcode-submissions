# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        stack = [root]
        while stack:
            popped = stack.pop()
            if popped:
                if popped.val == subRoot.val:
                    if self.checkSubroot(popped, subRoot):
                        return True

                if popped.right:
                    stack.append(popped.right)
                if popped.left:
                    stack.append(popped.left)

        print("returning false")
        return False

    def checkSubroot(self, node: Optional[TreeNode], subRoot: TreeNode) -> bool:
        print("entered")

        if node and not subRoot:
            return False

        if not node and subRoot:
            return False

        if not node and not subRoot:
            return True

        if node.val != subRoot.val:
            print("equal")
            return False

        return self.checkSubroot(node.left, subRoot.left) and self.checkSubroot(node.right, subRoot.right)