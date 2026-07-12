class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = [[0 for i in range(col)]for j in range(row)]
        count = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or visited[r][c] == 1 or grid[r][c] == "0":
                return
            
            visited[r][c] = 1

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    count += 1
                    dfs(r,c)

        return count