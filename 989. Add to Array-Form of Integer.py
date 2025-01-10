class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        result = []

        while k > 0 or i >= 0:
            if i >= 0:
                k += num[i]
            result.append(k % 10)
            k = k // 10
            i -= 1

        return result[::-1]