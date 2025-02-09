class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        good_pairs = 0
        counts = defaultdict(int)
        
        for i in range(n):
            good_pairs += counts[nums[i] - i]
            counts[nums[i] - i] += 1

        return total_pairs - good_pairs