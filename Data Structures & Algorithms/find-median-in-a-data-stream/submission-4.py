import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        len1, len2 = len(self.minHeap), len(self.maxHeap)
        if abs(len1 - len2) > 1:
            if len2 > len1:
                popFrom = self.maxHeap
                popInto = self.minHeap
            else:
                popFrom = self.minHeap
                popInto = self.maxHeap

            heapq.heappush(popInto, -heapq.heappop(popFrom))

    def findMedian(self) -> float:

        if len(self.minHeap) == len(self.maxHeap):
            a1 = self.minHeap[0]
            a2 = -self.maxHeap[0]
            return (a1 + a2) / 2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]


        