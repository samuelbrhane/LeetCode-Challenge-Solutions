class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = [-1] * (len(nums) - k + 1)
        streak = 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1

            if streak == k:
                result[i - k + 1] = nums[i]
                streak -= 1

        return result