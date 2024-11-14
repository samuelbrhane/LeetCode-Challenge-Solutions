class Solution:
    def countSubstrings(self, s: str) -> int:
        def check_palindrome(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        result = 0
        for i in range(len(s)):
            odd_count = check_palindrome(i, i)
            even_count = check_palindrome(i, i + 1)
            result += (odd_count + even_count)

        return result