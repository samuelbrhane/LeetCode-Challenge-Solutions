class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2 * n  - 1)
        used = set()

        def backtrack(i):
            if i == len(result):
                return True

            for num in reversed(range(1, n + 1)):
                if num in used:
                    continue
                if num > 1 and (i + num >= len(result) or result[i + num]):
                    continue

                used.add(num)
                result[i] = num

                if num > 1:
                    result[i + num] = num

                j = i + 1
                while j < len(result) and result[j]:
                    j += 1

                if backtrack(j):
                    return True
                
                used.remove(num)
                result[i] = 0

                if num > 1:
                    result[i + num] = 0
                    
        backtrack(0)
        return result