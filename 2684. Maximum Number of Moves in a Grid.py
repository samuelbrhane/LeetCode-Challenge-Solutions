class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = {}

        def dp(r, c):
            if c == COLS - 1:
                return 0

            if (r, c) in visited:
                return visited[(r, c)]

            curr_max = 0 
            if r > 0 and grid[r - 1][c + 1] > grid[r][c]:
                curr_max = max(curr_max, dp(r - 1, c + 1) + 1)

            if grid[r][c + 1] > grid[r][c]:
                curr_max = max(curr_max, dp(r, c + 1) + 1)

            if r < ROWS - 1 and grid[r + 1][c + 1] > grid[r][c]:
                curr_max = max(curr_max, dp(r + 1, c + 1) + 1)

            visited[(r, c)] = curr_max

            return curr_max
    
        max_moves = 0
        for row in range(ROWS):
            max_moves = max(max_moves, dp(row, 0))

        return max_moves