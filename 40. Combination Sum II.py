class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        candidates.sort()

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])


        backtrack(0, target, [])
        return result