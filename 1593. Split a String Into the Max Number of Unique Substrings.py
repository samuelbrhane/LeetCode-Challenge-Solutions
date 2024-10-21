class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def backtrack(i, unique_substr):
            if i == len(s):
                return len(unique_substr)

            max_count = 0

            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]

                if substr not in unique_substr:
                    unique_substr.add(substr)
                    max_count = max(max_count, backtrack(j, unique_substr))
                    unique_substr.remove(substr)

            return max_count

        return backtrack(0, set())