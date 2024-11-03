class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for idx, num in enumerate(nums):
            nums[idx] = str(num)

        def compare(x1, x2):
            if x1 + x2 > x2 + x1:
                return -1
            else:
                return 1
                
        nums.sort(key=cmp_to_key(compare))
        result = "".join(nums)

        return str(int(result))