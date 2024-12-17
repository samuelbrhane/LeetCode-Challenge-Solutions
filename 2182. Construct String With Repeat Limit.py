class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = []
        char_count = Counter(s)
        max_heap = [(-ord(char), count) for char, count in char_count.items()]
        heapq.heapify(max_heap)

        while max_heap:
            curr_ord, curr_count = heapq.heappop(max_heap)
            curr_limit = min(curr_count, repeatLimit)
            result.append(chr(-curr_ord) * curr_limit)

            if curr_count - curr_limit > 0 and max_heap:
                next_ord, next_count = heapq.heappop(max_heap)
                result.append(chr(-next_ord))

                heapq.heappush(max_heap, (curr_ord, curr_count - curr_limit))

                if next_count > 1:
                    heapq.heappush(max_heap, (next_ord, next_count - 1))

     
        return "".join(result)