class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()
        result = []

        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prev_height):
                return

            visited.add((r, c))

            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for i in range(COLS):
            dfs(0, i, pacific, heights[0][i])
            dfs(ROWS - 1, i, atlantic, heights[ROWS - 1][i])

        for i in range(ROWS):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, COLS - 1, atlantic, heights[i][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
            
        return result
                
        