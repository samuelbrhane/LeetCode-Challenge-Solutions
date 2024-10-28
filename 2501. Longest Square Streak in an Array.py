class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] = hash_map[num * num] + 1
          
        max_value = max(hash_map.values())   

        return max_value if max_value >= 2 else -1