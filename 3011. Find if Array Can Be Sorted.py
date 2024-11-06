class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(n):
            return bin(n).count("1")

        cur_min, cur_max = nums[0], nums[0]
        prev_max = float("-inf")

        for num in nums:
            if count_bits(num) == count_bits(cur_min):
                cur_min = min(cur_min, num)
                cur_max = max(cur_max, num)
            else:
                if cur_min < prev_max:
                    return False

                prev_max = cur_max
                cur_min, cur_max = num, num

        return False if cur_min < prev_max else True
        