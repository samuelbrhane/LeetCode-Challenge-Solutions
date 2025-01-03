class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] + nums + [0]
      
        right_sum = sum(prefix_sum)
        left_sum = 0

        for i in range(len(nums)):
            right_sum -= prefix_sum[i + 1]
            left_sum += prefix_sum[i]

            if right_sum == left_sum:
                return i

        return -1
