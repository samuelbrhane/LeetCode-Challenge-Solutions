class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n == 1:
                return 0
            if n in memo:
                return memo[n]

            if n % 2 == 0:
                memo[n] = 1 + helper(n // 2)
            else:
                memo[n] = 1 + min(helper(n + 1), helper(n - 1))

            return memo[n]

        return helper(n)