class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = defaultdict(int)
        result = [-1] * len(nums1)

        for idx, num in enumerate(nums1):
            index_map[num] = idx

        for i, num in enumerate(nums2):
            if num not in index_map:
                continue

            idx = index_map[num]
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    result[idx] = nums2[j]
                    break

        return result