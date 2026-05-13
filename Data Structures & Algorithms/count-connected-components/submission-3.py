class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        # Recursively loop through neighbors
        # If a neighbor has no neighbors, that means we have +1 connected component.
        # We need to keep track of the nodes we visited.
        #   Ex. 0 -> 1 -> 2 is a connected component
        #       but so would 1 -> 2. That shouldn't count.

        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        print(f"{adj_list}")

        visited = set()
        result = 0

        def dfs(node):
            if node in visited:
                return
                
            visited.add(node)

            neighbors = adj_list[node]

            for neighbor in adj_list[node]:
                dfs(neighbor)

        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1

        return result