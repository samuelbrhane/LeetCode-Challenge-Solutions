class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        str_length = 2 ** n - 1

        def helper(length: int, k: int) -> str:
            if length == 1:
                return "0"
            
            half = length // 2
            if k == half + 1:
                return "1"
            elif k <= half:
                return helper(half, k)
            else:
                result = helper(half, 1 + length - k)
                return "0" if result == "1" else "1"

        return helper(str_length, k)