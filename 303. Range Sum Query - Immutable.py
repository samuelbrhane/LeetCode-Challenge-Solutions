class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix_sum = [0] * (n + 1)

        for i in range(n):
            self.prefix_sum[i + 1] = nums[i] + self.prefix_sum[i]

    def sumRange(self, left: int, right: int) -> int:
        result = self.prefix_sum[right + 1] - self.prefix_sum[left]
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)