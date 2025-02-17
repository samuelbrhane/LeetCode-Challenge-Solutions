class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
     
        while left <= right:
            mid = (right + left) // 2
            row, col = divmod(mid, cols)
            matrix_val = matrix[row][col]

            if matrix_val == target:
                return True
            elif matrix_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False