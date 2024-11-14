class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]
        
        longest_substring = ""
        for i in range(len(s)):
            odd_palindrome = check_palindrome(i, i)
            even_palindrome = check_palindrome(i, i + 1)
            longest_substring = max(longest_substring, odd_palindrome, even_palindrome, key=len)

        return longest_substring
            