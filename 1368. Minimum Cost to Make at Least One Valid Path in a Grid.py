class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited_cell = [[False for _ in range(cols)] for _ in range(rows)]
        dq = deque([(0, 0, 0)])
        directions = {
            1: [0, 1],
            2: [0, -1], 
            3: [1, 0],
            4: [-1, 0]
        }

        while dq:
            r, c, cost = dq.popleft()

            if r == rows - 1 and c == cols - 1:
                return cost

            if visited_cell[r][c]:
                continue

            visited_cell[r][c] = True

            for direction, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited_cell[nr][nc]:
                    if direction == grid[r][c]:
                        dq.appendleft((nr, nc, cost))
                    else:
                        dq.append((nr, nc, cost + 1))

      