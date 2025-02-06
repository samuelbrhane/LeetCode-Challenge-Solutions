class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_map = defaultdict(int)
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                product_map[prod] += 1

        for count in product_map.values():
            if count > 1:
                result += (count * (count - 1) // 2) * 8

        
        return result