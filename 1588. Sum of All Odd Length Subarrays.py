class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        total_sum = 0
        for length in range(1, n + 1, 2): 
            for start in range(n - length + 1):
                end = start + length
                total_sum += prefix[end] - prefix[start]

        return total_sum