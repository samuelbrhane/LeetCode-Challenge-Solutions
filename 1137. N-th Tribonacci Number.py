class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def helper(x):
            if x in memo:
                return memo[x]
            
            if x == 0:
                result = 0
            elif x == 1 or x == 2:
                result = 1
            else:
                result = helper(x - 1) + helper(x - 2) + helper(x - 3)
            
            memo[x] = result
            return result

        return helper(n)