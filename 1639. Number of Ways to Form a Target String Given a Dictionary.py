class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7

        count =  defaultdict(int)
        for word in words:
            for idx, char in enumerate(word):
                count[(idx, char)] += 1

        cache = {}
        def dfs(i, k):
            if i == len(target):
                return 1
            if k == len(words[0]):
                return 0
            if (i, k) in cache:
                return cache[(i, k)]

            char = target[i]
            cache[(i, k)] = dfs(i, k + 1)
            cache[(i, k)] += count[(k, char)] * dfs(i + 1, k + 1)

            return cache[(i, k)] % mod

        return dfs(0, 0)


