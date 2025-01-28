class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        result = 0
        sign = 1
        max_val, min_val = pow(2, 31) - 1, pow(-2, 31)

        while i < n and s[i] == " ":
            i += 1

        if i < n and s[i] in ["-", "+"]:
            if s[i] == "-":
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (max_val - digit) // 10:
                return max_val if sign == 1 else min_val

            result = (result * 10) + digit

            i += 1

        return result * sign