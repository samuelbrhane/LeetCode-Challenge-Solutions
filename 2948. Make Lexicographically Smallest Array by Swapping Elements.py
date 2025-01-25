class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        result = []
        groups = []
        num_group = {}
        
        for num in sorted(nums):
            if not groups or abs(num - groups[-1][-1] > limit):
                groups.append(deque())

            groups[-1].append(num)
            num_group[num] = len(groups) - 1


        for num in nums:
            group_idx = num_group[num]
            result.append(groups[group_idx].popleft())

        return result
