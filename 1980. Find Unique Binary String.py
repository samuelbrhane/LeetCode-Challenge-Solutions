class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)
        n = len(nums[0])
        result = []

        def backtrack(path):
            if len(path) == n:
                join_str = "".join(path)
                if join_str not in num_set:
                    result.append(join_str)
                return

            for char in "01":
                backtrack(path + [char])

                if result:
                    return

        backtrack([])
        return result[0]