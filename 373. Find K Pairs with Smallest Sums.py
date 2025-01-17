class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        min_heap = []

        min_len = min(len(nums2), k)

        for j in range(min_len):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

        while min_heap and len(result) < k:
            cur_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return result