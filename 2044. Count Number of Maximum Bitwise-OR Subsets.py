class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = {0:1}
        max_or = 0

        for num in nums:
            dp_copy = dp.copy()
            for current, count in dp.items():
                new_or = num | current 
                dp_copy[new_or] = dp_copy.get(new_or, 0) + count

            dp = dp_copy
            
        max_or = max(dp.keys())

        return dp[max_or]
