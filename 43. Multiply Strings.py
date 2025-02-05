class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)  

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_val = product + result[i + j + 1]

                result[i + j + 1] = sum_val % 10
                result[i + j] += sum_val // 10  

        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str if result_str else "0"