class Solution:
    def minimumLength(self, s: str) -> int:
        counts = Counter(s)
        result = 0

        for char,val in counts.items():
            if val > 2:
                if val % 2:
                    result += 1
                else:
                    result += 2
            else:
                result += val

        return result