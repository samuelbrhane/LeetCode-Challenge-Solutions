class Solution:
    def minimumSteps(self, s: str) -> int:
        swap_count = 0
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == "1" and s[right] == "0":
                swap_count += (right - left)
                left += 1
                right -= 1
            if s[left] != "1":
                left += 1
            if s[right] != "0":
                right -= 1

        return swap_count
