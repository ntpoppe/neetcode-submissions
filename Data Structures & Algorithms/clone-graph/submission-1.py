"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_node_map = {}

        def dfs(node):
            existing_node = cloned_node_map.get(node.val)
            if existing_node is not None:
                return

            clone = Node(node.val)
            cloned_node_map[node.val] = clone
            for neighbor in node.neighbors:
                dfs(neighbor)
                clone.neighbors.append(cloned_node_map[neighbor.val])

        dfs(node)
        return cloned_node_map[1]
