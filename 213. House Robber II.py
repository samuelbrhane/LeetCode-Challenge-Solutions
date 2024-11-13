class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        def helper(nums):
            prev1, prev2 = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                current = max(prev2, nums[i] + prev1)
                prev1, prev2 = prev2, current

            return prev2

        return max(helper(nums[1:]), helper(nums[:-1]))