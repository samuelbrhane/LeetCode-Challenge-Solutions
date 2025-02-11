class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        added = False

        for start, end in intervals:
            if newInterval[0] <= end and newInterval[1] >= start and not added:
                result.append([min(start, newInterval[0]), max(end, newInterval[1])])
                added = True
            elif result and start <= result[-1][1]:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])

        if not intervals or not added:
            result.append(newInterval)

        result.sort(key = lambda x: x[0])

        return result