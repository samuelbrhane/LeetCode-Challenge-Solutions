class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hash_map = {0: -1}
        num_sum = 0

        for i in range(n):
            num_sum += nums[i]
            reminder = num_sum % k
            if reminder in hash_map:
                if i - hash_map[reminder] >= 2:
                    return True
            else:
                hash_map[reminder] = i

        return False
