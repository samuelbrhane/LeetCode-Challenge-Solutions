class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        counts = Counter(nums)
        result = []
        path = []

        def backtrack():
            if len(path) == n:
                result.append(path[:])
                return

            for num in counts:
                if counts[num] > 0:
                    path.append(num)
                    counts[num] -= 1
                    backtrack()
                    counts[num] += 1
                    path.pop()
                    
        backtrack()
        return result