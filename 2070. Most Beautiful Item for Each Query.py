class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(sorted_queries)
        current_max, j = 0, 0

        for q, i in sorted_queries:

            while j < len(items) and items[j][0] <= q:
                current_max = max(current_max, items[j][1])
                j += 1

            result[i] = current_max

        return result
