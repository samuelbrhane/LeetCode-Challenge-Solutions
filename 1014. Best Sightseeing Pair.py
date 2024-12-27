class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = 0
        curr_max = values[0]

        for i in range(1, len(values)):
            result = max(result, curr_max + values[i] - 1)
            curr_max = max(curr_max - 1, values[i])

        return result