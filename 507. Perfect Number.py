class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisor_sum = 1
        sqrt_num = int(num ** 0.5)
        
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                divisor_sum += i + (num // i if i != num // i else 0)
        
        return divisor_sum == num