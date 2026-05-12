class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        result = 0

        def dfs(i, j):
            nonlocal result

            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for dr, dc in DIRECTIONS:
                dfs(i + dr, j + dc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1

        return result