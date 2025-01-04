class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        unique_chars = set(s) 

        for char in unique_chars:
            first = s.find(char)
            last = s.rfind(char)

            if last - first > 1:
                middle_chars = set(s[first + 1:last])
                result += len(middle_chars)

        return result