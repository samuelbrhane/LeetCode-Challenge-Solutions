class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hash_map = {}
        max_val = -1

        def get_sum(num):
            result = 0

            while num:
                result += num % 10
                num //= 10

            return result

        for num in nums:
            num_sum = get_sum(num)
            if num_sum in hash_map:
                max_val = max(max_val, num + hash_map[num_sum])
                hash_map[num_sum] = max(num, hash_map[num_sum])
            else:
                hash_map[num_sum] = num

        return max_val