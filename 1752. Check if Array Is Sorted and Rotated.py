class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                count += 1
      
        if nums[-1] > nums[0]:
            count += 1
       
        return count <= 1