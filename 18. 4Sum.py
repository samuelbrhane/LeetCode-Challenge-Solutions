class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                start = j + 1
                end = len(nums) - 1
                
                while start < end:
                    num_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if num_sum == target:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1

                        while start < end and nums[start] == nums[start - 1]:
                            start += 1

                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1

                    elif num_sum < target:
                        start += 1
                    else:
                        end -= 1

        return result