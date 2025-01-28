class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        max_fish = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or not grid[r][c]:
                return 0

            visited[r][c] = True
            curr_fish = grid[r][c]
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for direction in directions:
                dr, dc = direction
                nr, nc = r + dr, c + dc

                curr_fish += dfs(nr, nc)

            return curr_fish


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and not visited[r][c]:
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish