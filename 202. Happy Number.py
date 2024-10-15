class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()

        while n not in hash_set:
            hash_set.add(n)
            n = self.square_sum(n)

            if n == 1:
                return True

        return False
    
    def square_sum(self, n: int) -> int:
        new_sum = 0

        while n:
            remainder = n % 10
            new_sum += pow(remainder, 2)
            n //= 10

        return new_sum