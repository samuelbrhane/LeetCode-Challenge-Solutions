class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_streak, dec_streak = 0, 0
        result = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_streak += 1
                dec_streak = 0
            elif nums[i] < nums[i - 1]:
                dec_streak += 1
                inc_streak = 0
            else:
                dec_streak = 0
                inc_streak = 0
                
            result = max(result, dec_streak, inc_streak)

        return result + 1