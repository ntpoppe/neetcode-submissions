class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        result = 0

        def dfs(i, j, parent = False):
            nonlocal visited
            nonlocal result

            if visited[i][j] == True:
                return

            visited[i][j] = True

            if grid[i][j] == "0":
                return

            if i - 1 >= 0:
                dfs(i - 1, j)

            if j + 1 < COLS:
                dfs(i, j + 1)

            if i + 1 < ROWS:
                dfs(i + 1, j)

            if j - 1 >= 0:
                dfs(i, j - 1)

            if parent == True:
                result += 1

        for i in range(ROWS):
            for j in range(COLS):
                if visited[i][j] == True:
                    continue

                dfs(i, j, True)

        return result