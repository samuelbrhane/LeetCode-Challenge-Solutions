class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x):
            count = 0
            for q in quantities:
                count += math.ceil(q / x)

            return count <= n
        
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left