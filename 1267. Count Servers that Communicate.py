class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_count, col_count = [0] * rows, [0] * cols
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    row_count[r] += 1
                    col_count[c] += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and max(row_count[r], col_count[c]) > 1:
                    result += 1

        return result