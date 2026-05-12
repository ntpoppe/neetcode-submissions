# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        sublists = []

        queue = [root]
        while queue:
            sublist = []
            for_queue = []

            while queue:
                pop = queue.pop(0)
                sublist.append(pop.val)
                if pop.left:
                    for_queue.append(pop.left)
                if pop.right:
                    for_queue.append(pop.right)
                
            sublists.append(sublist)
            queue = for_queue

        return sublists