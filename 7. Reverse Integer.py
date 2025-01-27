class Solution:
    def reverse(self, x: int) -> int:
        max_val = pow(2, 31) - 1
        negative = x < 0
        x = abs(x)
        result = 0
        
        while x:
            digit = x % 10
            x //= 10

            if result > (max_val - digit) // 10: 
                return 0

            result = (result * 10) + digit 

        return -result if negative else result