class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0

        def binary_search(start, target):
            left, right = start, len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left

        for i in range(len(nums)):
            left = binary_search(i + 1, lower - nums[i])
            right = binary_search(i + 1, upper - nums[i] + 1)
            count += (right - left)

        return count