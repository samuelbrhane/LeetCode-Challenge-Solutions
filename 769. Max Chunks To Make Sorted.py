class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        main_sum = curr_sum = 0
        result = 0
        for i in range(len(arr)):
            main_sum += i
            curr_sum += arr[i]

            if main_sum == curr_sum:
                result += 1

        return result