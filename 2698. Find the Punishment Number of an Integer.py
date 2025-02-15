class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        def partition(i, curr, target, string):
            if i == len(string) and curr == target:
                return True

            for j in range(i, len(string)):
                if partition(j + 1, curr + int(string[i:j+1]), target, string):
                    return True
            return False

        for i in range(1, n + 1):
            if partition(0, 0, i, str(i*i)):
                result += i * i 
        
        return result