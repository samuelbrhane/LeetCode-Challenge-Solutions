class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cache = {}
        durations = [1, 7, 30]

        def dfs(idx):
            if idx == n:
                return 0
            if idx in cache:
                return cache[idx]
                
            result = float("inf")
            new_idx = idx
            for index, cost in enumerate(costs):
                while new_idx < n and days[new_idx] < days[idx] + durations[index]:
                    new_idx += 1

                result = min(result, cost + dfs(new_idx)) 

            cache[idx] = result
            return result

        return dfs(0)