class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        visited = [False] * n
        def backtrack(path):
            if len(path) == n:
                result.append(path[:])
                return

            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    visited[i] = False

        backtrack([])
        print(result)
        return result