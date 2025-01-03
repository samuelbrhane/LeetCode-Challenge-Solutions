class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        n = len(nums)
        result = 0

        for i in range(n - 1):
            left_sum += nums[i]
            right_sum -= nums[i]

            if left_sum >= right_sum:
                result += 1

        return result