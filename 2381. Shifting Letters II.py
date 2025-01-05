class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)
        
        for start, end, direction in shifts:
            prefix[end + 1] += 1 if direction == 1 else -1
            prefix[start] += 1 if direction == 0 else -1

        diff = 0
        result = [ord(char) - ord("a") for char in s]
        
        for i in range(n, -1, -1):
            diff += prefix[i]

            result[i - 1] = (result[i - 1] + diff) % 26

        result = [chr(ord("a") + i) for i in result]
        return "".join(result)