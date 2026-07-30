import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []
        # heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        self.heap = sorted(self.heap)
        # heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        size = len(self.heap)
        if size % 2 == 0:
            # a1 = heapq.nlargest(size // 2 - 1, self.heap)
            # a2 = heapq.nlargest(size // 2, self.heap)
            # print(a1)
            # print(a2)

            a1 = self.heap[size // 2 - 1]
            a2 = self.heap[size // 2]
            print(self.heap)
            print(a1, a2)
            return (a1 + a2) / 2
        else:
            return self.heap[size // 2]
        