class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        distinct = set()
        color_count = defaultdict(int)
        result = []

        for x, y in queries:
            if x in ball_color:
                color = ball_color[x]
                color_count[color] -= 1

                if color_count[color] == 0:
                    distinct.remove(color)

            ball_color[x] = y
            color_count[y] += 1
            distinct.add(y)

            result.append(len(distinct))

        return result