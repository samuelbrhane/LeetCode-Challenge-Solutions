class Solution:
    def maxScore(self, s: str) -> int:
        right_sum = sum([int(s[i]) for i in range(1, len(s))])
        left_sum = 1 if s[0] == "0" else 0
        total_sum = left_sum + right_sum
        max_sum = total_sum

        for i in range(1, len(s) - 1):
            if s[i] == "1":
                total_sum -= 1
            else:
                total_sum += 1

            max_sum = max(max_sum, total_sum)

        return max_sum