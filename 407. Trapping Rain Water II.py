class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        visited_cell = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = []
        result, max_height = 0, 0
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1) or (c == 0 or c == cols - 1):
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited_cell[r][c] = True

        while min_heap:
            h, r, c = heapq.heappop(min_heap)
            max_height = max(max_height, h)
            result += max_height - h

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited_cell[nr][nc]:
                    visited_cell[nr][nc] = True
                    heapq.heappush(min_heap, (heightMap[nr][nc], nr, nc))

        return result