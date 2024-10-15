from typing import List
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        min_swap = float('inf')
        ones_idx = [i for i, num in enumerate(nums) if num == 1]
        n = len(ones_idx)
        prefix_sum = [0] * (n + 1)
    
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + ones_idx[i - 1]

        for i in range(n - k + 1):
            mid = i + k // 2
            left_cost = ones_idx[mid] * (mid - i) - (prefix_sum[mid] - prefix_sum[i])
            right_cost = (prefix_sum[i + k] - prefix_sum[mid + 1]) - ones_idx[mid] * (i + k - mid - 1)
            min_swap = min(min_swap, left_cost + right_cost)

        r = (k - 1) // 2
        min_swap -= r * (r + 1) // 2 * 2 + ((r + 1) if k % 2 == 0 else 0)

        return min_swap


