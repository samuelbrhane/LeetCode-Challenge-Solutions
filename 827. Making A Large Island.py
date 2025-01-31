class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        size = defaultdict(int) 
        label = 2 
        result = 0

        def in_bounds(r, c):
            return 0 <= r < n and 0 <= c < n

        def dfs(r, c, label):
            if not in_bounds(r, c) or grid[r][c] != 1:
                return 0

            grid[r][c] = label  
            island_size = 1  

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                island_size += dfs(nr, nc, label)  
            
            return island_size

        # Label islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    result = max(result, size[label])  
                    label += 1  

        # If the whole grid is 1s, return n * n
        if result == n * n:
            return result

        def connect(r, c):
            visited_labels = set()
            new_size = 1 

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] > 1:
                    island_label = grid[nr][nc]
                    if island_label not in visited_labels:
                        new_size += size[island_label]
                        visited_labels.add(island_label)

            return new_size

        # Try turning each 0 into a 1 and calculate the largest possible island
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    result = max(result, connect(r, c))

        return result
