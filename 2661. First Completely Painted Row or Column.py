class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row, col = [0] * rows, [0] * cols

        hash_map = {}
        for r in range(rows):
            for c in range(cols):
                hash_map[mat[r][c]] = (r, c)

        for i in range(len(arr)):
            r, c = hash_map[arr[i]]   
            row[r] += 1
            col[c] += 1

            if row[r] == cols or col[c] == rows:
                return i