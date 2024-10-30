class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        LIS = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        LDS = [1] * n
        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], 1 + LDS[j])
        
        min_removal = n
        for i in range(1, n - 1):
            if min(LIS[i], LDS[i]) > 1:
                min_removal = min(min_removal, n - LIS[i] - LDS[i] + 1)

        return min_removal