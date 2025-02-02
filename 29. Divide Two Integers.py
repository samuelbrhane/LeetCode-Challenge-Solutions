class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX 

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Shift divisor left until it's just smaller than dividend
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1  

            # Subtract the largest multiple from dividend
            dividend -= temp
            quotient += multiple

        # Apply sign and clamp result within 32-bit range
        return max(INT_MIN, min(INT_MAX, quotient * sign))