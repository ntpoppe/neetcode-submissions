class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # What is a valid tree?
        # 1. There are no cycles. (2nd example has cycle)
        # 2. All nodes must be connected.
        
        # Adjacency list // map node to neighbors.
        # DFS

        # { 0: [], 1: [], 2: [], 3: [], 4:[] }
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = set()

        def dfs(node, parent) -> bool:
            print(f"enter {node=} {parent=}")
            if node in visited:
                print(f"{node=} in visited")
                return False

            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n


