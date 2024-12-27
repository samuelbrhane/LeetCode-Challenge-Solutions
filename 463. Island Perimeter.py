class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited_cell = set()
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:
                return 1

            if (r, c) in visited_cell:
                return 0

            visited_cell.add((r, c))

            perimeter = 0
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r, c - 1)

            return perimeter

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r, c)