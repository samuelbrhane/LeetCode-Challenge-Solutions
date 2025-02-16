class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        created = [[False] * cols for _ in range(rows)]

        def fill_zeros(r, c):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                while 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc]:
                        matrix[nr][nc] = 0
                        created[nr][nc] = True

                    nr += dr
                    nc += dc

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0 and not created[r][c]:
                    fill_zeros(r, c)