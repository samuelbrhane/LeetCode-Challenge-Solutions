class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
  
        while left < right:
            if s[left] != s[right]:
                return self.check_palindrome(s, left + 1, right) or self.check_palindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True

    def check_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

        
