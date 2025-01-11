class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        result = [0]

        def backtrack(idx):
            if idx > n:
                result[0] += 1
                return

            for i in range(1, n + 1):
                if not visited[i] and (idx % i == 0 or i % idx == 0):
                    visited[i] = True
                    backtrack(idx + 1)
                    visited[i] = False


        backtrack(1)
        return result[0]