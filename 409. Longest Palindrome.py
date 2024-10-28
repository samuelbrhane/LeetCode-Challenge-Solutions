from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        hash_map = defaultdict(int)

        for char in s:
            hash_map[char] += 1
        
        odd = False
        for key, val in hash_map.items():
            if val % 2 == 0:
                result += val
            else:
                result += (val - 1)
                odd = True

        if odd:
            result += 1

        return result