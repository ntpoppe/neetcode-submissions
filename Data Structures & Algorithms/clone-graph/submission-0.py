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
            print("entered dfs")
            existing_node = cloned_node_map.get(node.val)
            if existing_node is not None:
                print("existing, returning")
                return

            clone = Node(node.val)
            cloned_node_map[node.val] = clone
            print(f"neighbors for {clone.val}: {node.neighbors}")
            for neighbor in node.neighbors:
                dfs(neighbor)
                clone.neighbors.append(cloned_node_map[neighbor.val])

        dfs(node)
        print(f"{cloned_node_map=}")
        return cloned_node_map[1]
