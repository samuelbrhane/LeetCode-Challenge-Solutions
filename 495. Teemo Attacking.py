class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        timeSeries = [timeSeries[0] - duration] + timeSeries
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i - 1]
            if diff >= duration:
                result += duration
            else:
                result += diff

        return result
