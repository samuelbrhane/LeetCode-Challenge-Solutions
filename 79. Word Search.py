class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        def dfs(r, c, idx):
            if idx == n:
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or word[idx] != board[r][c]:
                return False

            temp = board[r][c]
            board[r][c] = "*"

            result = (dfs(r + 1, c, idx + 1) or
                    dfs(r - 1, c, idx + 1) or
                    dfs(r, c + 1, idx + 1) or
                    dfs(r, c - 1, idx + 1))

            board[r][c] = temp   
            return result

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False