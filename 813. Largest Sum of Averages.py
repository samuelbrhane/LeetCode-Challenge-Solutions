class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def mean(i, j):
            return (prefix[j + 1] - prefix[i]) / (j - i + 1)

        memo = {}
        def dfs(i, k):
            if (i, k) in memo:
                return memo[(i, k)]

            if k == 1:
                return mean(i, n - 1)

            max_score = 0
            for j in range(i, n - k + 1): 
                max_score = max(max_score, mean(i, j) + dfs(j + 1, k - 1))

            memo[(i, k)] = max_score
            return max_score

        return dfs(0, k)