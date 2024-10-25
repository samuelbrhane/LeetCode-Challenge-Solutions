class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            average = (-self.maxheap[0] + self.minheap[0]) / 2
            return average



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()