class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        cache = {}

        def helper(length):
            if length > high:
                return 0

            if length in cache:
                return cache[length]

            result = 1 if length >= low else 0
            result += helper(length + zero) + helper(length + one)
            cache[length] = result

            return result % mod

        return helper(0)