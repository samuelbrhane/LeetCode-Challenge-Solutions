class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        result = [[0] * cols for _ in range(rows)]
        visited_cell = set()
        dq = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    visited_cell.add((r, c))
                    dq.append((r,c))

        while dq:
            r, c = dq.popleft()
            
            for direction in directions:
                dr, dc = direction
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited_cell:
                    result[nr][nc] = result[r][c] + 1
                    visited_cell.add((nr, nc))
                    dq.append((nr, nc))
                    
        return result

                