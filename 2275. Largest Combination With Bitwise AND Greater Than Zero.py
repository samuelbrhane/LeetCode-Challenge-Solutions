class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_comb = 0
        for i in range(32):
            count = 0
            for num in candidates:
                count += 1 if (1 << i) & num else 0
            max_comb = max(max_comb, count)

        return max_comb