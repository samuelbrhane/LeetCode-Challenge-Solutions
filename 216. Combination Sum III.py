class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(i, path, total):
            if len(path) == k and total == n:
                result.append(path[::])
                return

            for i in range(i, 10):
                if total + i > n:
                    break

                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
            

        backtrack(1, [], 0)
        return result