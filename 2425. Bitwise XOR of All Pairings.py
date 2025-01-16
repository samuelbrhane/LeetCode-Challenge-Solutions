class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        if len(nums2) % 2:
            for n in nums1:
                result ^= n

        if len(nums1) % 2:
            for n in nums2:
                result ^= n

        return result