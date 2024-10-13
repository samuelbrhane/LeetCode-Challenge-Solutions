from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        min_swap = float('inf')

        # Extract the indices where nums[i] is 1
        ones_idx = [i for i, num in enumerate(nums) if num == 1]
        n = len(ones_idx)

        # Create a prefix sum array
        prefix_sum = [0] * (n + 1)
    
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + ones_idx[i - 1]

        for i in range(n - k + 1):
            mid = i + k // 2
            left_cost = ones_idx[mid] * (mid - i) - (prefix_sum[mid] - prefix_sum[i])
            right_cost = (prefix_sum[i + k] - prefix_sum[mid + 1]) - ones_idx[mid] * (i + k - mid - 1)
            min_swap = min(min_swap, left_cost + right_cost)

        # Subtract moves around the median
        r = (k - 1) // 2
        min_swap -= r * (r + 1) // 2 * 2 + ((r + 1) if k % 2 == 0 else 0)

        return min_swap


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1,0,0,1,0,1]
    k1 = 2
    print("Example 1 Output:", solution.minMoves(nums1, k1))  # Output: 1

    # Example 2
    nums2 = [1,0,0,0,0,0,1,1]
    k2 = 3
    print("Example 2 Output:", solution.minMoves(nums2, k2))  # Output: 5

    # Example 3
    nums3 = [1,1,0,1]
    k3 = 2
    print("Example 3 Output:", solution.minMoves(nums3, k3))  # Output: 0
