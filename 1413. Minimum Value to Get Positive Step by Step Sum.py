class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        min_val = min(prefix)

        return 1 - min_val if min_val < 0 else 1