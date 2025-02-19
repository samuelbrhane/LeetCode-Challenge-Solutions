class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        result = []
        
        for i in range(len(nums)):
            if i + 1 not in num_set:
                result.append(i + 1)

        return result