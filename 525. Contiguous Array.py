class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros = 0
        ones = 0
        result = 0
        hash_map = defaultdict(int)

        for idx, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1

            if (ones - zeros) not in hash_map:
                hash_map[ones - zeros] = idx

            if ones == zeros:
                result = ones + zeros
            else:
                i = hash_map[ones - zeros]
                result = max(result, idx - i)

        return result