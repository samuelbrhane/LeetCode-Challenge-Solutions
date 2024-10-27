class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            count = 0
            start = 0

            for end in range(len(nums)):
                while start < len(nums) and nums[start] - nums[end] <= mid:
                    start += 1

                count += start - end - 1

            if count >= k:
                right = mid
            else:
                left = mid + 1
                
        return left