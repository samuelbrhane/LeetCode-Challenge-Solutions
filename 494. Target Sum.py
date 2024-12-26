class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(index, curr_sum):
            if (index, curr_sum) in cache:
                return cache[(index, curr_sum)]

            if index == len(nums):
                return 1 if curr_sum == target else 0

            result = (backtrack(index + 1, curr_sum + nums[index]) + 
                      backtrack(index + 1, curr_sum - nums[index]))

            cache[(index, curr_sum)] = result

            return result

        return backtrack(0, 0)