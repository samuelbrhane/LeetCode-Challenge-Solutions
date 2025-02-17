class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = deque()
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while carry or i >= 0 or j >= 0:
            int1 = int(num1[i]) if i >= 0 else 0
            int2 = int(num2[j]) if j >= 0 else 0

            num_sum = carry + int1 + int2
            carry = num_sum // 10
            num = num_sum % 10
            result.appendleft(str(num))

            i -= 1
            j -= 1

        return "".join(result)