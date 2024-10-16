class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        string = ""

        for num, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if num:
                heapq.heappush(max_heap, (num, char))

        while max_heap:
            num, char = heapq.heappop(max_heap)
            if len(string) >= 2 and string[-1] == string[-2] == char:
                if not max_heap:
                    break
                num2, char2 = heapq.heappop(max_heap)
                string += char2
                num2 += 1

                if num2:
                    heapq.heappush(max_heap, (num2, char2))
            else:
                string += char
                num += 1
            
            if num:
                heapq.heappush(max_heap, (num, char))

        return string