class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float("inf")

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum

        return closest_sum