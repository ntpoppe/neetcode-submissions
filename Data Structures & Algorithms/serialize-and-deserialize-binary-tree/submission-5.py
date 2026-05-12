# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        
        def dfs(node):
            nonlocal res
            if node:
                res += f"{node.val}|"
                dfs(node.left)
                dfs(node.right)
            else:
                res += f"None|"

        dfs(root)
        res = res[:-1]
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeVals = data.split('|')
        i = -1
        print(nodeVals)

        root = None
        def build_from_dfs():
            nonlocal i

            i += 1
            if i == len(nodeVals):
                return None

            val = nodeVals[i]
            if not val or val == "None":
                return None

            node = TreeNode(int(val))
            node.left = build_from_dfs()
            node.right = build_from_dfs()
            return node

        root = build_from_dfs()
        return root