class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1] * len(queries)
        groups = defaultdict(list)
        for idx, q in enumerate(queries):
            l, r = sorted(q)

            if l == r or heights[r] > heights[l]:
                result[idx] = r
            else:
                max_val = max(heights[r], heights[l])
                groups[r].append((max_val, idx))

        min_heap = []
        for idx, h in enumerate(heights):

            for g_h, g_i in groups[idx]:
                heapq.heappush(min_heap, (g_h, g_i))

            while min_heap and h > min_heap[0][0]:
                g_h, g_i = heapq.heappop(min_heap)
                result[g_i] = idx

        return result

