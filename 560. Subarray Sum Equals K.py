class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cur_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            cur_sum += num
            diff = cur_sum - k

            result += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

        return result